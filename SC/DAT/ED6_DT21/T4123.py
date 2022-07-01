import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4123_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4123   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '艾南'),
    TXT(0x02, '管家菲利普'),
    TXT(0x03, '雪拉扎德'),
    TXT(0x04, '阿加特'),
    TXT(0x05, '奥利维尔'),
    TXT(0x06, '科洛丝'),
    TXT(0x07, '提妲'),
    TXT(0x08, '金'),
    TXT(0x09, '亚妮拉丝'),
    TXT(0x0A, '信'),
    TXT(0x0B, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4123.x'
    header.mapIndex       = 1
    header.bgm            = 34
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x3910
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
        ('ED6_DT07/CH02580._CH', 'ED6_DT07/CH02580P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT06/CH20053._CH', 'ED6_DT06/CH20053P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
        ('ED6_DT26/CH20301._CH', 'ED6_DT26/CH20301P._CP'),
        ('ED6_DT07/CH00024._CH', 'ED6_DT07/CH00024P._CP'),
        ('ED6_DT07/CH00054._CH', 'ED6_DT07/CH00054P._CP'),
        ('ED6_DT07/CH00034._CH', 'ED6_DT07/CH00034P._CP'),
        ('ED6_DT07/CH00044._CH', 'ED6_DT07/CH00044P._CP'),
        ('ED6_DT07/CH00064._CH', 'ED6_DT07/CH00064P._CP'),
        ('ED6_DT07/CH00074._CH', 'ED6_DT07/CH00074P._CP'),
        ('ED6_DT07/CH00033._CH', 'ED6_DT07/CH00033P._CP'),
        ('ED6_DT07/CH00073._CH', 'ED6_DT07/CH00073P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT27/CH03085._CH', 'ED6_DT27/CH03085P._CP'),
        ('ED6_DT27/CH03091._CH', 'ED6_DT27/CH03091P._CP'),
        ('ED6_DT26/CH20415._CH', 'ED6_DT26/CH20415P._CP'),
    ]

# id: 0x10002 offset: 0x15A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -4460,
            z                   = 0,
            y                   = 960,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
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
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0191,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0191,
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
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0191,
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
            dword_10            = 8,
            chipIndex           = 8,
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
            dword_10            = 1966096,
            chipIndex           = 18,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x29A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x29A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x29A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 4970,
            triggerZ            = 0,
            triggerY            = -1040,
            triggerRange        = 1400,
            actorX              = 4970,
            actorZ              = 2000,
            actorY              = -1040,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2BE
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            Expr.Return,
        ),
        'loc_3C5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Return,
        ),
        'loc_2E2',
    )

    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -5450, 0, 310, 0)

    def _loc_2E2(): pass

    label('loc_2E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_310',
    )

    OP_4A(0x000B, 255)
    ClearChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000B, 0x0004)
    SetChrPos(0x000B, 54780, 200, -3510, 90)
    SetChrChipByIndex(0x000B, 11)

    Jump('loc_334')

    def _loc_310(): pass

    label('loc_310')

    OP_4A(0x000A, 255)
    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0004)
    SetChrPos(0x000A, 54780, 200, -3510, 90)
    SetChrChipByIndex(0x000A, 10)

    def _loc_334(): pass

    label('loc_334')

    OP_4A(0x000D, 255)
    OP_4A(0x000E, 255)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    SetChrFlags(0x000C, 0x0004)
    SetChrFlags(0x000F, 0x0004)
    SetChrPos(0x000C, 57160, 200, -5120, 270)
    SetChrPos(0x000D, 60800, 0, 2300, 0)
    SetChrPos(0x000E, 58950, 0, 2510, 180)
    SetChrPos(0x000F, 54780, 200, -5080, 90)
    SetChrChipByIndex(0x000C, 12)
    SetChrChipByIndex(0x000D, 13)
    SetChrChipByIndex(0x000E, 14)
    SetChrChipByIndex(0x000F, 15)
    OP_4A(0x0008, 255)
    SetChrFlags(0x0008, 0x0002)
    SetChrChipByIndex(0x0008, 9)
    SetChrSubChip(0x0008, 0)

    def _loc_3C5(): pass

    label('loc_3C5')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_3D1'),
        (-1, 'loc_3F7'),
    )

    def _loc_3D1(): pass

    label('loc_3D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3F4',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x02000000)
    SetMapFlags(0x10000000)
    Event(0, 0x000B)

    def _loc_3F4(): pass

    label('loc_3F4')

    Jump('loc_3F7')

    def _loc_3F7(): pass

    label('loc_3F7')

    Return()

# id: 0x0001 offset: 0x3F8
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            Expr.Return,
        ),
        'loc_404',
    )

    OP_72(0x0005, 0x0004)

    def _loc_404(): pass

    label('loc_404')

    Return()

# id: 0x0002 offset: 0x405
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
        'loc_42A',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_56C')

    def _loc_42A(): pass

    label('loc_42A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_443',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_56C')

    def _loc_443(): pass

    label('loc_443')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_45C',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_56C')

    def _loc_45C(): pass

    label('loc_45C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_475',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_56C')

    def _loc_475(): pass

    label('loc_475')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_48E',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_56C')

    def _loc_48E(): pass

    label('loc_48E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4A7',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_56C')

    def _loc_4A7(): pass

    label('loc_4A7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C0',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_56C')

    def _loc_4C0(): pass

    label('loc_4C0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4D9',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_56C')

    def _loc_4D9(): pass

    label('loc_4D9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4F2',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_56C')

    def _loc_4F2(): pass

    label('loc_4F2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_50B',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_56C')

    def _loc_50B(): pass

    label('loc_50B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_524',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_56C')

    def _loc_524(): pass

    label('loc_524')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_53D',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_56C')

    def _loc_53D(): pass

    label('loc_53D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_556',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_56C')

    def _loc_556(): pass

    label('loc_556')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_56C',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_56C(): pass

    label('loc_56C')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_581',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_56C')

    def _loc_581(): pass

    label('loc_581')

    Return()

# id: 0x0003 offset: 0x582
@scena.Code('func_03_582')
def func_03_582():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Return,
        ),
        'loc_5C3',
    )

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾南倒下睡着了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Jump('loc_5FE')

    def _loc_5C3(): pass

    label('loc_5C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            Expr.Return,
        ),
        'loc_5FE',
    )

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾南倒下睡着了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_5FE(): pass

    label('loc_5FE')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x602
@scena.Code('func_04_602')
def func_04_602():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#0660270189V#720F艾丝蒂尔大人、各位的看护\n',
            '请交给我菲利普吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660270190V公爵阁下的事，\n',
            '就请你们多多关照了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x67C
@scena.Code('func_05_67C')
def func_05_67C():
    TalkBegin(0x00FE)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '雪拉扎德在桌子上\n',
            '趴着睡着了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x6C4
@scena.Code('func_06_6C4')
def func_06_6C4():
    TalkBegin(0x00FE)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '阿加特在桌子上\n',
            '趴着睡着了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x70A
@scena.Code('func_07_70A')
def func_07_70A():
    TalkBegin(0x00FE)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '奥利维尔在桌子上\n',
            '趴着睡着了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x752
@scena.Code('func_08_752')
def func_08_752():
    TalkBegin(0x000D)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '科洛丝在书架旁\n',
            '倚靠着睡着了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x000D)

    Return()

# id: 0x0009 offset: 0x79A
@scena.Code('func_09_79A')
def func_09_79A():
    TalkBegin(0x000E)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '提妲在书架旁\n',
            '倚靠着睡着了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x000E)

    Return()

# id: 0x000A offset: 0x7E0
@scena.Code('func_0A_7E0')
def func_0A_7E0():
    TalkBegin(0x00FE)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '金在桌子上\n',
            '趴着睡着了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x822
@scena.Code('func_0B_822')
def func_0B_822():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_835',
    )

    Call(0, 0x001A)

    def _loc_835(): pass

    label('loc_835')

    OP_4A(0x0008, 255)
    SetChrFlags(0x0008, 0x0002)
    SetChrChipByIndex(0x0008, 9)
    SetChrSubChip(0x0008, 0)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0109, 0x0080)
    SetChrFlags(0x0143, 0x0080)
    SetChrFlags(0x00F7, 0x0080)
    OP_6D(30, -250, -5270, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_72(0x0005, 0x0004)
    FadeIn(1500, 0)
    Sleep(500)

    OP_22(0x0006, 0x00, 0x64)
    Sleep(500)

    CreateThread(0x0101, 0x01, 0x00, 0x000C)
    Sleep(800)

    CreateThread(0x0109, 0x01, 0x00, 0x000D)
    Sleep(800)

    CreateThread(0x0143, 0x01, 0x00, 0x000E)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010270035V#1011F艾南先生，我们回来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_20(0x000007D0)
    OP_6D(-4460, 0, 960, 2000)
    Sleep(1000)

    Fade(1000)
    OP_6D(-2420, 0, -1880, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(277, 0)
    OP_0D()
    OP_1D(0x51)

    ChrTalk(
        0x0101,
        (
            '#0010270036V#1020F#5P艾、艾南先生！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0143,
        (
            '#0660270037V#721F怎么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270038V#1069F哼，来这套啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0101, 0x01, 0x00, 0x000F)
    Sleep(500)

    CreateThread(0x0143, 0x01, 0x00, 0x0011)
    Sleep(200)

    CreateThread(0x0109, 0x01, 0x00, 0x0010)

    @scena.Lambda('lambda_0A1D')
    def lambda_0A1D():
        OP_6D(-5430, 0, 690, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0A1D)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010270039V#1020F#5P艾南先生！？\n',
            '艾南先生！',
            TxtCtl.Enter,
        ),
    )

    WaitForThreadExit(0x0109, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Fade(250)
    SetChrFlags(0x0109, 0x0002)
    SetChrChipByIndex(0x0109, 19)
    SetChrSubChip(0x0109, 3)
    OP_0D()
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0109,
        (
            '#0180270040V#1067F呼吸还很平稳……\n',
            '看来是睡着了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270041V#1063F这个人就是王都支部的接待吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270042V#1026F嗯，嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x0101, 135, 400)

    ChrTalk(
        0x0101,
        (
            '#0010270043V#1020F……大家！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0B67')
    def lambda_0B67():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_0B67')

    DispatchAsync2(0x0143, 0x0002, lambda_0B67)

    OP_8E(0x0101, -4230, 0, -2820, 6000, 0x00)

    @scena.Lambda('lambda_0B8C')
    def lambda_0B8C():
        OP_6D(-1050, 0, 3360, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B8C)

    OP_8E(0x0101, -1000, 0, -2890, 6000, 0x00)
    OP_8E(0x0101, 4270, 0, 4610, 6000, 0x00)
    OP_8E(0x0101, -3420, 3500, 5000, 6000, 0x00)
    Fade(1000)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, 56220, 600, -3080, 180)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_C23',
    )

    OP_4A(0x000B, 255)
    ClearChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000B, 0x0004)
    SetChrPos(0x000B, 54780, 200, -3510, 90)
    SetChrChipByIndex(0x000B, 11)

    Jump('loc_C47')

    def _loc_C23(): pass

    label('loc_C23')

    OP_4A(0x000A, 255)
    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0004)
    SetChrPos(0x000A, 54780, 200, -3510, 90)
    SetChrChipByIndex(0x000A, 10)

    def _loc_C47(): pass

    label('loc_C47')

    ClearChrFlags(0x0109, 0x0002)
    SetChrChipByIndex(0x0109, 65535)
    TerminateThread(0x0143, 0x02)
    OP_4A(0x000D, 255)
    OP_4A(0x000E, 255)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    SetChrFlags(0x000C, 0x0004)
    SetChrFlags(0x000F, 0x0004)
    SetChrPos(0x000C, 57160, 200, -5120, 270)
    SetChrPos(0x000D, 60800, 0, 2300, 0)
    SetChrPos(0x000E, 58950, 0, 2510, 180)
    SetChrPos(0x000F, 54780, 200, -5080, 90)
    SetChrChipByIndex(0x000C, 12)
    SetChrChipByIndex(0x000D, 13)
    SetChrChipByIndex(0x000E, 14)
    SetChrChipByIndex(0x000F, 15)
    OP_6D(56580, 0, -270, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    CreateThread(0x0101, 0x01, 0x00, 0x0017)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010270044V#1020F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0D49')
    def lambda_0D49():
        OP_6D(54530, 0, -560, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0D49)

    OP_8E(0x0101, 54820, 0, -1300, 3000, 0x00)
    WaitForThreadExit(0x0101, 0x0001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_DB3',
    )

    ChrTalk(
        0x0101,
        (
            '#0010270045V#1020F#5P阿加特、奥利维尔、金先生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DE8')

    def _loc_DB3(): pass

    label('loc_DB3')

    ChrTalk(
        0x0101,
        (
            '#0010270046V#1020F#5P雪拉姐、奥利维尔、金先生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DE8(): pass

    label('loc_DE8')

    OP_8C(0x0101, 45, 600)
    Sleep(500)

    @scena.Lambda('lambda_0DFA')
    def lambda_0DFA():
        OP_6D(57790, 0, 1880, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0DFA)

    OP_8E(0x0101, 59620, 0, 910, 4000, 0x00)
    ChrTurnDirection(0x0101, 0x000E, 400)
    Sleep(500)

    ChrTurnDirection(0x0101, 0x000D, 400)
    Sleep(500)

    OP_8C(0x0101, 0, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010270047V#1020F#6P提妲、科洛丝！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0109, 0x01, 0x00, 0x0012)
    Sleep(800)

    CreateThread(0x0143, 0x01, 0x00, 0x0013)
    WaitForThreadExit(0x0109, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0109,
        (
            '#0180270048V#1068F#6P糟糕……\n',
            '看来全员都中招了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0109, 90, 400)
    WaitForThreadExit(0x0143, 0x0001)
    CreateThread(0x0143, 0x01, 0x00, 0x0014)
    Sleep(400)

    OP_8E(0x0109, 58490, 0, 840, 3000, 0x00)
    ChrTurnDirection(0x0109, 0x0101, 400)

    ChrTalk(
        0x0109,
        (
            '#0180270049V#1063F#5P怎样、没事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270050V#1026F#6P嗯，嗯……\n',
            '好像都睡着了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270051V#1007F到底大家，\n',
            '这是怎么了啊～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0143, 0x0001)

    @scena.Lambda('lambda_0F8E')
    def lambda_0F8E():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_0F8E')

    DispatchAsync2(0x0143, 0x0001, lambda_0F8E)

    Sleep(500)

    ChrTalk(
        0x0143,
        (
            '#0660270052V#720F#5P唔，看来是\n',
            '中招了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660270053V大家看起来像突然被睡魔袭击\n',
            '一样倒地不起了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 315, 400)

    ChrTalk(
        0x0101,
        (
            '#0010270054V#1015F#6P确、确实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0109, 0, 400)

    ChrTalk(
        0x0109,
        (
            '#0180270055V#1064F#6P哦哦，真敏锐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0011, 400)
    Sleep(1000)

    @scena.Lambda('lambda_1092')
    def lambda_1092():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_1092')

    DispatchAsync2(0x0109, 0x0001, lambda_1092)

    @scena.Lambda('lambda_10A3')
    def lambda_10A3():
        OP_6D(56030, 0, 20, 1500)

        ExitThread()

    DispatchAsync(0x0143, 0x0002, lambda_10A3)

    OP_8E(0x0101, 56290, 0, -2290, 3000, 0x00)
    ChrTurnDirection(0x0101, 0x0011, 400)
    WaitForThreadExit(0x0143, 0x0002)
    WaitForThreadExit(0x0143, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010270056V#1004F#5P咦，这封信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0109, 0x01)
    OP_62(0x0109, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_1129')
    def lambda_1129():
        OP_8E(0x00FE, 56780, 0, -890, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0000, lambda_1129)

    WaitForThreadExit(0x0109, 0x0000)
    ChrTurnDirection(0x0109, 0x0011, 400)

    ChrTalk(
        0x0109,
        (
            '#0180270057V#1064F#2P等一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270058V这个，和我们收到的\n',
            '信封不是一样的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270059V#1020F#6P嗯、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9F(0x0011, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)
    SetChrFlags(0x0011, 0x0080)
    Sleep(500)

    ChrTurnDirection(0x0101, 0x0109, 400)
    Sleep(500)

    Sleep(200)

    Fade(250)
    SetChrChipByIndex(0x0101, 21)
    SetChrSubChip(0x0101, 0)
    OP_0D()
    Sleep(200)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔打开信封确认了信的内容。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AD(0x00240097, 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '小女孩和公爵在我们手上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '想要回他们的话，\n',
            '就请参加『茶会』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    Sleep(1500)

    ChrTalk(
        0x0101,
        (
            '#0010270062V#1005F#6P你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0143,
        (
            '#0660270063V#721F#8P公、公爵阁下……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270064V#1065F#2P茶会的地点\n',
            '果然还是王都吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270065V#1063F这里写的\n',
            '女孩是谁，知道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0101, 0)

    ChrTalk(
        0x0101,
        (
            '#0010270066V#1004F#6P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 270, 600)
    Sleep(500)

    OP_8C(0x0101, 90, 600)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010270067V#1020F#5P玲！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270068V玲，你在哪儿！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_140B')
    def lambda_140B():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_140B')

    DispatchAsync2(0x0109, 0x0001, lambda_140B)

    @scena.Lambda('lambda_141C')
    def lambda_141C():
        OP_6D(63130, 0, 4190, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_141C)

    OP_8E(0x0101, 64290, 0, 320, 6000, 0x00)
    OP_8E(0x0101, 64590, 2000, 4740, 6000, 0x00)
    OP_8E(0x0101, 61650, 3850, 4740, 6000, 0x00)
    TerminateThread(0x0109, 0x01)
    TerminateThread(0x0143, 0x01)
    Fade(1000)
    OP_6D(119700, 0, 4700, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, 125400, -2000, 4700, 270)
    OP_8E(0x0101, 119700, 0, 4700, 5000, 0x00)
    OP_69(0x0101, 0x00000000)

    @scena.Lambda('lambda_14E6')
    def lambda_14E6():
        OP_69(0x0101, 0x00000000)
        Yield()

        Jump('lambda_14E6')

    DispatchAsync2(0x0101, 0x0001, lambda_14E6)

    OP_8E(0x0101, 119700, 0, -1390, 5000, 0x00)
    OP_8C(0x0101, 270, 600)
    Sleep(500)

    OP_8C(0x0101, 90, 600)
    Sleep(500)

    CreateThread(0x0109, 0x01, 0x00, 0x0015)
    OP_8C(0x0101, 180, 600)
    Sleep(500)

    TerminateThread(0x0101, 0x01)
    Sleep(300)

    CreateThread(0x0143, 0x01, 0x00, 0x0016)

    @scena.Lambda('lambda_1546')
    def lambda_1546():
        OP_6D(119410, 0, -320, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1546)

    WaitForThreadExit(0x0109, 0x0001)

    ChrTalk(
        0x0109,
        (
            '#0180270069V#1063F#2P看来是把那孩子\n',
            '掳走了啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270070V艾丝蒂尔的朋友吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010270071V#1026F#6P不，是因为某些原因\n',
            '暂时照看的孩子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270072V#1027F居然偏偏\n',
            '被卷进这种事……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270073V#1067F#2P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0143,
        (
            '#0660270074V#722F艾丝蒂尔大人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_61(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010270075V#1003F#6P对不起，菲利普先生……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270076V说不定公爵\n',
            '也是受连累的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0143,
        (
            '#0660270077V#720F不，这不一定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660270078V即便是这样\n',
            '到这时候还一个人\n',
            '到处转悠的阁下也有责任。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660270079V请别这么自责。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270080V#1063F#2P对啊、艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270081V首先要去追查\n',
            '信中所说的茶会才是啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270082V#1002F#6P嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(250)
    SetChrChipByIndex(0x0101, 21)
    SetChrSubChip(0x0101, 0)
    OP_0D()
    Sleep(200)

    Sleep(200)

    FadeOut(300, 0, 100)
    OP_AD(0x00240097, 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetChrName('')
    SetMessageWindowPos(-1, 300, -1, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '小女孩和公爵在我们手上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '想要回他们的话，\n',
            '就请参加『茶会』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    Sleep(1500)

    Fade(250)
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0101, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010270085V#1015F#6P这么说来茶会这话\n',
            '好像在谈到特务兵余党的时候\n',
            '艾南先生说过似的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270086V#1004F……对了，凯文先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270087V刚才读信的时候，\n',
            '你是不是说了句\n',
            '果然还是在王都吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270088V#1064F#2P怎么，你听到了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270089V#1066F嗯～其实是\n',
            '有点内情的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2711',
    )

    SetChrPos(0x000A, 125400, 0, 4700, 270)

    NpcTalk(
        0x000A,
        '女性的声音',
        (
            '#0030270090V#5P……这个内情\n',
            '让我来说明吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_4A(0x000A, 255)
    SetChrChipByIndex(0x000A, 2)
    SetChrPos(0x000A, 125400, -2000, 4700, 270)
    ClearChrFlags(0x000A, 0x0080)

    @scena.Lambda('lambda_1A47')
    def lambda_1A47():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_1A47)

    @scena.Lambda('lambda_1A55')
    def lambda_1A55():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0143, 0x0001, lambda_1A55)

    @scena.Lambda('lambda_1A63')
    def lambda_1A63():
        OP_6D(118950, 0, 1040, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1A63)

    OP_8E(0x000A, 119700, 0, 4700, 3000, 0x00)
    OP_8E(0x000A, 119700, 0, 1770, 3000, 0x00)

    ChrTalk(
        0x0109,
        (
            '#0180270091V#1062F#6P哦、时机正好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270092V#1004F#6P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270093V雪，雪拉姐！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030270094V#027F好久不见了、艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270095V好像发生了\n',
            '很严重的事嘛？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270096V#025F不过凯文先生。\n',
            '我们彼此都没赶上呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270097V#1068F#6P嗯嗯，真没面子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270098V#1020F#6P为、为什么\n',
            '雪拉姐会在这里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270099V而且，为什么能和凯文先生\n',
            '这么自然的说话！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030270100V#020F我和亚妮拉丝\n',
            '发现了特务兵的大本营\n',
            '这你可能听说了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270101V就在那时，\n',
            '认识了这个人的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270102V在搜索消失的余党上\n',
            '现在还要请他帮忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270103V#1025F#6P是、是吗……\n',
            '所以才这么清楚状况啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270104V#1060F#5P嘿嘿，就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0010, 125400, 0, 4700, 270)

    NpcTalk(
        0x0010,
        '女孩的声音',
        (
            '#0120270105V#5P雪拉前辈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0010, 400)

    @scena.Lambda('lambda_1D85')
    def lambda_1D85():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_1D85')

    DispatchAsync2(0x000A, 0x0001, lambda_1D85)

    SetChrPos(0x0010, 125400, -2000, 4700, 270)
    ClearChrFlags(0x0010, 0x0080)
    SetChrChipByIndex(0x0010, 20)
    OP_8E(0x0010, 119700, 0, 4700, 5000, 0x00)
    OP_8E(0x0010, 120700, 0, 1650, 5000, 0x00)
    SetChrChipByIndex(0x0010, 8)
    SetChrSubChip(0x0010, 0)
    TerminateThread(0x000A, 0x01)

    ChrTalk(
        0x0101,
        (
            '#0010270106V#1004F#6P啊，亚妮拉丝！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0120270107V#811F#2P艾丝蒂尔！\n',
            '太好了，你没事啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120270108V#1310F还有凯文先生\n',
            '也来了这边啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270109V#1060F#6P啊啊，我也\n',
            '没赶上啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030270110V#020F#5P对了，下面的通信器怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x000A, 400)

    ChrTalk(
        0x0010,
        (
            '#0120270111V#1316F#4P不行……\n',
            '好像被拿走了零件\n',
            '无法马上使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030270112V#026F#5P这么说来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000A, 225, 500)

    @scena.Lambda('lambda_1F57')
    def lambda_1F57():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_1F57')

    DispatchAsync2(0x0101, 0x0001, lambda_1F57)

    @scena.Lambda('lambda_1F68')
    def lambda_1F68():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_1F68')

    DispatchAsync2(0x0109, 0x0001, lambda_1F68)

    @scena.Lambda('lambda_1F79')
    def lambda_1F79():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_1F79')

    DispatchAsync2(0x0143, 0x0001, lambda_1F79)

    @scena.Lambda('lambda_1F8A')
    def lambda_1F8A():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_1F8A')

    DispatchAsync2(0x0010, 0x0001, lambda_1F8A)

    OP_8E(0x000A, 117610, 0, 410, 3000, 0x00)

    @scena.Lambda('lambda_1FAF')
    def lambda_1FAF():
        OP_6D(116400, 0, 3390, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1FAF)

    @scena.Lambda('lambda_1FC7')
    def lambda_1FC7():
        OP_67(0, 3500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1FC7)

    @scena.Lambda('lambda_1FDF')
    def lambda_1FDF():
        OP_6B(3140, 3000)

        ExitThread()

    DispatchAsync(0x0109, 0x0002, lambda_1FDF)

    @scena.Lambda('lambda_1FEF')
    def lambda_1FEF():
        OP_6E(306, 3000)

        ExitThread()

    DispatchAsync(0x0109, 0x0003, lambda_1FEF)

    OP_8E(0x000A, 114650, 250, 560, 3000, 0x00)
    OP_8E(0x000A, 115020, 250, 4850, 3000, 0x00)
    Sleep(1000)

    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0109, 0x01)
    TerminateThread(0x0143, 0x01)
    TerminateThread(0x0010, 0x01)

    ChrTalk(
        0x000A,
        (
            '#0030270113V#522F#6P不行，这边也一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    OP_6D(118020, 0, 400, 0)
    OP_67(0, 5230, -10000, 0)
    OP_6B(2620, 0)
    OP_6C(315000, 0)
    OP_6E(306, 0)
    OP_8C(0x000A, 180, 400)
    CreateThread(0x000A, 0x00, 0x00, 0x0018)
    Sleep(500)

    CreateThread(0x0010, 0x00, 0x00, 0x0019)

    @scena.Lambda('lambda_20C9')
    def lambda_20C9():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_20C9')

    DispatchAsync2(0x0101, 0x0001, lambda_20C9)

    @scena.Lambda('lambda_20DA')
    def lambda_20DA():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_20DA')

    DispatchAsync2(0x0109, 0x0001, lambda_20DA)

    @scena.Lambda('lambda_20EB')
    def lambda_20EB():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_20EB')

    DispatchAsync2(0x0143, 0x0001, lambda_20EB)

    WaitForThreadExit(0x000A, 0x0000)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0109, 0x01)
    TerminateThread(0x0143, 0x01)
    TerminateThread(0x0010, 0x01)

    ChrTalk(
        0x0101,
        (
            '#0010270114V#1002F这么说……\n',
            '是敌人破坏的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030270115V#022F#5P不会错的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270116V到底是为了什么\n',
            '要做这种事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010270117V#1004F对了，雪拉姐！\n',
            '这个留下的信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔给雪拉扎德等人\n',
            '说明了之前发现信的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x000A,
        (
            '#0030270118V#026F#5P茶会……\n',
            '总算全部连接起来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270119V#022F掳走那孩子和公爵的\n',
            '是特务兵的余党没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270120V而且背后\n',
            '应该是『噬身之蛇』在搞鬼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270121V#1026F嗯，我们也\n',
            '被奇怪的机械袭击了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270122V但是参加茶会\n',
            '应该去哪里才好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030270123V#026F#5P总之只有去想得到的地方\n',
            '找找看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000A, 45, 400)
    Sleep(400)

    ChrTalk(
        0x000A,
        (
            '#0030270124V#020F#5P亚妮拉丝。\n',
            '能不能拜托你件事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0120270125V#814F好，什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030270126V#022F#5P希望你去艾尔贝离宫的警备本部\n',
            '联络一下这个情况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270127V出现在周游道上的武装集团\n',
            '恐怕是表面佯攻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270128V#1002F原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270129V#1063F#4P果然真正目的是王都啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0120270130V#816F明白了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120270131V那么我立刻\n',
            '冲去离宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0010, 400)

    ChrTalk(
        0x0101,
        (
            '#0010270132V#1002F亚妮拉丝，小心啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '#0120270133V#811F嗯，艾丝蒂尔也是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2568')
    def lambda_2568():
        ChrTurnDirection(0x0109, 0x0010, 400)
        Yield()

        Jump('lambda_2568')

    DispatchAsync2(0x0109, 0x0000, lambda_2568)

    @scena.Lambda('lambda_2579')
    def lambda_2579():
        ChrTurnDirection(0x0143, 0x0010, 400)
        Yield()

        Jump('lambda_2579')

    DispatchAsync2(0x0143, 0x0000, lambda_2579)

    OP_8C(0x0010, 0, 400)

    @scena.Lambda('lambda_2591')
    def lambda_2591():
        OP_6D(119000, 0, 1990, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2591)

    SetChrChipByIndex(0x0010, 20)
    OP_8E(0x0010, 119700, 0, 4700, 5000, 0x00)
    OP_8E(0x0010, 125400, -2000, 4700, 5000, 0x00)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    @scena.Lambda('lambda_25E0')
    def lambda_25E0():
        OP_6D(118020, 0, 400, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_25E0)

    OP_8C(0x000A, 90, 400)

    @scena.Lambda('lambda_25FF')
    def lambda_25FF():
        OP_8C(0x0101, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_25FF)

    Sleep(50)

    @scena.Lambda('lambda_2612')
    def lambda_2612():
        OP_8C(0x0109, 270, 400)

        ExitThread()

    DispatchAsync(0x0109, 0x0000, lambda_2612)

    Sleep(50)

    @scena.Lambda('lambda_2625')
    def lambda_2625():
        OP_8C(0x0143, 270, 400)

        ExitThread()

    DispatchAsync(0x0143, 0x0000, lambda_2625)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x000A,
        (
            '#0030270134V#020F#5P管家先生，不好意思\n',
            '你能在协会待命吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270135V我们一定会找回公爵阁下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0143,
        (
            '#0660270136V#720F#4P……明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660270137V待命期间，就让我\n',
            '负责各位的护理吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660270138V阁下就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_346E')

    def _loc_2711(): pass

    label('loc_2711')

    SetChrPos(0x000B, 125400, 0, 4700, 270)

    NpcTalk(
        0x000B,
        '青年的声音',
        (
            '#0050270139V#5P……这个内情\n',
            '让我来说明吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_4A(0x000B, 255)
    SetChrChipByIndex(0x000B, 3)
    SetChrPos(0x000B, 125400, -2000, 4700, 270)
    ClearChrFlags(0x000B, 0x0080)

    @scena.Lambda('lambda_279E')
    def lambda_279E():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0109, 0x0001, lambda_279E)

    @scena.Lambda('lambda_27AC')
    def lambda_27AC():
        OP_8C(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0143, 0x0001, lambda_27AC)

    @scena.Lambda('lambda_27BA')
    def lambda_27BA():
        OP_6D(118950, 0, 1040, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_27BA)

    OP_8E(0x000B, 119700, 0, 4700, 3000, 0x00)
    OP_8E(0x000B, 119700, 0, 1770, 3000, 0x00)

    ChrTalk(
        0x0109,
        (
            '#0180270091V#1062F#6P哦、时机正好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270092V#1004F#6P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270142V阿、阿、阿加特！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0050270143V#051F好久不见了啊，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270144V事情变得\n',
            '相当麻烦了嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270145V#053F不过凯文。\n',
            '我们彼此都没赶上啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270097V#1068F#6P嗯嗯，真没面子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270147V#1020F#6P为、为什么\n',
            '阿加特会在这里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270099V而且，为什么能和凯文先生\n',
            '说得通话！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0050270149V#051F我和亚妮拉丝\n',
            '发现了特务兵的大本营\n',
            '这你听艾南说过吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270150V和这个不良神父\n',
            '就是那时候认识的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270151V在搜索消失的余党上\n',
            '现在还要请他帮忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270103V#1025F#6P是、是吗……\n',
            '所以才这么清楚状况啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270104V#1060F#5P嘿嘿，就是这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0010, 125400, 0, 4700, 270)

    NpcTalk(
        0x0010,
        '女孩的声音',
        (
            '#0120270154V#5P阿加特前辈！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0010, 400)

    @scena.Lambda('lambda_2ADE')
    def lambda_2ADE():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_2ADE')

    DispatchAsync2(0x000B, 0x0001, lambda_2ADE)

    SetChrPos(0x0010, 125400, -2000, 4700, 270)
    ClearChrFlags(0x0010, 0x0080)
    SetChrChipByIndex(0x0010, 20)
    OP_8E(0x0010, 119700, 0, 4700, 5000, 0x00)
    OP_8E(0x0010, 120700, 0, 1650, 5000, 0x00)
    SetChrChipByIndex(0x0010, 8)
    SetChrSubChip(0x0010, 0)
    TerminateThread(0x000B, 0x01)

    ChrTalk(
        0x0101,
        (
            '#0010270106V#1004F#6P啊，亚妮拉丝！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0120270107V#811F#2P艾丝蒂尔！\n',
            '太好了，你没事啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120270108V#1310F还有凯文先生\n',
            '也来了这边啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270109V#1060F#6P啊啊，我也\n',
            '没赶上啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0050270159V#050F#5P对了，下面的通信器怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x000B, 400)

    ChrTalk(
        0x0010,
        (
            '#0120270111V#1316F#4P不行……\n',
            '好像被拿走了零件\n',
            '无法马上使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0050270161V#552F#5P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000B, 225, 500)

    @scena.Lambda('lambda_2CAA')
    def lambda_2CAA():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_2CAA')

    DispatchAsync2(0x0101, 0x0001, lambda_2CAA)

    @scena.Lambda('lambda_2CBB')
    def lambda_2CBB():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_2CBB')

    DispatchAsync2(0x0109, 0x0001, lambda_2CBB)

    @scena.Lambda('lambda_2CCC')
    def lambda_2CCC():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_2CCC')

    DispatchAsync2(0x0143, 0x0001, lambda_2CCC)

    @scena.Lambda('lambda_2CDD')
    def lambda_2CDD():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_2CDD')

    DispatchAsync2(0x0010, 0x0001, lambda_2CDD)

    OP_8E(0x000B, 117610, 0, 410, 3000, 0x00)

    @scena.Lambda('lambda_2D02')
    def lambda_2D02():
        OP_6D(116400, 0, 3390, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2D02)

    @scena.Lambda('lambda_2D1A')
    def lambda_2D1A():
        OP_67(0, 3500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2D1A)

    @scena.Lambda('lambda_2D32')
    def lambda_2D32():
        OP_6B(3140, 3000)

        ExitThread()

    DispatchAsync(0x0109, 0x0002, lambda_2D32)

    @scena.Lambda('lambda_2D42')
    def lambda_2D42():
        OP_6E(306, 3000)

        ExitThread()

    DispatchAsync(0x0109, 0x0003, lambda_2D42)

    OP_8E(0x000B, 114650, 250, 560, 3000, 0x00)
    OP_8E(0x000B, 115020, 250, 4850, 3000, 0x00)
    Sleep(1000)

    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0109, 0x01)
    TerminateThread(0x0143, 0x01)
    TerminateThread(0x0010, 0x01)

    ChrTalk(
        0x000B,
        (
            '#0050270162V#555F#6P哼，这边也一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    OP_6D(118020, 0, 400, 0)
    OP_67(0, 5230, -10000, 0)
    OP_6B(2620, 0)
    OP_6C(315000, 0)
    OP_6E(306, 0)
    OP_8C(0x000B, 180, 400)
    CreateThread(0x000B, 0x00, 0x00, 0x0018)
    Sleep(500)

    CreateThread(0x0010, 0x00, 0x00, 0x0019)

    @scena.Lambda('lambda_2E1A')
    def lambda_2E1A():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_2E1A')

    DispatchAsync2(0x0101, 0x0001, lambda_2E1A)

    @scena.Lambda('lambda_2E2B')
    def lambda_2E2B():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_2E2B')

    DispatchAsync2(0x0109, 0x0001, lambda_2E2B)

    @scena.Lambda('lambda_2E3C')
    def lambda_2E3C():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_2E3C')

    DispatchAsync2(0x0143, 0x0001, lambda_2E3C)

    WaitForThreadExit(0x000B, 0x0000)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0109, 0x01)
    TerminateThread(0x0143, 0x01)
    TerminateThread(0x0010, 0x01)

    ChrTalk(
        0x0101,
        (
            '#0010270114V#1002F这么说……\n',
            '是敌人破坏的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0050270164V#050F#5P没错吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270165V问题是到底为了什么\n',
            '做这种事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010270166V#1004F对了、阿加特！\n',
            '这个留下的信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔对阿加特等人\n',
            '说明了之前发现信的情况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x000B,
        (
            '#0050270167V#053F#5P茶会……\n',
            '总算全部连接起来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270168V#057F掳走那孩子和公爵的\n',
            '肯定是特务兵的余党吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270169V而且背后\n',
            '应该是『噬身之蛇』在搞鬼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270121V#1026F嗯，我们也\n',
            '被奇怪的机械袭击了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270122V但是参加茶会\n',
            '应该去哪里才好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0050270172V#053F#5P总之只有去想得到的地方\n',
            '从头找找看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000B, 45, 400)
    Sleep(400)

    ChrTalk(
        0x000B,
        (
            '#0050270173V#050F#5P亚妮拉丝，有件事想拜托你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0120270125V#814F好，什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0050270175V#050F#5P去艾尔贝离宫的警备本部\n',
            '联络一下这个情况。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270176V出现在周游道上的武装集团\n',
            '恐怕是表面佯攻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270128V#1002F原来如此……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270129V#1063F#4P果然真正目的是王都啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0120270130V#816F明白了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120270131V那么我立刻\n',
            '冲去离宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0010, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010270132V#1002F亚妮拉丝，小心啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '#0120270133V#811F嗯，艾丝蒂尔也是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_32B6')
    def lambda_32B6():
        ChrTurnDirection(0x0109, 0x0010, 400)
        Yield()

        Jump('lambda_32B6')

    DispatchAsync2(0x0109, 0x0000, lambda_32B6)

    @scena.Lambda('lambda_32C7')
    def lambda_32C7():
        ChrTurnDirection(0x0143, 0x0010, 400)
        Yield()

        Jump('lambda_32C7')

    DispatchAsync2(0x0143, 0x0000, lambda_32C7)

    OP_8C(0x0010, 0, 400)

    @scena.Lambda('lambda_32DF')
    def lambda_32DF():
        OP_6D(119000, 0, 1990, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_32DF)

    SetChrChipByIndex(0x0010, 20)
    OP_8E(0x0010, 119700, 0, 4700, 5000, 0x00)
    OP_8E(0x0010, 125400, -2000, 4700, 5000, 0x00)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    @scena.Lambda('lambda_332E')
    def lambda_332E():
        OP_6D(118020, 0, 400, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_332E)

    OP_8C(0x000B, 90, 400)

    @scena.Lambda('lambda_334D')
    def lambda_334D():
        OP_8C(0x0101, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_334D)

    Sleep(50)

    @scena.Lambda('lambda_3360')
    def lambda_3360():
        OP_8C(0x0109, 270, 400)

        ExitThread()

    DispatchAsync(0x0109, 0x0000, lambda_3360)

    Sleep(50)

    @scena.Lambda('lambda_3373')
    def lambda_3373():
        OP_8C(0x0143, 270, 400)

        ExitThread()

    DispatchAsync(0x0143, 0x0000, lambda_3373)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x000B,
        (
            '#0050270183V#050F#5P记得你是菲利普吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270184V不好意思\n',
            '你就待在协会待命吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270185V我们一定找回公爵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0143,
        (
            '#0660270136V#720F#4P……明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660270137V待命期间，就让我\n',
            '负责各位的护理吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660270138V阁下就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_346E(): pass

    label('loc_346E')

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T4310._SN', 105, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x3486
@scena.Code('func_0C_3486')
def func_0C_3486():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 90, -500, -7250, 0)

    @scena.Lambda('lambda_34AD')
    def lambda_34AD():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_34AD)

    OP_8E(0x00FE, -20, -130, -4440, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x0008, 400)

    Return()

# id: 0x000D offset: 0x34D5
@scena.Code('func_0D_34D5')
def func_0D_34D5():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 90, -500, -7250, 0)

    @scena.Lambda('lambda_34FC')
    def lambda_34FC():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_34FC)

    OP_8E(0x00FE, 1090, -130, -4460, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x0008, 400)

    Return()

# id: 0x000E offset: 0x3524
@scena.Code('func_0E_3524')
def func_0E_3524():
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 90, -500, -7250, 0)

    @scena.Lambda('lambda_354B')
    def lambda_354B():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_354B)

    OP_8E(0x00FE, -40, -250, -5540, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x0008, 400)

    Return()

# id: 0x000F offset: 0x3573
@scena.Code('func_0F_3573')
def func_0F_3573():
    OP_8E(0x00FE, -4480, 0, -2950, 5000, 0x00)
    OP_8E(0x00FE, -5700, 0, 620, 5000, 0x00)
    ChrTurnDirection(0x00FE, 0x0008, 400)

    Return()

# id: 0x0010 offset: 0x35A3
@scena.Code('func_10_35A3')
def func_10_35A3():
    OP_8E(0x00FE, -2610, 0, -3340, 4000, 0x00)
    OP_8E(0x00FE, -4920, 0, -3220, 4000, 0x00)
    OP_8E(0x00FE, -4730, 0, 0, 4000, 0x00)

    Return()

# id: 0x0011 offset: 0x35E0
@scena.Code('func_11_35E0')
def func_11_35E0():
    OP_8E(0x00FE, -2610, 0, -3340, 4000, 0x00)
    OP_8E(0x00FE, -4920, 0, -3220, 4000, 0x00)
    OP_8E(0x00FE, -5730, 0, -1010, 4000, 0x00)

    Return()

# id: 0x0012 offset: 0x361D
@scena.Code('func_12_361D')
def func_12_361D():
    SetChrPos(0x00FE, 60250, -2000, 4530, 270)
    OP_8E(0x00FE, 55110, 0, 4750, 3000, 0x00)
    OP_8E(0x00FE, 55140, 0, 1860, 3000, 0x00)
    Sleep(500)

    OP_8C(0x00FE, 90, 400)
    Sleep(500)

    OP_8C(0x00FE, 180, 400)

    Return()

# id: 0x0013 offset: 0x366F
@scena.Code('func_13_366F')
def func_13_366F():
    SetChrPos(0x00FE, 60250, -2000, 4530, 270)
    OP_8E(0x00FE, 55110, 0, 4750, 3000, 0x00)
    OP_8C(0x00FE, 180, 400)
    Sleep(1000)

    ChrTurnDirection(0x00FE, 0x000E, 400)

    Return()

# id: 0x0014 offset: 0x36A8
@scena.Code('func_14_36A8')
def func_14_36A8():
    Sleep(1000)

    OP_8E(0x00FE, 55140, 0, 2620, 3000, 0x00)
    OP_8E(0x00FE, 57690, 0, 2620, 3000, 0x00)
    ChrTurnDirection(0x00FE, 0x000E, 400)

    Return()

# id: 0x0015 offset: 0x36DD
@scena.Code('func_15_36DD')
def func_15_36DD():
    SetChrPos(0x00FE, 125400, -2000, 4700, 270)
    OP_8E(0x00FE, 119700, 0, 4700, 3000, 0x00)
    OP_8E(0x00FE, 120350, 0, -150, 3000, 0x00)
    OP_8C(0x00FE, 180, 400)

    Return()

# id: 0x0016 offset: 0x371E
@scena.Code('func_16_371E')
def func_16_371E():
    SetChrPos(0x00FE, 125400, -2000, 4700, 270)
    OP_8E(0x00FE, 119700, 0, 4700, 3000, 0x00)
    OP_8E(0x00FE, 119240, 0, -180, 3000, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    Return()

# id: 0x0017 offset: 0x375F
@scena.Code('func_17_375F')
def func_17_375F():
    SetChrPos(0x00FE, 58740, -2000, 4560, 270)
    OP_8E(0x00FE, 54960, 0, 4880, 5000, 0x00)
    OP_8E(0x00FE, 54720, 0, 3650, 5000, 0x00)

    Return()

# id: 0x0018 offset: 0x3799
@scena.Code('func_18_3799')
def func_18_3799():
    OP_8E(0x00FE, 114650, 250, 560, 3000, 0x00)
    OP_8E(0x00FE, 117180, 0, -500, 3000, 0x00)
    OP_8C(0x00FE, 90, 500)

    Return()

# id: 0x0019 offset: 0x37C9
@scena.Code('func_19_37C9')
def func_19_37C9():
    OP_8E(0x00FE, 119220, 0, 1500, 2000, 0x00)

    @scena.Lambda('lambda_37E3')
    def lambda_37E3():
        OP_8C(0x00FE, 225, 400)
        Yield()

        Jump('lambda_37E3')

    DispatchAsync2(0x00FE, 0x0001, lambda_37E3)

    Return()

# id: 0x001A offset: 0x37EF
@scena.Code('func_1A_37EF')
def func_1A_37EF():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
        (0x00000000, 'loc_3869'),
        (0x00000001, 'loc_386F'),
        (-1, 'loc_3875'),
    )

    def _loc_3869(): pass

    label('loc_3869')

    OP_A2(0x1200)

    Jump('loc_3875')

    def _loc_386F(): pass

    label('loc_386F')

    OP_A2(0x1201)

    Jump('loc_3875')

    def _loc_3875(): pass

    label('loc_3875')

    Return()

# id: 0x001B offset: 0x3876
@scena.Code('func_1B_3876')
def func_1B_3876():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3887',
    )

    OP_2A(0x00BD, 0x00BE, 0xFFFF)

    Jump('loc_38D4')

    def _loc_3887(): pass

    label('loc_3887')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_389E',
    )

    OP_2A(0x00AA, 0x00AC, 0x00C4, 0x00AB, 0x00A9, 0xFFFF)

    Jump('loc_38D4')

    def _loc_389E(): pass

    label('loc_389E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_38B3',
    )

    OP_2A(0x00AA, 0x00AC, 0x00C4, 0x00AB, 0xFFFF)

    Jump('loc_38D4')

    def _loc_38B3(): pass

    label('loc_38B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_38C6',
    )

    OP_2A(0x00AA, 0x00AC, 0x00C4, 0xFFFF)

    Jump('loc_38D4')

    def _loc_38C6(): pass

    label('loc_38C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_38D4',
    )

    OP_2A(0x00AA, 0x00AC, 0xFFFF)

    def _loc_38D4(): pass

    label('loc_38D4')

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
