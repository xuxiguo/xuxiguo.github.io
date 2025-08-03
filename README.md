# Norman Guo - Personal Website

This is a clean, organized personal website built with a modern development workflow.

## 🚀 **Quick Start - Edit Your Content**

**📝 EDIT THIS FILE:** [`development/src/data/content.json`](development/src/data/content.json)

Or double-click: [`edit-content.bat`](edit-content.bat) to open it directly!

## 🗂️ Project Structure (REORGANIZED!)

```
📁 root/                          # GitHub Pages files (CLEAN!)
├── index.html                    # Main website file
├── assets/                       # Images, PDFs, and media
├── css/                          # Compiled stylesheets  
├── js/                           # Compiled JavaScript
├── 📝 EDIT-CONTENT.md            # Quick link to content file
├── 📝 edit-content.bat           # Double-click to edit content
│
📁 development/                   # Development files (ORGANIZED!)
├── src/
│   ├── data/content.json         # ✨ EDIT THIS FILE FOR CONTENT
│   ├── pug/                      # HTML templates
│   └── scss/                     # CSS source
├── scripts/                      # Build scripts
└── node_modules/                 # Development dependencies
```

## 🚀 Quick Start

### Edit Your Content
**Option 1:** Click [`development/src/data/content.json`](development/src/data/content.json)
**Option 2:** Double-click [`edit-content.bat`](edit-content.bat)
**Option 3:** Open [`EDIT-CONTENT.md`](EDIT-CONTENT.md)

### Build & Preview
```bash
npm run build    # Builds the website
npm run dev      # Development server with live reload
```

### Deploy to GitHub Pages
```bash
npm run deploy   # Builds and prepares for GitHub Pages
```

## 📝 Content Management

**Easy Content Updates:** Just edit `development/src/data/content.json`

- ✅ Personal information
- ✅ Research papers
- ✅ Teaching experience  
- ✅ Social links
- ✅ Blockchain demos

After editing, run `npm run build` to update your website.

## 🎯 Benefits of This Structure

✅ **Clean Root Directory** - Only essential files for GitHub Pages  
✅ **Organized Development** - All build tools in `development/`  
✅ **Easy Content Access** - Multiple ways to find and edit content  
✅ **Professional Organization** - Clear separation of concerns  
✅ **GitHub Pages Ready** - Optimized for automatic deployment

## 📚 Common Commands

- `npm run build` - Build the website
- `npm run dev` - Development with live reload  
- `npm run validate` - Check content file validity
- `npm run deploy` - Build and prepare for deployment

## 🔧 Development

The development workflow is clean and simple:

1. **Edit content**: Use any of the quick access methods above
2. **Build**: Run `npm run build` 
3. **Deploy**: Commit and push to GitHub

Your GitHub Pages site will automatically update!