#!/usr/bin/env node

/**
 * Content Update Helper
 * This script helps validate and update the content.json file
 */

const fs = require('fs');
const path = require('path');

const CONTENT_FILE = path.join(__dirname, 'src', 'data', 'content.json');

function validateContentFile() {
    try {
        const content = fs.readFileSync(CONTENT_FILE, 'utf8');
        const data = JSON.parse(content);
        
        console.log('✅ Content file is valid JSON');
        
        // Basic validation
        const requiredFields = ['meta', 'personal', 'about', 'navigation'];
        const missingFields = requiredFields.filter(field => !data[field]);
        
        if (missingFields.length > 0) {
            console.warn('⚠️  Missing required fields:', missingFields.join(', '));
        } else {
            console.log('✅ All required fields present');
        }
        
        // Check for common issues
        if (data.personal && !data.personal.email) {
            console.warn('⚠️  Email address is missing');
        }
        
        if (data.socialLinks && data.socialLinks.length === 0) {
            console.warn('⚠️  No social links configured');
        }
        
        return true;
    } catch (error) {
        console.error('❌ Content file validation failed:');
        console.error(error.message);
        return false;
    }
}

function showContentStats() {
    try {
        const content = fs.readFileSync(CONTENT_FILE, 'utf8');
        const data = JSON.parse(content);
        
        console.log('\n📊 Content Statistics:');
        console.log(`  • Navigation items: ${data.navigation ? data.navigation.length : 0}`);
        console.log(`  • Social links: ${data.socialLinks ? data.socialLinks.length : 0}`);
        console.log(`  • Publications: ${data.research?.publications ? data.research.publications.length : 0}`);
        console.log(`  • Working papers: ${data.research?.workingPapers ? data.research.workingPapers.length : 0}`);
        console.log(`  • Teaching positions: ${data.teaching ? data.teaching.length : 0}`);
        
        if (data.blockchain?.demos) {
            console.log(`  • Blockchain demos: ${data.blockchain.demos.length}`);
        }
        
    } catch (error) {
        console.error('❌ Could not read content statistics');
    }
}

function main() {
    console.log('🔍 Validating content file...\n');
    
    if (!fs.existsSync(CONTENT_FILE)) {
        console.error(`❌ Content file not found at: ${CONTENT_FILE}`);
        process.exit(1);
    }
    
    const isValid = validateContentFile();
    
    if (isValid) {
        showContentStats();
        console.log('\n🎉 Content file is ready!');
        console.log('\n💡 Next steps:');
        console.log('  1. Run "npm run build" to generate the website');
        console.log('  2. Run "npm run start" for development with live reload');
    } else {
        console.log('\n🔧 Please fix the issues above and run this script again.');
        process.exit(1);
    }
}

if (require.main === module) {
    main();
}

module.exports = {
    validateContentFile,
    showContentStats
};
