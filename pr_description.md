# 🧹 [Code Health] Simplify Experience duration calculation

🎯 **What:**
Removed redundant `Date` object instantiations and date parsing logic in `src/components/sections/Experience.astro`.

💡 **Why:**
The original code parsed the `startDate` and `endDate` strings and instantiated multiple `Date` objects when extracting the year for display, and then again when computing the time difference. Consolidating this into a single check for `start` and `end` eliminates duplicate execution while keeping the logic strictly localized and clearer to read.

✅ **Verification:**
I verified the date math via a short javascript script reproducing the before-and-after logic. I also ran the `pnpm run build` task to ensure that Astro built successfully with no runtime errors. No visual regressions were found in Astro's rendering.

✨ **Result:**
Cleaner, less redundant code without altering behavior.
