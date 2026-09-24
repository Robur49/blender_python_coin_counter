# Blender Coin Counter Tool 🪙

A custom Python tool developed within Blender to automate asset counting for an original 3D platformer environment I modeled from scratch. Created as a technical art portfolio piece, this project demonstrates custom tool creation using Blender's Python API (`bpy`) to streamline level design workflows.

![Tool Showcase](link-to-your-gif-or-screenshot-here.gif)
> [Note for myself: Record a quick 5-second GIF or take a screenshot of yourself clicking the button in Blender and the count showing up. Upload it to your repo and link it above.]

## 🛠️ Features

* Custom UI Panel: Integrates seamlessly into Blender's 3D Viewport side panel (N-Panel).
* Automated Asset Tracking: Instantly iterates through the scene data to tally specific game assets (coins) based on naming conventions.
* Non-Destructive: Runs purely as a reporting tool without altering scene geometry or object data.

## 🚀 How to Run
1. Download the repository and open `Coin_Counter_Proj.blend` in Blender.
2. Open the Scripting workspace, load `coin_counter.py`, and click **Run Script**.
3. In the 3D Viewport, press `N` to open the side panel, find the "Count Coins" tab, and click the button!

## 📂 Repository Structure

```text
blender_python_coin_counter
├── README.md                 # Project documentation
├── coin_counter.py       # The standalone Python script (Main Tool)
└── Coin_Counter_Proj.blend # The 3D test environment and assets
```

## 📄 References

* Blender Python API: https://docs.blender.org/api/current/info_quickstart.html#accessing-collections
* Darkfall. (2020, December 3). Blender Python Tutorial : How to Display Info Messages [learn python for beginners]
  [Video]. YouTube. Retrieved September 22, 2026, from https://www.youtube.com/watch?v=TgQ9ahMuDMw&list=PLFtLHTf5bnym_wk4DcYIMq1DkjqB7kDb-&index=24
