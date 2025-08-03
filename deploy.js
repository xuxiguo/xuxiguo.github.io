#!/usr/bin/env node

/**
 * Deploy Script
 * This script builds the website and copies files to the root for GitHub Pages deployment
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

console.log('🚀 Starting deployment process...\n');

try {
    // 1. Validate content
    console.log('1️⃣ Validating content...');
    execSync('node validate-content.js', { stdio: 'inherit' });
    
    // 2. Build the website
    console.log('\n2️⃣ Building website...');
    execSync('npm run build', { stdio: 'inherit' });
    
    // 3. Copy files to root
    console.log('\n3️⃣ Copying files for deployment...');
    
    // Copy main HTML file
    fs.copyFileSync('dist/index.html', 'index.html');
    console.log('   ✅ Copied index.html');
    
    // Copy CSS files
    if (fs.existsSync('dist/css')) {
        if (!fs.existsSync('css')) fs.mkdirSync('css', { recursive: true });
        const cssFiles = fs.readdirSync('dist/css');
        cssFiles.forEach(file => {
            fs.copyFileSync(path.join('dist/css', file), path.join('css', file));
        });
        console.log(`   ✅ Copied ${cssFiles.length} CSS file(s)`);
    }
    
    // Copy JS files
    if (fs.existsSync('dist/js')) {
        if (!fs.existsSync('js')) fs.mkdirSync('js', { recursive: true });
        const jsFiles = fs.readdirSync('dist/js');
        jsFiles.forEach(file => {
            fs.copyFileSync(path.join('dist/js', file), path.join('js', file));
        });
        console.log(`   ✅ Copied ${jsFiles.length} JS file(s)`);
    }
    
    // Copy assets if they exist
    if (fs.existsSync('dist/assets')) {
        const copyRecursive = (src, dest) => {
            if (!fs.existsSync(dest)) fs.mkdirSync(dest, { recursive: true });
            const items = fs.readdirSync(src);
            items.forEach(item => {
                const srcPath = path.join(src, item);
                const destPath = path.join(dest, item);
                if (fs.statSync(srcPath).isDirectory()) {
                    copyRecursive(srcPath, destPath);
                } else {
                    fs.copyFileSync(srcPath, destPath);
                }
            });
        };
        copyRecursive('dist/assets', 'assets');
        console.log('   ✅ Copied assets');
    }
    
    console.log('\n🎉 Deployment successful!');
    console.log('\n📝 Files ready for deployment:');
    console.log('   • index.html (main website)');
    console.log('   • css/styles.css (compiled styles)');
    console.log('   • js/scripts.js (JavaScript)');
    console.log('   • assets/ (images and other files)');
    
    console.log('\n💡 Next steps:');
    console.log('   1. Commit and push to GitHub');
    console.log('   2. Your GitHub Pages site will automatically update');
    
} catch (error) {
    console.error('\n❌ Deployment failed:', error.message);
    process.exit(1);
}
