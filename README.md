# Coding Contest Template

Build a Codeforces-style contest webpage using Jinja.

### Usage

Define the problems in `build.py`. MathJax is supported.

Build the HTML file:

```
python build.py
```

Set the contest end time in `script.js`:

```
const endTime = new Date("2025-04-01T00:00:00Z").getTime();
```

Deploy as a static webpage from the `/build` directory.