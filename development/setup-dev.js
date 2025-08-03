#!/usr/bin/env node

/**
 * Development setup script for the website
 * This script sets up the development environment and provides instructions
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

console.log('🚀 Setting up your development environment...\n');

// Check if node_modules exists
if (!fs.existsSync('node_modules')) {
    console.log('📦 Installing dependencies...');
    try {
        execSync('npm install', { stdio: 'inherit' });
        console.log('✅ Dependencies installed successfully!\n');
    } catch (error) {
        console.error('❌ Failed to install dependencies');
        process.exit(1);
    }
} else {
    console.log('✅ Dependencies already installed\n');
}

// Check if content.json exists
const contentPath = path.join('src', 'data', 'content.json');
if (!fs.existsSync(contentPath)) {
    console.warn('⚠️  Warning: content.json file not found at src/data/content.json');
    console.log('   This file contains your website content. Make sure it exists before building.\n');
}

console.log('🎯 Available commands:');
console.log('  npm run build     - Build the website');
console.log('  npm run start     - Build and start development server');
console.log('  npm run clean     - Clean build directory');
console.log('');
console.log('📝 To edit your website content:');
console.log('  1. Edit src/data/content.json');
console.log('  2. Run npm run build');
console.log('  3. Your changes will be reflected in index.html');
console.log('');
console.log('🔧 Development workflow:');
console.log('  1. Edit content.json for text changes');
console.log('  2. Edit src/pug/index.pug for layout changes');
console.log('  3. Edit src/scss/ files for styling changes');
console.log('  4. Run npm run start for live development');
console.log('');
console.log('✨ Happy coding!');
