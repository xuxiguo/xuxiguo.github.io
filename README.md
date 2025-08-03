# Norman Guo's Personal Website

This is a modern, data-driven personal website built with a static site generator approach using Pug templates, SCSS, and JSON data files.

## 🚀 Key Features

- **Data-Driven Content**: All website content is managed through a single JSON file
- **Modern Build System**: Uses Pug templates, SCSS compilation, and automatic builds
- **Responsive Design**: Bootstrap-based responsive layout
- **Development Server**: Live reload for efficient development
- **Easy Maintenance**: No need to edit HTML directly

## 📁 Project Structure

```
├── src/                          # Source files
│   ├── data/
│   │   └── content.json         # 📝 EDIT THIS FILE for all content changes
│   ├── pug/
│   │   └── index.pug            # HTML template
│   ├── scss/                    # Styling files
│   └── assets/                  # Images and other assets
├── scripts/                     # Build scripts
├── dist/                        # Generated website (auto-generated)
├── index.html                   # Final website (auto-generated)
└── package.json                 # Project dependencies
```

## ✨ Quick Start

### 1. Install Dependencies
```bash
npm install
```

### 2. Build the Website
```bash
npm run build
```

### 3. Start Development Server
```bash
npm run start
```

## 📝 Editing Your Website Content

**Important**: To update your website content, you only need to edit `src/data/content.json`. This file contains all your personal information, research papers, teaching experience, and more.

### Example Content Updates

#### Personal Information
```json
{
  "personal": {
    "firstName": "Norman",
    "lastName": "Guo",
    "email": "norman.guo@slu.edu",
    "institution": "Saint Louis University"
  }
}
```

#### Adding a New Research Paper
```json
{
  "research": {
    "workingPapers": [
      {
        "title": "Your New Paper Title",
        "authors": [
          {
            "name": "Co-Author Name",
            "url": "https://co-author-website.com"
          }
        ],
        "paperUrl": "link-to-paper.pdf",
        "description": "Description of your research..."
      }
    ]
  }
}
```

#### Adding a New Course
```json
{
  "teaching": [
    {
      "course": "New Course Name",
      "institution": "Your Institution",
      "period": "2024 - Present",
      "description": "Course description..."
    }
  ]
}
```

## 🔧 Development Workflow

### For Content Changes:
1. Edit `src/data/content.json`
2. Run `npm run build`
3. Your changes will be reflected in `index.html`

### For Layout/Design Changes:
1. Edit `src/pug/index.pug` (template structure)
2. Edit `src/scss/` files (styling)
3. Run `npm run build`

### For Live Development:
1. Run `npm run start`
2. Make changes to any source files
3. Browser will automatically reload with changes

## 📋 Available Commands

- `npm run build` - Build the complete website
- `npm run start` - Build and start development server with live reload
- `npm run clean` - Clean the build directory
- `npm run build:pug` - Build only HTML from Pug templates
- `npm run build:scss` - Build only CSS from SCSS
- `npm run build:scripts` - Build only JavaScript
- `npm run build:assets` - Copy only assets

## 🎯 Content Management Guide

### Meta Information
Update SEO and tracking information:
- `meta.title` - Browser tab title
- `meta.description` - SEO description
- `meta.googleAnalyticsId` - Google Analytics tracking ID

### Navigation
Control which sections appear in your navigation:
```json
{
  "navigation": [
    { "id": "about", "label": "About" },
    { "id": "research", "label": "Research" }
  ]
}
```

### Social Links
Add or remove social media links:
```json
{
  "socialLinks": [
    {
      "platform": "github",
      "url": "https://github.com/yourusername",
      "icon": "fab fa-github"
    }
  ]
}
```

## 🚀 Deployment

After building with `npm run build`, the following files are ready for deployment:
- `index.html` - Main website file
- `css/` - Compiled stylesheets
- `js/` - JavaScript files
- `assets/` - Images and other assets

Simply upload these files to your web server or GitHub Pages.

## 🛠 Troubleshooting

### Build Errors
If you encounter build errors:
1. Check that `src/data/content.json` is valid JSON
2. Run `npm install` to ensure all dependencies are installed
3. Run `npm run clean` then `npm run build`

### Content Not Updating
1. Ensure you edited `src/data/content.json` (not `index.html` directly)
2. Run `npm run build` after making changes
3. Check the console for any JSON parsing errors

### Missing Dependencies
If you see "module not found" errors:
```bash
npm install
```

## 📞 Support

If you need help with this system, check:
1. The generated `dist/index.html` file to see the current output
2. Console messages when running build commands
3. Ensure all file paths in `content.json` are correct

---

**Remember**: Always edit `src/data/content.json` for content changes, never edit `index.html` directly as it will be overwritten on the next build!
