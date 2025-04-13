/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/templates/**/*.html", // Scan all HTML files in templates
    "./app/**/*.py" // Scan Python files in app directory (for potential dynamic classes)
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
