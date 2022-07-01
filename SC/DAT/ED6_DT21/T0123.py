import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0123_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0123   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '爱娜'),
    TXT(0x02, '雪拉扎德'),
    TXT(0x03, '阿加特'),
    TXT(0x04, '奥利维尔'),
    TXT(0x05, '科洛丝'),
    TXT(0x06, '提妲'),
    TXT(0x07, '金'),
    TXT(0x08, '克劳斯市长'),
    TXT(0x09, '里农'),
    TXT(0x0A, '布露姆老奶奶'),
    TXT(0x0B, '基蒂'),
    TXT(0x0C, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0123.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT21/T0123._SN', 'ED6_DT21/T0123_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x365B
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH02560._CH', 'ED6_DT07/CH02560P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT07/CH00053._CH', 'ED6_DT07/CH00053P._CP'),
        ('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP'),
        ('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP'),
        ('ED6_DT07/CH02350._CH', 'ED6_DT07/CH02350P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01010._CH', 'ED6_DT07/CH01010P._CP'),
        ('ED6_DT07/CH01770._CH', 'ED6_DT07/CH01770P._CP'),
    ]

# id: 0x10002 offset: 0x122
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 750,
            z                   = 0,
            y                   = 118600,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 3800,
            z                   = 0,
            y                   = 2000,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 47500,
            z                   = 0,
            y                   = -1110,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 46300,
            z                   = 0,
            y                   = -1110,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
    )

# id: 0x10003 offset: 0x282
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x282
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x282
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 1271,
            triggerZ            = 0,
            triggerY            = 116402,
            triggerRange        = 800,
            actorX              = 750,
            actorZ              = 1500,
            actorY              = 118600,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3810,
            triggerZ            = 0,
            triggerY            = 1080,
            triggerRange        = 800,
            actorX              = 3800,
            actorZ              = 1500,
            actorY              = 2000,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4900,
            triggerZ            = 0,
            triggerY            = 112600,
            triggerRange        = 1400,
            actorX              = 4900,
            actorZ              = 2000,
            actorY              = 112600,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2EE
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x2EF
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x6A),
            Expr.Equ,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x68),
            Expr.Equ,
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3D5',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_335',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0004)
    SetChrChipByIndex(0x000A, 8)
    SetChrPos(0x000A, -790, 200, 69820, 360)

    def _loc_335(): pass

    label('loc_335')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_362',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000B, 0x0004)
    SetChrChipByIndex(0x000B, 9)
    SetChrPos(0x000B, 1060, 200, 69820, 360)

    def _loc_362(): pass

    label('loc_362')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_385',
    )

    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, -1940, 0, 74490, 360)

    def _loc_385(): pass

    label('loc_385')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3A8',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -4290, 0, 73800, 360)

    def _loc_3A8(): pass

    label('loc_3A8')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3D5',
    )

    ClearChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000E, 0x0004)
    SetChrChipByIndex(0x000E, 10)
    SetChrPos(0x000E, 140, 200, 71510, 180)

    def _loc_3D5(): pass

    label('loc_3D5')

    Return()

# id: 0x0002 offset: 0x3D6
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3FB',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_53D')

    def _loc_3FB(): pass

    label('loc_3FB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_414',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_53D')

    def _loc_414(): pass

    label('loc_414')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_42D',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_53D')

    def _loc_42D(): pass

    label('loc_42D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_446',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_53D')

    def _loc_446(): pass

    label('loc_446')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_45F',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_53D')

    def _loc_45F(): pass

    label('loc_45F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_478',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_53D')

    def _loc_478(): pass

    label('loc_478')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_491',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_53D')

    def _loc_491(): pass

    label('loc_491')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4AA',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_53D')

    def _loc_4AA(): pass

    label('loc_4AA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C3',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_53D')

    def _loc_4C3(): pass

    label('loc_4C3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4DC',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_53D')

    def _loc_4DC(): pass

    label('loc_4DC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4F5',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_53D')

    def _loc_4F5(): pass

    label('loc_4F5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_50E',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_53D')

    def _loc_50E(): pass

    label('loc_50E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_527',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_53D')

    def _loc_527(): pass

    label('loc_527')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_53D',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_53D(): pass

    label('loc_53D')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_552',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_53D')

    def _loc_552(): pass

    label('loc_552')

    Return()

# id: 0x0003 offset: 0x553
@scena.Code('func_03_553')
def func_03_553():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 3, 0x1813)),
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 4, 0x1814)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 5, 0x1815)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 6, 0x1816)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 7, 0x1817)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_572',
    )

    Call(0, 0x000F)

    Jump('loc_67D')

    def _loc_572(): pass

    label('loc_572')

    TalkBegin(0x0008)
    Call(6, 0x0005)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_668',
    )

    OP_0D()
    Sleep(200)

    If(
        (
            (Expr.Eval, "OP_A9(0x03)"),
            Expr.Return,
        ),
        'loc_5F9',
    )

    ChrTalk(
        0x0008,
        (
            '#0350291505V#740F辛苦了。\n',
            '看来顺利达成目的了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291506V完成了什么任务的话\n',
            '再来报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_662')

    def _loc_5F9(): pass

    label('loc_5F9')

    ChrTalk(
        0x0008,
        (
            '#0350291507V#740F哎呀，现在\n',
            '好像没有可以报告的工作吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350291508V完成了什么任务的话\n',
            '再来报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_662(): pass

    label('loc_662')

    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_668(): pass

    label('loc_668')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_679',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_679(): pass

    label('loc_679')

    Call(0, 0x0005)

    def _loc_67D(): pass

    label('loc_67D')

    Return()

# id: 0x0004 offset: 0x67E
@scena.Code('func_04_67E')
def func_04_67E():
    Call(0, 0x0006)

    Return()

# id: 0x0005 offset: 0x683
@scena.Code('func_05_683')
def func_05_683():
    TalkBegin(0x0008)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_879',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            (Expr.PushVar, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6F6',
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '报告\n'),
            TXT(0x02, '呼叫同伴\n'),
            TXT(0x03, '离开\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    FadeIn(300, 0)

    Jump('loc_6FA')

    def _loc_6F6(): pass

    label('loc_6F6')

    Call(6, 0x0005)

    def _loc_6FA(): pass

    label('loc_6FA')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_868',
    )

    OP_0D()
    Sleep(200)

    If(
        (
            (Expr.Eval, "OP_29(0x00C0, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x00C0, 0x00, 0x20)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_78C',
    )

    OP_28(0x00C3, 0x04, 0x20)
    OP_A9(0x03)

    ChrTalk(
        0x0008,
        (
            '#0350281442V#740F辛苦了。\n',
            '看来顺利达成目的了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350281443V完成了什么任务的话\n',
            '再来报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_862')

    def _loc_78C(): pass

    label('loc_78C')

    If(
        (
            (Expr.Eval, "OP_A9(0x03)"),
            Expr.Return,
        ),
        'loc_7F9',
    )

    ChrTalk(
        0x0008,
        (
            '#0350281444V#740F辛苦了。\n',
            '看来顺利达成目的了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350281445V完成了什么任务的话\n',
            '再来报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_862')

    def _loc_7F9(): pass

    label('loc_7F9')

    ChrTalk(
        0x0008,
        (
            '#0350281446V#740F哎呀，现在\n',
            '好像没有可以报告的工作吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350281447V完成了什么任务的话\n',
            '再来报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_862(): pass

    label('loc_862')

    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_868(): pass

    label('loc_868')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_879',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_879(): pass

    label('loc_879')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 3, 0x1813)),
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 4, 0x1814)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 5, 0x1815)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 6, 0x1816)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 7, 0x1817)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_898',
    )

    Call(0, 0x000F)

    Jump('loc_99C')

    def _loc_898(): pass

    label('loc_898')

    OP_A2(0x1884)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_902',
    )

    ChrTalk(
        0x0008,
        (
            '#0350281448V#740F那么，昏睡事件的调查\n',
            '麻烦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350281449V请你们\n',
            '小心谨慎的进行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_999')

    def _loc_902(): pass

    label('loc_902')

    ChrTalk(
        0x0008,
        (
            '#0350281450V#740F听说你们在克劳斯市长的\n',
            '委托下开始调查昏睡事件了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350281451V我们已经正式\n',
            '受到委托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350281452V那么调查就\n',
            '麻烦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_999(): pass

    label('loc_999')

    TalkEnd(0x0008)

    def _loc_99C(): pass

    label('loc_99C')

    Return()

# id: 0x0006 offset: 0x99D
@scena.Code('func_06_99D')
def func_06_99D():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 5, 0x1885)),
            Expr.Return,
        ),
        'loc_9CF',
    )

    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9BE',
    )

    OP_A9(0x02)
    TalkEnd(0x0010)

    Return()

    def _loc_9BE(): pass

    label('loc_9BE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9CF',
    )

    TalkEnd(0x0010)

    Return()

    def _loc_9CF(): pass

    label('loc_9CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_E1F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 5, 0x1885)),
            Expr.Return,
        ),
        'loc_BFB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B8F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_A76',
    )

    ChrTalk(
        0x0010,
        (
            '我老妈带回来的那位小姐，\n',
            '说要在店里帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '这、这一定是……\n',
            '为了让我结婚设计的阴谋啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '啊，真郁闷……\n',
            '我该怎么拒绝呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B8C')

    def _loc_A76(): pass

    label('loc_A76')

    ChrTalk(
        0x0010,
        (
            '哟，这么晚，辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '游击士真不容易啊，\n',
            '现在对我个人来说是个大危机……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '我老妈带回来的那个小姐，\n',
            '说要在店里帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '本来这是一件好事，\n',
            '不过一和我老妈扯上关系……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '这、这一定是……\n',
            '这是为了让我结婚设计的阴谋啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '啊，真郁闷……\n',
            '可我还不想结婚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0001)

    def _loc_B8C(): pass

    label('loc_B8C')

    Jump('loc_BF8')

    def _loc_B8F(): pass

    label('loc_B8F')

    ChrTalk(
        0x0010,
        (
            '如果装备不足的话，\n',
            '请随时过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '今晚还没\n',
            '那么快打烊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '那么，艾丝蒂尔你们\n',
            '工作也要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_BF8(): pass

    label('loc_BF8')

    Jump('loc_E1F')

    def _loc_BFB(): pass

    label('loc_BFB')

    OP_62(0x0010, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrTurnDirection(0x0010, 0x0101, 0)
    Sleep(400)

    ChrTalk(
        0x0010,
        (
            '哦！\n',
            '艾丝蒂尔，终于来了啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1008F里农先生……\n',
            '嘿嘿，好久不见。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这么晚才来跟你打招呼，真对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '哪里哪里，没关系啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '不过你回来的\n',
            '可真不是时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '莫非你们现在\n',
            '还在巡逻什么的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F啊，嗯……\n',
            '算是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F嗯，为了以防万一，\n',
            '协会也提高了警惕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0103, 400)

    ChrTalk(
        0x0010,
        (
            '呼，真不容易。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '不过这样一来\n',
            '就给我们这些居民壮胆了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '如果装备不足的话\n',
            '请随时过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '今晚还没\n',
            '那么快打烊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#525F谢谢，真是太好了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F嗯……\n',
            '那么，里农先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '嗯，你们加油工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1885)
    OP_A2(0x0002)

    def _loc_E1F(): pass

    label('loc_E1F')

    TalkEnd(0x0010)

    Return()

# id: 0x0007 offset: 0xE23
@scena.Code('func_07_E23')
def func_07_E23():
    TalkBegin(0x0011)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_F5D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_E8F',
    )

    ChrTalk(
        0x00FE,
        (
            '基蒂小姐从明天起\n',
            '要在店里帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '里农的表情虽然很复杂，\n',
            '不过我可没说过什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F5D')

    def _loc_E8F(): pass

    label('loc_E8F')

    ChrTalk(
        0x00FE,
        (
            '这是基蒂小姐自己\n',
            '强烈要求的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她从明天起就要在我家的\n',
            '店里帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是我家的里农\n',
            '表情却很复杂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他好像以为\n',
            '这是我安排的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可能因为我去给他找过新娘，\n',
            '那孩子的警惕性一下子升高了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    def _loc_F5D(): pass

    label('loc_F5D')

    TalkEnd(0x0011)

    Return()

# id: 0x0008 offset: 0xF61
@scena.Code('func_08_F61')
def func_08_F61():
    TalkBegin(0x0012)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 2, 0x1812)),
            Expr.Return,
        ),
        'loc_1093',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_FCB',
    )

    ChrTalk(
        0x00FE,
        (
            '在我好说歹说下，\n',
            '终于能在这店里帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然受了别人的关照，\n',
            '就得有所回报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1093')

    def _loc_FCB(): pass

    label('loc_FCB')

    ChrTalk(
        0x00FE,
        (
            '在我不断拜托之下\n',
            '终于能在这店里帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '受了别人的关照，\n',
            '就得有所回报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不过老太太的儿子\n',
            '好象有点不高兴呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '像我这种不明来历的人，\n',
            '突然来到店里，\n',
            '果然还是令人比较在意吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0004)

    def _loc_1093(): pass

    label('loc_1093')

    TalkEnd(0x0012)

    Return()

# id: 0x0009 offset: 0x1097
@scena.Code('func_09_1097')
def func_09_1097():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x05,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000A)
    ClearChrFlags(0x000A, 0x0010)
    ChrTurnDirection(0x000A, 0x0000, 0)

    ExecExpressionWithValue(
        0x000A,
        0x04,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x04,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xA, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x05,
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xA, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1127',
    )

    Jump('loc_1169')

    def _loc_1127(): pass

    label('loc_1127')

    If(
        (
            (Expr.GetChrWork, 0xA, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1143',
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1169')

    def _loc_1143(): pass

    label('loc_1143')

    If(
        (
            (Expr.GetChrWork, 0xA, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_115F',
    )

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1169')

    def _loc_115F(): pass

    label('loc_115F')

    ExecExpressionWithValue(
        0x000A,
        0x08,
        (
            (Expr.GetChrWork, 0xA, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1169(): pass

    label('loc_1169')

    ExecExpressionWithValue(
        0x000A,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x000A, 0x0010)

    ChrTalk(
        0x000A,
        (
            '#0050290818V#050F哟，调查还顺利吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【队伍组成】\n'),
            TXT(0x01, '【放弃】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1214'),
        (0x00000001, 'loc_124D'),
        (-1, 'loc_12A7'),
    )

    def _loc_1214(): pass

    label('loc_1214')

    ChrTalk(
        0x000A,
        (
            '#0050271305V#051F哦，知道了。\n',
            '要调整队伍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x000E)

    Jump('loc_12A7')

    def _loc_124D(): pass

    label('loc_124D')

    ChrTalk(
        0x000A,
        (
            '#0050271306V#052F怎么，不调整了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050271307V#050F需要我的重剑时\n',
            '尽管开口吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12A7')

    def _loc_12A7(): pass

    label('loc_12A7')

    SetChrSubChip(0x000A, 0)
    TalkEnd(0x000A)

    Return()

# id: 0x000A offset: 0x12B0
@scena.Code('func_0A_12B0')
def func_0A_12B0():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000B)
    ClearChrFlags(0x000B, 0x0010)
    ChrTurnDirection(0x000B, 0x0000, 0)

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xB, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x05,
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xB, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1340',
    )

    Jump('loc_1382')

    def _loc_1340(): pass

    label('loc_1340')

    If(
        (
            (Expr.GetChrWork, 0xB, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_135C',
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1382')

    def _loc_135C(): pass

    label('loc_135C')

    If(
        (
            (Expr.GetChrWork, 0xB, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1378',
    )

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1382')

    def _loc_1378(): pass

    label('loc_1378')

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.GetChrWork, 0xB, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1382(): pass

    label('loc_1382')

    ExecExpressionWithValue(
        0x000B,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x000B, 0x0010)

    ChrTalk(
        0x000B,
        (
            '#0040291517V#034F真是的……\n',
            '真是个麻烦的夜晚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040291518V#030F如果你们希望的话，\n',
            '我来唱一曲给你们散散心如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【队伍组成】\n'),
            TXT(0x01, '【放弃】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_147A'),
        (0x00000001, 'loc_14D3'),
        (-1, 'loc_152E'),
    )

    def _loc_147A(): pass

    label('loc_147A')

    ChrTalk(
        0x000B,
        (
            '#0040240128V#030F呵，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040240129V看来是需要\n',
            '我这个天才的力量啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x000E)

    Jump('loc_152E')

    def _loc_14D3(): pass

    label('loc_14D3')

    ChrTalk(
        0x000B,
        (
            '#0040271287V#030F哎呀，不要我了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040291522V呵呵，那么我就在这里\n',
            '静候佳音了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_152E')

    def _loc_152E(): pass

    label('loc_152E')

    SetChrSubChip(0x000B, 0)
    TalkEnd(0x000B)

    Return()

# id: 0x000B offset: 0x1537
@scena.Code('func_0B_1537')
def func_0B_1537():
    TalkBegin(0x000C)

    ChrTalk(
        0x000C,
        (
            '#0060291523V#043F啊，各位……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060291524V有什么我\n',
            '可以帮忙的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【队伍组成】\n'),
            TXT(0x01, '【放弃】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_15DF'),
        (0x00000001, 'loc_1614'),
        (-1, 'loc_1667'),
    )

    def _loc_15DF(): pass

    label('loc_15DF')

    ChrTalk(
        0x000C,
        (
            '#0060291525V#042F明白了。\n',
            '要调整队伍吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x000E)

    Jump('loc_1667')

    def _loc_1614(): pass

    label('loc_1614')

    ChrTalk(
        0x000C,
        (
            '#0060291526V#049F外面雾很浓……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060291527V希望不要增添更多的\n',
            '受害者……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1667')

    def _loc_1667(): pass

    label('loc_1667')

    TalkEnd(0x000C)

    Return()

# id: 0x000C offset: 0x166B
@scena.Code('func_0C_166B')
def func_0C_166B():
    TalkBegin(0x000D)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16C4',
    )

    ChrTalk(
        0x000D,
        (
            '#0070271308V#560F啊，阿加特哥哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271309V那个，有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_175B')

    def _loc_16C4(): pass

    label('loc_16C4')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1710',
    )

    ChrTalk(
        0x0107,
        (
            '#0070271310V#060F啊、姐姐，是你们啊。\n',
            '怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_175B')

    def _loc_1710(): pass

    label('loc_1710')

    ChrTalk(
        0x0107,
        (
            '#0070271311V#060F啊、姐姐，是你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271309V那个，有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_175B(): pass

    label('loc_175B')

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【队伍组成】\n'),
            TXT(0x01, '【放弃】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_17B8'),
        (0x00000001, 'loc_183F'),
        (-1, 'loc_191C'),
    )

    def _loc_17B8(): pass

    label('loc_17B8')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1806',
    )

    ChrTalk(
        0x0107,
        (
            '#0070271313V#060F啊，嗯，明白了。\n',
            '要调整队伍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1838')

    def _loc_1806(): pass

    label('loc_1806')

    ChrTalk(
        0x0107,
        (
            '#0070271314V#560F啊，明白了。\n',
            '要调整队伍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1838(): pass

    label('loc_1838')

    Call(0, 0x000E)

    Jump('loc_191C')

    def _loc_183F(): pass

    label('loc_183F')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_18B8',
    )

    ChrTalk(
        0x0107,
        (
            '#0070271319V#064F咦，又不要了吗……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271320V#060F我就在这里等，\n',
            '有什么事就来找我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1919')

    def _loc_18B8(): pass

    label('loc_18B8')

    ChrTalk(
        0x0107,
        (
            '#0070271319V#064F咦，又不要了吗……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070271322V#060F我会在这里等的，\n',
            '随时都可以来找我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1919(): pass

    label('loc_1919')

    Jump('loc_191C')

    def _loc_191C(): pass

    label('loc_191C')

    TalkEnd(0x000D)

    Return()

# id: 0x000D offset: 0x1920
@scena.Code('func_0D_1920')
def func_0D_1920():
    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x05,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkBegin(0x000E)
    ClearChrFlags(0x000E, 0x0010)
    ChrTurnDirection(0x000E, 0x0000, 0)

    ExecExpressionWithValue(
        0x000E,
        0x04,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x04,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x168),
            Expr.Add,
            (Expr.GetChrWork, 0xE, 0x5),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x05,
        (
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x2D),
            Expr.Leq,
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x13B),
            Expr.Geq,
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x195),
            Expr.Leq,
            Expr.Nez64,
            Expr.Or,
            (Expr.GetChrWork, 0xE, 0x4),
            (Expr.PushLong, 0x2A3),
            Expr.Geq,
            Expr.Or,
            Expr.Return,
        ),
        'loc_19B0',
    )

    Jump('loc_19F2')

    def _loc_19B0(): pass

    label('loc_19B0')

    If(
        (
            (Expr.GetChrWork, 0xE, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_19CC',
    )

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_19F2')

    def _loc_19CC(): pass

    label('loc_19CC')

    If(
        (
            (Expr.GetChrWork, 0xE, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_19E8',
    )

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_19F2')

    def _loc_19E8(): pass

    label('loc_19E8')

    ExecExpressionWithValue(
        0x000E,
        0x08,
        (
            (Expr.GetChrWork, 0xE, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_19F2(): pass

    label('loc_19F2')

    ExecExpressionWithValue(
        0x000E,
        0x04,
        (
            (Expr.GetChrWork, 0x0, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0000,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x05,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x000E, 0x0010)

    ChrTalk(
        0x000E,
        (
            '#0080291555V#072F哟，状态怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【队伍组成】\n'),
            TXT(0x01, '【放弃】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1A9B'),
        (0x00000001, 'loc_1AC5'),
        (-1, 'loc_1B00'),
    )

    def _loc_1A9B(): pass

    label('loc_1A9B')

    ChrTalk(
        0x000E,
        (
            '#0080291556V#072F要更换队员？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(0, 0x000E)

    Jump('loc_1B00')

    def _loc_1AC5(): pass

    label('loc_1AC5')

    ChrTalk(
        0x000E,
        (
            '#0080291557V#072F我在这里等，\n',
            '需要的时候就说一声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B00')

    def _loc_1B00(): pass

    label('loc_1B00')

    SetChrSubChip(0x000E, 0)
    TalkEnd(0x000E)

    Return()

# id: 0x000E offset: 0x1B09
@scena.Code('func_0E_1B09')
def func_0E_1B09():
    OP_C9(
        0x01,
        (
            0x0000,
            0x0002,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0003,
            0x0004,
            0x0006,
            0x0007,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(1000)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1B74',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0004)
    SetChrChipByIndex(0x000A, 8)
    SetChrPos(0x000A, -790, 200, 69820, 360)

    def _loc_1B74(): pass

    label('loc_1B74')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1BA1',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000B, 0x0004)
    SetChrChipByIndex(0x000B, 9)
    SetChrPos(0x000B, 1060, 200, 69820, 360)

    def _loc_1BA1(): pass

    label('loc_1BA1')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1BC4',
    )

    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, -1940, 0, 74490, 360)

    def _loc_1BC4(): pass

    label('loc_1BC4')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1BE7',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -4290, 0, 73800, 360)

    def _loc_1BE7(): pass

    label('loc_1BE7')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1C14',
    )

    ClearChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000E, 0x0004)
    SetChrChipByIndex(0x000E, 10)
    SetChrPos(0x000E, 140, 200, 71510, 180)

    def _loc_1C14(): pass

    label('loc_1C14')

    OP_0D()

    Return()

# id: 0x000F offset: 0x1C16
@scena.Code('func_0F_1C16')
def func_0F_1C16():
    EventBegin(0x00)
    OP_4A(0x0008, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1C3A',
    )

    Call(0, 0x0012)
    FadeIn(0, 0)
    Call(0, 0x0013)

    def _loc_1C3A(): pass

    label('loc_1C3A')

    Fade(1000)
    OP_6D(370, 0, 117930, 0)
    OP_67(0, 6810, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 640, 0, 116600, 0)
    SetChrPos(0x0103, 1600, 0, 116600, 0)
    SetChrPos(0x00F8, 1800, 0, 115320, 0)
    SetChrPos(0x00F9, 840, 0, 115320, 0)
    OP_8C(0x0008, 180, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D74',
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◇从教会出来之后没跟爱娜说话】\n'),
            TXT(0x01, '【◇从教会出来之后已经跟爱娜说话】\n'),
            TXT(0x02, '【◇不变更】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1D68'),
        (0x00000001, 'loc_1D6E'),
        (-1, 'loc_1D74'),
    )

    def _loc_1D68(): pass

    label('loc_1D68')

    OP_A3(0x1884)

    Jump('loc_1D74')

    def _loc_1D6E(): pass

    label('loc_1D6E')

    OP_A2(0x1884)

    Jump('loc_1D74')

    def _loc_1D74(): pass

    label('loc_1D74')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0310, 4, 0x1884)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1DE9',
    )

    ChrTalk(
        0x0008,
        (
            '#0350290001V#742F听说你们在克劳斯市长的\n',
            '委托下开始调查昏睡事件了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350290002V怎么样？调查得如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E3A')

    def _loc_1DE9(): pass

    label('loc_1DE9')

    ChrTalk(
        0x0008,
        (
            '#0350290003V#742F事件的调查，辛苦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350290004V怎么样？调查得如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E3A(): pass

    label('loc_1E3A')

    ChrTalk(
        0x0101,
        (
            '#0010290005V#1025F#6P啊，嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290006V从昏睡者的家人那里\n',
            '大致了解过情况了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【继续调查】\n'),
            TXT(0x01, '【向爱娜报告】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F4D',
    )

    ChrTalk(
        0x0008,
        (
            '#0350290007V#742F明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350290008V等情况都了解完后\n',
            '就回协会了报告吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1884)
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Jump('loc_33D3')

    def _loc_1F4D(): pass

    label('loc_1F4D')

    ChrTalk(
        0x0008,
        (
            '#0350290007V#742F明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350290010V那么，把大家叫来\n',
            '对信息进行一遍整理吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(500)

    Call(0, 0x0010)
    OP_4A(0x0008, 255)
    OP_6D(140, 0, 117080, 0)
    OP_67(0, 6760, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 510, 0, 116600, 0)
    SetChrPos(0x0103, 1570, 0, 116600, 0)
    SetChrPos(0x0105, -230, 0, 115790, 0)
    SetChrPos(0x0104, 2320, 0, 115270, 0)
    SetChrPos(0x0107, 1070, 0, 115580, 0)
    SetChrPos(0x0108, 250, 0, 114280, 0)
    SetChrPos(0x0106, 1500, 0, 114310, 0)
    OP_8C(0x0008, 180, 0)
    OP_1D(0x73)
    Sleep(500)

    FadeIn(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0350290011V#744F……原来如此。\n',
            '你们调查到不少情况了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350290012V#742F尤其是昏睡者的\n',
            '相关人员对事件描述很有意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350290013V总之在所有的描述中\n',
            '有一个地方是完全相符的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290014V#1004F#6P啊，那是指……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName('')

    Talk(
        (
            0x18,
            (TxtCtl.SetColor, 0x5),
            '４份描述的共同点是？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【昏睡的时刻】\n'),
            TXT(0x01, '【是否有目击者】\n'),
            TXT(0x02, '【听见的声音】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_221F'),
        (0x00000001, 'loc_23BE'),
        (0x00000002, 'loc_245C'),
        (-1, 'loc_2593'),
    )

    def _loc_221F(): pass

    label('loc_221F')

    ChrTurnDirection(0x0103, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030290015V#524F不……\n',
            '这方面各自都有微妙的差别。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290016V玲达小姐是在５点前被\n',
            '在准备饭菜的夫人发现的，\n',
            '所以实际昏睡应该在４点半前后。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290017V另一方面，拉欧爷爷\n',
            '是在５点半左右昏睡的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010290018V#1015F#5P这样啊……\n',
            '有一个小时的差距啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290019V#026F４个人的案子共同拥有的特点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290020V#022F那就是昏睡时\n',
            '都没有目击者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290021V#1004F#5P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2593')

    def _loc_23BE(): pass

    label('loc_23BE')

    OP_2B(0x0090, 0x0003)
    ChrTurnDirection(0x0103, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030290022V#026F嗯，确实是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290023V#022F４个人的案子共同拥有的特点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290024V就是昏睡的瞬间\n',
            '都没有目击者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    Jump('loc_2593')

    def _loc_245C(): pass

    label('loc_245C')

    OP_2B(0x0090, 0x0001)
    ChrTurnDirection(0x0103, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030290025V#524F……铃声啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290026V确实很令人在意，\n',
            '不过在托露塔夫人和鲁克的案子里\n',
            '都没有提到铃声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010290027V#1015F#5P哦，对……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290019V#026F４个人的案子共同拥有的特点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290020V#022F那就是昏睡时\n',
            '都没有目击者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290030V#1004F#5P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2593')

    def _loc_2593(): pass

    label('loc_2593')

    ChrTalk(
        0x0106,
        (
            '#0050290031V#051F#6P哟，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050290032V就好像是算准时机\n',
            '一样地睡着了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0105, 90, 400)
    Sleep(500)

    ChrTalk(
        0x0105,
        (
            '#0060290033V#043F#5P如果是这样的话，\n',
            '这场雾的背后似乎就隐藏着什么了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060290034V视野这么差，\n',
            '目击者就会减少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040290035V#035F#6P悄悄地出现在雾中，\n',
            '会吞噬牺牲者灵魂的恶魔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290036V#030F这种妖艳的印象\n',
            '浮现在我的眼前。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070290037V#065F#6P啊啊啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290038V#1007F#5P唔，鸡皮疙瘩也起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350290039V#744F经你这么一说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350290040V#740F好像就有了能确定恶魔印象\n',
            '的有力描述了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290041V#026F嗯……\n',
            '『铃声』和『黑衣女人』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290042V#022F这些看来都和\n',
            '昏睡事件有关。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290043V#1015F#5P先不说铃声，\n',
            '看到黑衣女人的\n',
            '应该是伊莉莎吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290044V有没有是偶然的可能性呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290045V#027F不……这不可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290046V如果你仔细想想那个女人\n',
            '出现的地方发生了什么的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290047V#1004F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName('')

    Talk(
        (
            0x18,
            (TxtCtl.SetColor, 0x5),
            '在黑衣女人出现的地方发生了什么？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【托露塔昏睡了】\n'),
            TXT(0x01, '【拉欧爷爷昏睡了】\n'),
            TXT(0x02, '【鲁克昏睡了】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_29B7'),
        (0x00000001, 'loc_2A53'),
        (0x00000002, 'loc_2AE5'),
        (-1, 'loc_2B53'),
    )

    def _loc_29B7(): pass

    label('loc_29B7')

    ChrTalk(
        0x0103,
        (
            '#0030290048V#026F托露塔夫人是倒在\n',
            '酒馆二楼的阳台上的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290049V既然黑衣女子\n',
            '是出现在钟楼上的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290050V#022F帕特是在那里\n',
            '发现鲁克的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B53')

    def _loc_2A53(): pass

    label('loc_2A53')

    ChrTalk(
        0x0103,
        (
            '#0030290051V#026F拉欧爷爷是倒在\n',
            '自家门口的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290049V既然黑衣女子\n',
            '是出现在钟楼上的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290050V#022F帕特是在那里\n',
            '发现鲁克的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B53')

    def _loc_2AE5(): pass

    label('loc_2AE5')

    OP_2B(0x0090, 0x0003)

    ChrTalk(
        0x0103,
        (
            '#0030290054V#026F对，黑衣女子\n',
            '是出现在钟楼上的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290050V#022F帕特是在那里\n',
            '发现鲁克的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B53')

    def _loc_2B53(): pass

    label('loc_2B53')

    ChrTalk(
        0x0101,
        (
            '#0010290056V#1020F#5P确、确实……\n',
            '不可能是偶然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290057V那么那个\n',
            '黑衣女人果然……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080290058V#074F嗯，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080290059V#072F看来又有新的\n',
            '『执行者』出现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050290060V#057F#6P哼……果然是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060290061V#047F#5P原因不明的雾和昏睡\n',
            '是这次的『不可能的现象』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060290062V#042F那么铃声\n',
            '就是『暗示』了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0350290063V#744F现在总算能\n',
            '确定敌人的身份了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350290064V#742F我接下来要联络\n',
            '各地支部和王国军……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0350290065V你们有什么打算？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0103, 0, 400)

    @scena.Lambda('lambda_2D37')
    def lambda_2D37():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2D37)

    OP_8C(0x0101, 0, 400)

    ChrTalk(
        0x0103,
        (
            '#0030290066V#522F#6P是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290067V这样下去不知何时\n',
            '又会有其他市民遭到袭击。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290068V#022F我们应该彻夜巡逻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290069V#1006F#6P嗯，我也赞成。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290070V换班进行的话\n',
            '也能稍微得到一点休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(50)

    OP_62(0x0108, 0x00000000, 2300, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0106)
    Sleep(50)

    OP_63(0x0108)

    ChrTalk(
        0x0108,
        (
            '#0080290071V#070F啊，没这个必要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2E84')
    def lambda_2E84():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2E84)

    Sleep(50)

    @scena.Lambda('lambda_2E97')
    def lambda_2E97():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_2E97)

    Sleep(50)

    @scena.Lambda('lambda_2EAA')
    def lambda_2EAA():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2EAA)

    Sleep(50)

    @scena.Lambda('lambda_2EBD')
    def lambda_2EBD():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_2EBD)

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010290072V#1004F#5P啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050290073V#051F#6P晚上的巡逻就\n',
            '交给我们这些男人吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050290074V你们就一起\n',
            '在家好好休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290075V#1026F#5P但，但是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030290076V#524F是啊，艾丝蒂尔\n',
            '今天也累了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290077V你带公主还有\n',
            '提妲去家里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010191305V#1026F#5P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290079V#1007F……嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050290080V#555F#6P我说，雪拉扎德，\n',
            '你怎么说得事不关己一样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050290081V我都说了巡逻交给\n',
            '我们这些男人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x0103, 180, 400)

    @scena.Lambda('lambda_30C3')
    def lambda_30C3():
        OP_8C(0x0101, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_30C3)

    ChrTalk(
        0x0103,
        (
            '#0030290082V#023F#2P……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080290083V#070F你和艾丝蒂尔\n',
            '在调查上已经很努力了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080290084V也可以说是换班吧，\n',
            '今晚你们就好好休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290085V#024F#2P你、你等等……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290086V对Ｂ级游击士\n',
            '没必要有这方面的担心！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040290087V#030F#6P雪拉，\n',
            '这个你就听他的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290088V虽然你装出一副没事的样子，\n',
            '不过疲劳完全浮现在脸上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290089V#522F#2P……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040290090V#031F#6P在必要的时候休息，\n',
            '不也是游击士的工作吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290091V#522F#2P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290092V#025F……没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010200288V#1026F#5P雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290094V#524F#2P金先生、阿加特，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290095V夜间的巡逻……\n',
            '就麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080290096V#071F嗯，交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050290097V#051F#6P明天则需要你\n',
            '努力工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)
    OP_A2(0x10F2)
    NewScene('ED6_DT21/T0101._SN', 110, 0, 0)
    IdleLoop()

    def _loc_33D3(): pass

    label('loc_33D3')

    Return()

# id: 0x0010 offset: 0x33D4
@scena.Code('func_10_33D4')
def func_10_33D4():
    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_340D',
    )

    FormationAddMember(ChrTable['奥利维尔'], 0xFA, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_340D(): pass

    label('loc_340D')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3446',
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_342E',
    )

    FormationAddMember(ChrTable['科洛丝'], 0xFA, 0xFF)

    Jump('loc_3432')

    def _loc_342E(): pass

    label('loc_342E')

    FormationAddMember(ChrTable['科洛丝'], 0xFB, 0xFF)

    def _loc_3432(): pass

    label('loc_3432')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_3446(): pass

    label('loc_3446')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3493',
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3467',
    )

    FormationAddMember(ChrTable['金'], 0xFA, 0xFF)

    Jump('loc_347F')

    def _loc_3467(): pass

    label('loc_3467')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_347B',
    )

    FormationAddMember(ChrTable['金'], 0xFB, 0xFF)

    Jump('loc_347F')

    def _loc_347B(): pass

    label('loc_347B')

    FormationAddMember(ChrTable['金'], 0xFC, 0xFF)

    def _loc_347F(): pass

    label('loc_347F')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x8),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_3493(): pass

    label('loc_3493')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_34E0',
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34B4',
    )

    FormationAddMember(ChrTable['阿加特'], 0xFA, 0xFF)

    Jump('loc_34CC')

    def _loc_34B4(): pass

    label('loc_34B4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34C8',
    )

    FormationAddMember(ChrTable['阿加特'], 0xFB, 0xFF)

    Jump('loc_34CC')

    def _loc_34C8(): pass

    label('loc_34C8')

    FormationAddMember(ChrTable['阿加特'], 0xFC, 0xFF)

    def _loc_34CC(): pass

    label('loc_34CC')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x10),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_34E0(): pass

    label('loc_34E0')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_3505',
    )

    FormationAddMember(ChrTable['提妲'], 0xFC, 0xFF)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_3505(): pass

    label('loc_3505')

    Return()

# id: 0x0011 offset: 0x3506
@scena.Code('func_11_3506')
def func_11_3506():
    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_3516',
    )

    FormationDelMember(0x03, 0xFF)

    def _loc_3516(): pass

    label('loc_3516')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.And,
            Expr.Return,
        ),
        'loc_3526',
    )

    FormationDelMember(0x04, 0xFF)

    def _loc_3526(): pass

    label('loc_3526')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.And,
            Expr.Return,
        ),
        'loc_3536',
    )

    FormationDelMember(0x06, 0xFF)

    def _loc_3536(): pass

    label('loc_3536')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x8),
            Expr.And,
            Expr.Return,
        ),
        'loc_3546',
    )

    FormationDelMember(0x07, 0xFF)

    def _loc_3546(): pass

    label('loc_3546')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_3556',
    )

    FormationDelMember(0x05, 0xFF)

    def _loc_3556(): pass

    label('loc_3556')

    Return()

# id: 0x0012 offset: 0x3557
@scena.Code('func_12_3557')
def func_12_3557():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_35D4'),
        (0x00000001, 'loc_35DA'),
        (-1, 'loc_35E0'),
    )

    def _loc_35D4(): pass

    label('loc_35D4')

    OP_A2(0x1200)

    Jump('loc_35E0')

    def _loc_35DA(): pass

    label('loc_35DA')

    OP_A2(0x1201)

    Jump('loc_35E0')

    def _loc_35E0(): pass

    label('loc_35E0')

    Return()

# id: 0x0013 offset: 0x35E1
@scena.Code('func_13_35E1')
def func_13_35E1():
    ClearMapFlags(0x00000001)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            0x0000,
            0x0002,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0003,
            0x0004,
            0x0006,
            0x0007,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)
    Sleep(1000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
