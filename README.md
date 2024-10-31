<a text-align="center" href="https://github.com/theasynch/YDSE_Sim/releases/tag/v1.0">Download Available Now</a>


---

# 🌌 Young's Double-Slit Experiment Simulator

A real-time simulation of the classic Young's Double-Slit Experiment, visualizing the wave interference pattern with customizable parameters for wavelength, slit separation, and screen distance.

---

## 🌠 What is the Young's Double-Slit Experiment?

The **Young's Double-Slit Experiment (YDSE)** is a fundamental experiment in physics that demonstrates the **wave nature of light**. When light passes through two closely spaced slits, it creates an interference pattern of alternating bright and dark bands on a screen due to **constructive and destructive interference** of the waves. This experiment provides evidence for the dual nature of light, acting both as particles and waves.

---

## 🖥️ About the Simulator

This Python-based GUI application simulates the YDSE setup and visualizes the interference pattern as you adjust parameters in real-time:
- **Wavelength**: Change the light's wavelength to observe color changes in the interference.
- **Slit Separation**: Adjust the spacing between slits to modify the fringe width.
- **Screen Distance**: Vary the distance from the slits to the screen to explore how the pattern spreads out.

The app generates a continuous intensity graph, illustrating how the interference pattern would appear on a screen in real life.

---

## ⚙️ How the Code Works

1. **GUI Creation**: Uses `PyQt5` for an interactive interface, complete with sliders for each parameter.
2. **Plotting**: Employs `matplotlib` to display a live graph of the interference pattern, with customizable graph styles for a unique aesthetic.
3. **Simulation**: Based on the YDSE formula, the code calculates intensity at various screen points using the selected parameters to dynamically update the graph.

Each change in slider values triggers a recalculation, providing a **real-time view** of how each factor affects the interference pattern.

---

## 🚀 How to Use the Code

### Requirements
1. Python 3.6+
2. Libraries: `PyQt5`, `numpy`, `matplotlib`

You can install the dependencies with:
```bash
pip install PyQt5 numpy matplotlib
```

### Steps
1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/yourusername/YDSE-Simulator.git
   ```
2. **Navigate to the Project Folder**:
   ```bash
   cd YDSE-Simulator
   ```
3. **Run the Simulation**:
   ```bash
   python ydse_simulator.py
   ```
4. **Interact with the GUI**:
   - Adjust **Wavelength** (in nm), **Slit Separation** (in mm), and **Screen Distance** (in cm) using the sliders.
   - Observe real-time changes in the interference pattern graph.

---

## ✨ Closing Notes

Thank you for checking out this YDSE Simulator! This project is continuously evolving, and contributions are more than welcome. Feel free to submit suggestions, open issues, or even make a **pull request**. Whether you’re a student or a seasoned physicist, your insights will help enhance this tool.

---

> **Let's make physics accessible and visual for everyone!**

---
