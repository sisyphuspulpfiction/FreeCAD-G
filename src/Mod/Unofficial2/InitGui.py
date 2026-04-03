import FreeCADGui as Gui
import FreeCAD as App

class Unofficial2_Modeling_Workbench(Workbench):
    MenuText = "Unofficial 2.0 Modeling"
    ToolTip = "Unified Top-Down Modeling Environment (NX-style)"
    Icon = """"""

    def Initialize(self):
        # 1. Base Modeling (Home)
        self.appendToolbar("U2 Base Features", [
            "PartDesign_Body", "PartDesign_NewSketch",
            "PartDesign_Pad", "PartDesign_Pocket",
            "PartDesign_Revolution", "PartDesign_Groove",
            "PartDesign_Hole"
        ])

        # 2. Detail & Editing
        self.appendToolbar("U2 Detail Features", [
            "PartDesign_Fillet", "PartDesign_Chamfer",
            "PartDesign_Draft", "PartDesign_Thickness",
            "PartDesign_Boolean", "PartDesign_Mirrored",
            "PartDesign_LinearPattern", "PartDesign_PolarPattern"
        ])

        # 3. Advanced Surfacing & Curves
        self.appendToolbar("U2 Surface & Curve", [
            "Part_RuledSurface", "Part_Loft", "Part_Sweep",
            "Part_Offset", "Part_Thickness", "Part_Extrude",
            "Part_Revolve", "Part_Fillet"
        ])

        # 4. Assembly & Top-Down (Mimics WAVE Linker concept via Binder/Links)
        self.appendToolbar("U2 Assembly & Inter-Part", [
            "Assembly_CreateAssembly", "Assembly_InsertLink",
            "PartDesign_SubShapeBinder", "PartDesign_Clone",
            "Assembly_SolveSystem", "Std_LinkMake"
        ])

        # 5. Analysis & Measurement
        self.appendToolbar("U2 Analysis", [
            "Measure_Linear", "Measure_Angle",
            "Inspection_VisualInspection"
        ])

    def Activated(self):
        # Enforce strict single-document tree behavior similar to Part Navigator
        Gui.runCommand('Std_TreeSingleDocument')
        # Clear lingering selections for a clean start
        Gui.Selection.clearSelection()

        # Additional UX enforcement: switch to Task Panel by default if not already
        if hasattr(Gui, "getMainWindow"):
            mw = Gui.getMainWindow()
            # Attempt to bring Model/Tasks tabs to front, though specific implementation
            # depends on the user's layout, this is a standard FreeCAD UI reset approach.

    def Deactivated(self):
        pass

# Register the rebranded and upgraded workbench
Gui.addWorkbench(Unofficial2_Modeling_Workbench())
