/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}"
  ],
  theme: {
    maxWidth: {
      "1/4": "25%",
      "1/3": "33.33%",
      "1/2": "50%",
      "2/3": "66.66%",
      "3/4": "75%",
      full: "100%",
    },
    extend: {
      colors: {
        "ups-yellow": "#FFC400",
        "ups-grey": "#F2F1EF",
        "ups-teal": "#0A8080",
      },
      fontFamily: {  
        'sans': ['Roboto', 'sans-serif'],
    },
  },
  plugins: [],
}

