# MkDocs Implementation Roadmap

## Quick Start (Immediate Changes)

### 1. Hide Date Navigation (5 minutes)
Add the following to your existing `/docs/styles/custom.css`:

```css
/* Hide date-based navigation */
.md-nav__item--nested > .md-nav > .md-nav__item:has(.md-nav__link[href*="/2024/"]),
.md-nav__item--nested > .md-nav > .md-nav__item:has(.md-nav__link[href*="/2025/"]) {
    display: none !important;
}
```

### 2. Control Navigation with .pages Files (10 minutes)
The `.pages` files have been created in:
- `/docs/.pages` - Controls top-level navigation
- `/docs/research/.pages` - Controls research section navigation

These will override the automatic date-based navigation.

### 3. Update Homepage (15 minutes)
Replace the current `/docs/index.md` with a more dynamic version focusing on:
- Recent highlights (last 3-5 articles)
- Research areas with article counts
- Quick navigation by audience type

## Phase 1: Core Structure (Week 1)

### Day 1-2: Navigation Enhancement
- [ ] Test `.pages` files are working correctly
- [ ] Verify date navigation is hidden
- [ ] Update `mkdocs.yml` with new theme features
- [ ] Add navigation.tabs for better top-level organization

### Day 3-4: Category Pages
- [ ] Add overview sections to each research category page
- [ ] Include statistics (article count, last updated)
- [ ] Add "Featured Articles" sections
- [ ] Create cross-category links

### Day 5-7: Homepage Redesign
- [ ] Create new homepage layout with statistics
- [ ] Add "This Week's Highlights" section
- [ ] Implement quick navigation by interest
- [ ] Test responsive design

## Phase 2: Enhanced Features (Week 2)

### New Plugins Installation
```bash
pip install mkdocs-rss-plugin
pip install mkdocs-tags-plugin
pip install mkdocs-git-revision-date-localized-plugin
pip install mkdocs-minify-plugin
```

### Tag Implementation
- [ ] Add tags to article front matter
- [ ] Create `/docs/tags.md` index page
- [ ] Test tag filtering and navigation

### RSS Feed
- [ ] Configure RSS plugin for latest articles
- [ ] Add RSS link to homepage
- [ ] Test feed generation

## Phase 3: Advanced Customization (Week 3+)

### Custom Templates
- [ ] Create custom homepage template if needed
- [ ] Design project showcase template
- [ ] Implement dynamic content loading

### Search Enhancement
- [ ] Configure search to prioritize titles and tags
- [ ] Add search suggestions
- [ ] Create custom search page if needed

### Analytics and Monitoring
- [ ] Add Google Analytics
- [ ] Set up page view tracking
- [ ] Monitor navigation patterns

## Testing Checklist

- [ ] Navigation works without date folders visible
- [ ] All research categories are accessible
- [ ] Homepage loads quickly with dynamic content
- [ ] Mobile navigation is smooth
- [ ] Search returns relevant results
- [ ] RSS feed generates correctly
- [ ] Tags link between related content

## Rollback Plan

If issues arise:
1. Keep original `mkdocs.yml` as backup
2. Remove `.pages` files to restore automatic navigation
3. Remove hide-dates.css to show date navigation again

## Notes

- The awesome-pages plugin respects `.pages` files over automatic scanning
- CSS hiding is a quick fix; .pages files provide proper control
- Start with minimal changes and add features incrementally
- Monitor site build times as plugins are added