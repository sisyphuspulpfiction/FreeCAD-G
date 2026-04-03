import FreeCADGui as Gui
import FreeCAD as App

class NX_Modeling_Workbench(Workbench):
    MenuText = "NX V2 Modeling"
    ToolTip = "Unified NX-style Modeling Environment"
    # You can add a base64 encoded icon string here later to give it an NX logo
    Icon = """"""

    def Initialize(self):
        # Consolidate standard NX tools into unified toolbars
        # Mimicking the Home tab in NX
        self.appendToolbar("NX Base Features", [
            "PartDesign_Body", "PartDesign_NewSketch",
            "PartDesign_Pad", "PartDesign_Pocket",
            "PartDesign_Revolution", "PartDesign_Groove"
        ])

        self.appendToolbar("NX Detail Features", [
            "PartDesign_Fillet", "PartDesign_Chamfer",
            "PartDesign_Draft", "PartDesign_Thickness"
        ])

        self.appendToolbar("NX Surface & Curve", [
            "Part_RuledSurface", "Part_Loft", "Part_Sweep",
            "Part_Offset"
        ])

        # Assuming you are using FreeCAD 0.21+ with the built-in assembly workbench
        self.appendToolbar("NX Assembly", [
            "Assembly_CreateAssembly", "Assembly_InsertLink",
            "Assembly_SolveSystem"
        ])

    def Activated(self):
        # Auto-switch tree view to behave like the NX Part Navigator
        # This forces the tree to show a single unified document hierarchy
        Gui.runCommand('Std_TreeSingleDocument')
        # Clear any lingering selections upon entering the workbench
        Gui.Selection.clearSelection()

    def Deactivated(self):
        pass

# Register the workbench with FreeCAD's GUI
Gui.addWorkbench(NX_Modeling_Workbench())
