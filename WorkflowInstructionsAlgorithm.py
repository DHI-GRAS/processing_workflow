from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import QgsProcessingAlgorithm
from processing.gui.AlgorithmDialog import AlgorithmDialog

# An empty GeoAlgorithm to be used as a dummy when wanting to
# display an purely instruction step in a workflow.


class WorkflowInstructionsAlgorithm(QgsProcessingAlgorithm):

    def __init__(self):
        QgsProcessingAlgorithm.__init__(self)
        self._name = "workflowinstructions"
        self._displayName = self.tr("Workflow instructions")
        self._group = self.tr("Workflow-only tools")
        self._groupId = "workflowtools"

    def initAlgorithm(self, config=None):
        pass

    def createInstance(self):
        return WorkflowInstructionsAlgorithm()

    def processAlgorithm(self, parameters, context, progress):
        pass

    def name(self):
        return self._name

    def displayName(self):
        return self._displayName

    def shortDescription(self):
        return self._name

    def group(self):
        return self._group

    def groupId(self):
        return self._groupId

    def flags(self):
        return super().flags() | (QgsProcessingAlgorithm.FlagNoThreading |
                                  QgsProcessingAlgorithm.FlagDisplayNameIsLiteral |
                                  QgsProcessingAlgorithm.FlagHideFromToolbox |
                                  QgsProcessingAlgorithm.FlagHideFromModeler)

    def helpUrl(self):
        return ""

    def svgIconPath(self):
        return ""

    def tr(self, string, context=''):
        if context == '':
            context = self.__class__.__name__
        return QCoreApplication.translate(context, string)
