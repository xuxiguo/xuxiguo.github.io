#!/usr/bin/env node

/**
 * Build Script for Reorganized Structure
 * This script builds the website from the development directory
 */

const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

console.log('🚀 Building website from development directory...\n');

// Change to development directory
const developmentDir = path.join(__dirname, 'development');
process.chdir(developmentDir);

try {
    // Run the build process
    console.log('📦 Running npm build...');
    execSync('npm run build', { stdio: 'inherit' });
    
    // Copy built files to root
    console.log('\n📋 Copying built files to root directory...');
    
    const rootDir = path.join(__dirname);
    
    // Copy index.html
    if (fs.existsSync('index.html')) {
        fs.copyFileSync('index.html', path.join(rootDir, 'index.html'));
        console.log('✅ Copied index.html');
    }
    
    // Copy assets, css, js directories
    const dirsToSync = ['assets', 'css', 'js'];
    
    for (const dir of dirsToSync) {
        if (fs.existsSync(dir)) {
            // Remove existing directory in root
            const targetDir = path.join(rootDir, dir);
            if (fs.existsSync(targetDir)) {
                fs.rmSync(targetDir, { recursive: true, force: true });
            }
            
            // Copy new directory
            fs.cpSync(dir, targetDir, { recursive: true });
            console.log(`✅ Copied ${dir}/`);
        }
    }
    
    console.log('\n🎉 Build completed successfully!');
    console.log('📁 Your website files are ready in the root directory for GitHub Pages');
    
} catch (error) {
    console.error('❌ Build failed:', error.message);
    process.exit(1);
}
