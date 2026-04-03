import FreeCADGui as Gui
import FreeCAD as App

class Unofficial2_Modeling_Workbench(Workbench):
    MenuText = "Unofficial 2.0 Modeling"
    ToolTip = "Unified Top-Down Modeling Environment"

    # A generic "U2" geometric logo in base64 XPM/SVG format.
    # Using a simple built-in or string icon to avoid missing file errors.
    Icon = """
            /* XPM */
            static const char * u2_icon[] = {
            "16 16 3 1",
            "  c None",
            ". c #000000",
            "+ c #0055FF",
            "                ",
            "  ............  ",
            "  .++++++++++.  ",
            "  .++......++.  ",
            "  .++.    .++.  ",
            "  .++.    .++.  ",
            "  .++.    .++.  ",
            "  .++.    .++.  ",
            "  .++.    .++.  ",
            "  .++.    .++.  ",
            "  .++......++.  ",
            "  .++++++++++.  ",
            "  ............  ",
            "                ",
            "                ",
            "                "};
            """

    def Initialize(self):
        # --- 1. Base Modeling (Home) ---
        self.appendToolbar("U2 Home / Solid Features", [
            "PartDesign_Body", "PartDesign_NewSketch",
            "Sketcher_EditSketch", "Sketcher_LeaveSketch",
            "PartDesign_Pad", "PartDesign_Pocket",
            "PartDesign_Revolution", "PartDesign_Groove",
            "PartDesign_Hole", "PartDesign_AdditiveLoft",
            "PartDesign_AdditivePipe"
        ])

        # --- 2. Detail & Editing ---
        self.appendToolbar("U2 Detail Features", [
            "PartDesign_Fillet", "PartDesign_Chamfer",
            "PartDesign_Draft", "PartDesign_Thickness",
            "PartDesign_Boolean", "PartDesign_Mirrored",
            "PartDesign_LinearPattern", "PartDesign_PolarPattern",
            "PartDesign_MultiTransform"
        ])

        # --- 3. Advanced Surfacing & Curves ---
        self.appendToolbar("U2 Surface & Curve", [
            "Part_RuledSurface", "Part_Loft", "Part_Sweep",
            "Part_Offset", "Part_Thickness", "Part_Extrude",
            "Part_Revolve", "Part_Fillet", "Part_JoinConnect",
            "Part_MakeFace", "Draft_BSpline", "Draft_Bezier"
        ])

        # --- 4. Assembly & Top-Down ---
        # Mimics WAVE Linker concept via SubShapeBinder and Link tools
        self.appendToolbar("U2 Assembly & Inter-Part", [
            "Assembly_CreateAssembly", "Assembly_InsertLink",
            "Assembly_CreateJointFixed", "Assembly_CreateJointRevolute",
            "Assembly_CreateJointCylindrical", "Assembly_CreateJointSlider",
            "Assembly_SolveSystem", "PartDesign_SubShapeBinder",
            "PartDesign_Clone", "Std_LinkMake", "Std_LinkMakeRelative"
        ])

        # --- 5. Drafting / TechDraw ---
        self.appendToolbar("U2 Drafting", [
            "TechDraw_PageDefault", "TechDraw_PageTemplate",
            "TechDraw_View", "TechDraw_ProjectionGroup",
            "TechDraw_LengthDimension", "TechDraw_RadiusDimension",
            "TechDraw_ExportPageSVG"
        ])

        # --- 6. Analysis & Measurement ---
        self.appendToolbar("U2 Analysis", [
            "Measure_Linear", "Measure_Angle",
            "Inspection_VisualInspection", "Part_CheckGeometry"
        ])

        # --- 7. Standard Views & Display ---
        self.appendToolbar("U2 Display & Views", [
            "Std_ViewFitAll", "Std_ViewIsometric",
            "Std_ViewFront", "Std_ViewTop", "Std_ViewRight",
            "Std_DrawStyle", "Std_PerspectiveCamera", "Std_OrthographicCamera"
        ])

        # Group commands into contextual menus
        self.appendMenu(["Unofficial 2.0", "Home"], ["PartDesign_Body", "PartDesign_NewSketch", "PartDesign_Pad", "PartDesign_Pocket"])
        self.appendMenu(["Unofficial 2.0", "Assemblies"], ["Assembly_CreateAssembly", "Assembly_InsertLink", "Assembly_SolveSystem"])
        self.appendMenu(["Unofficial 2.0", "Surfaces"], ["Part_RuledSurface", "Part_Loft", "Part_Sweep"])
        self.appendMenu(["Unofficial 2.0", "Drafting"], ["TechDraw_PageDefault", "TechDraw_View", "TechDraw_LengthDimension"])

    def Activated(self):
        # Enforce strict single-document tree behavior similar to high-end CAD Part Navigators
        try:
            Gui.runCommand('Std_TreeSingleDocument')
        except Exception:
            pass

        # Clear lingering selections for a clean start
        Gui.Selection.clearSelection()

        # Switch to Model / Task tab explicitly if the UI architecture supports it
        if hasattr(Gui, "getMainWindow"):
            try:
                mw = Gui.getMainWindow()
                dock_widgets = mw.findChildren(Gui.PyQt4.QtGui.QDockWidget) if hasattr(Gui, "PyQt4") else mw.findChildren(Gui.PySide.QtGui.QDockWidget) if hasattr(Gui, "PySide") else mw.findChildren(App.gui.QDockWidget) if hasattr(App, "gui") else []
                for dw in dock_widgets:
                    if "Tree" in dw.objectName() or "Task" in dw.objectName():
                        dw.raise_()
            except Exception:
                pass # Gracefully degrade if UI bindings differ

    def Deactivated(self):
        # Optional: cleanup or reset view state if switching away from unified mode
        pass

# Register the massively upgraded workbench
Gui.addWorkbench(Unofficial2_Modeling_Workbench())
