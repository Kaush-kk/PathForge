---
name: Aetheric Intelligence
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#cbc3d7'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#958ea0'
  outline-variant: '#494454'
  surface-tint: '#d0bcff'
  primary: '#d0bcff'
  on-primary: '#3c0091'
  primary-container: '#a078ff'
  on-primary-container: '#340080'
  inverse-primary: '#6d3bd7'
  secondary: '#4cd7f6'
  on-secondary: '#003640'
  secondary-container: '#03b5d3'
  on-secondary-container: '#00424e'
  tertiary: '#c4c1fb'
  on-tertiary: '#2d2a5b'
  tertiary-container: '#8e8bc2'
  on-tertiary-container: '#262354'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e9ddff'
  primary-fixed-dim: '#d0bcff'
  on-primary-fixed: '#23005c'
  on-primary-fixed-variant: '#5516be'
  secondary-fixed: '#acedff'
  secondary-fixed-dim: '#4cd7f6'
  on-secondary-fixed: '#001f26'
  on-secondary-fixed-variant: '#004e5c'
  tertiary-fixed: '#e3dfff'
  tertiary-fixed-dim: '#c4c1fb'
  on-tertiary-fixed: '#181445'
  on-tertiary-fixed-variant: '#444173'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  stats-number:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin-desktop: 80px
  margin-mobile: 20px
  container-max-width: 1280px
---

## Brand & Style

The design system for PathForge is built on a narrative of "Computational Guidance"—the intersection of deep mathematical rigor and fluid, AI-driven exploration. It is designed for ambitious professionals and students navigating the complexities of career evolution. 

The visual style is a fusion of **Glassmorphism** and **Corporate Modernism**. It leverages the depth of a dark-mode-first environment where surfaces appear to float over an infinite digital void. The aesthetic is futuristic yet disciplined, using light as a functional tool to highlight paths and decision nodes. The emotional response is one of clarity, high-tech reliability, and visionary potential.

## Colors

The palette is anchored in a "Deep Space" black (`#0A0A0A`), providing a high-contrast foundation for luminous accents. 

- **Primary Purple:** A vibrant, electric violet used for primary actions, success states, and the core brand identity.
- **Secondary Cyan:** A technical, cooling blue used for data visualization, secondary interactive elements, and AI-driven suggestions.
- **Tertiary Indigo:** A deep, structural color used for container backgrounds and subtle depth layers.
- **Functional Gradients:** Used sparingly for progress bars and top-tier "Hero" interactions to simulate energy flow and movement.

## Typography

This design system uses a tri-font hierarchy to balance technical precision with readability. 

1. **Space Grotesk (Headlines):** Its geometric, futuristic skeleton is used for impactful titles and key statistics, echoing the AI-driven theme.
2. **Hanken Grotesk (Body):** A clean, modern sans-serif that ensures long-form content is accessible and professional.
3. **JetBrains Mono (Labels/System):** A monospaced font used for metadata, micro-copy, and technical labels, reinforcing the "Forge" aspect of the brand—where paths are engineered and calculated.

## Layout & Spacing

The system utilizes a **12-column fluid grid** for desktop and a **4-column grid** for mobile. 

- **The Rhythm:** Based on a 4px baseline unit. All padding and margins should be multiples of 4 (e.g., 8, 16, 24, 32, 48, 64).
- **Depth Hierarchy:** Spacing is used to create "islands" of information. High-density data areas use tighter 16px internal padding, while hero sections use expansive 80px+ vertical padding to evoke a sense of premium "breathing room."
- **Safe Zones:** Content is center-aligned within a max-width container to ensure legibility on ultra-wide monitors.

## Elevation & Depth

Visual hierarchy is achieved through **Tonal Layering** and **Glassmorphism** rather than traditional drop shadows.

- **Level 0 (Floor):** Pure black background (`#0A0A0A`).
- **Level 1 (Base Container):** Dark indigo (`#1E1B4B`) with a 40% opacity and a 20px backdrop blur. Borders are 1px solid with 10% white opacity.
- **Level 2 (Interactive/Floating):** Similar to Level 1 but with a subtle inner glow (1px top-border) using the primary purple at 30% opacity to suggest light hitting the edge.
- **The "Pulse":** For AI-active states, use a faint, diffused radial gradient behind the component to simulate a glow emanating from within the UI.

## Shapes

The shape language is "Calculated Softness." Elements are rounded enough to feel approachable and modern, but maintain a structured, engineering-led feel.

- **Standard Radius:** 0.5rem (8px) for buttons, inputs, and small cards.
- **Large Radius:** 1.5rem (24px) for main dashboard containers and sections.
- **Pill Shapes:** Reserved exclusively for status indicators (chips) and the primary search/command bar to distinguish them as high-level navigational tools.

## Components

### Buttons
- **Primary:** Gradient fill (Purple to Cyan), white text, 8px radius. On hover, the gradient shifts or brightness increases by 10%.
- **Secondary:** Ghost style. 1px Purple border, transparent background, becomes 10% Purple fill on hover.

### Input Fields
- Dark backgrounds with 1px borders. Focus state triggers a Cyan border glow and a subtle "scan-line" animation if the field is AI-powered.

### Cards
- Utilizes the Level 1 Elevation glass effect. Headers within cards should use the `label-caps` typography style in Cyan to differentiate categories.

### Progress & Paths
- Vertical and horizontal lines connecting "nodes" should be thin (1px) and use the Secondary Cyan color. Active paths should have a "flowing" animation effect.

### Chips
- Small, pill-shaped elements with a low-opacity fill of the primary color. Used for tags like "High Demand" or "AI Recommended."