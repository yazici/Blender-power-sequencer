import bpy

from .utils.doc import doc_name, doc_idname, doc_brief, doc_description


class DeselectHandlesAndGrab(bpy.types.Operator):
    """
    Deselect the handles of all selected strips and call the Sequence Slide operator
    """
    doc = {
        'name': doc_name(__qualname__),
        'demo': '',
        'description': doc_description(__doc__),
        'shortcuts': [],
        'keymap': 'Sequencer'
    }
    bl_idname = doc_idname(doc['name'])
    bl_label = doc['name']
    bl_description = doc_brief(doc['description'])
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        for s in context.selected_sequences:
            s.select_left_handle = False
            s.select_right_handle = False
            s.select = True

        bpy.ops.transform.seq_slide('INVOKE_DEFAULT')
        return {'FINISHED'}

