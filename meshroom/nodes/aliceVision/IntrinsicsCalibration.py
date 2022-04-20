__version__ = '2.0'

from meshroom.core import desc


class IntrinsicsCalibration(desc.CommandLineNode):
    commandLine = 'aliceVision_intrinsicsCalibration {allParams}'
    size = desc.DynamicNodeSize('input')
    category = 'Other'
    documentation = '''
    Calibration of a camera intrinsics using checkerboards
'''

    inputs = [
        desc.File(
            name='input',
            label='SfmData',
            description='SfmData File',
            value='',
            uid=[0],
        ),
        desc.File(
            name='checkerboards',
            label='Checkerboards folder',
            description='Folder for checkerboards json files',
            value='',
            uid=[0],
        ),
        desc.FloatParam(name="squareSize", label="Square size", description="Square size of checkerboard (mm)", value=0.1, uid=[0], range=(0, 1, 0.01)),
        desc.ChoiceParam(
            name='verboseLevel',
            label='Verbose Level',
            description='Verbosity level (fatal, error, warning, info, debug, trace).',
            value='info',
            values=['fatal', 'error', 'warning', 'info', 'debug', 'trace'],
            exclusive=True,
            uid=[],
        ),
    ]

    outputs = [
        desc.File(
            name='outSfMData',
            label='Output SfmData File',
            description='Path to the output sfmData file',
            value=desc.Node.internalFolder + 'sfmData.sfm',
            uid=[],
        )
    ]
