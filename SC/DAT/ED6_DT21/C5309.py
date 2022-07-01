import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5309_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5309   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '瘦狼瓦鲁特'),
    TXT(0x02, '瘦狼瓦鲁特'),
    TXT(0x03, '血狮'),
    TXT(0x04, '血狮'),
    TXT(0x05, '亡命装甲兵'),
    TXT(0x06, '幻惑之铃露茜奥拉'),
    TXT(0x07, '目标用照相机'),
    TXT(0x08, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5309.x'
    header.mapIndex       = 1
    header.bgm            = 64
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x6055
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
        ('ED6_DT26/CH20461._CH', 'ED6_DT26/CH20461P._CP'),
    ]

# id: 0x10002 offset: 0xB2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
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
            dword_10            = 0,
            chipIndex           = 0,
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
            dword_10            = 0,
            chipIndex           = 0,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
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
            dword_10            = 0,
            chipIndex           = 0,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x192
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x192
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x192
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -32500,
            triggerZ            = 0,
            triggerY            = 0,
            triggerRange        = 800,
            actorX              = -32500,
            actorZ              = 1000,
            actorY              = 0,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x001B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1B6
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 5, 0x2235)),
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 1, 0x2239)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_230',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -18090, 0, 3500, 180)
    ClearChrFlags(0x0008, 0x0001)
    SetChrFlags(0x0008, 0x0002)
    SetChrFlags(0x0008, 0x0010)
    SetChrChipByIndex(0x0008, 0)
    SetChrSubChip(0x0008, 23)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -17410, 0, 4440, 180)
    ClearChrFlags(0x0009, 0x0001)
    SetChrFlags(0x0009, 0x0002)
    SetChrFlags(0x0009, 0x0010)
    SetChrChipByIndex(0x0009, 0)
    SetChrSubChip(0x0009, 23)
    ClearChrFlags(0x0009, 0x0080)
    OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    def _loc_230(): pass

    label('loc_230')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_241',
    )

    OP_A3(0x10F0)
    Event(0, 0x001C)

    Jump('loc_28E')

    def _loc_241(): pass

    label('loc_241')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 4, 0x2234)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 5, 0x2235)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_28E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_26B',
    )

    Event(0, 0x001D)

    Jump('loc_28E')

    def _loc_26B(): pass

    label('loc_26B')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_285',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0006)

    Jump('loc_28E')

    def _loc_285(): pass

    label('loc_285')

    SetMapFlags(0x10000000)
    Event(0, 0x0014)

    def _loc_28E(): pass

    label('loc_28E')

    Return()

# id: 0x0001 offset: 0x28F
@scena.Code('Init')
def Init():
    OP_22(0x01C3, 0x01, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 6, 0x2236)),
            Expr.Return,
        ),
        'loc_2A4',
    )

    OP_64(0x00, 0x0001)
    OP_71(0x0001, 0x0004)

    def _loc_2A4(): pass

    label('loc_2A4')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x461),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D2',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C5',
    )

    Call(0, 0x0004)

    Jump('loc_2D2')

    def _loc_2C5(): pass

    label('loc_2C5')

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(0, 0x0005)

    def _loc_2D2(): pass

    label('loc_2D2')

    ExecExpressionWithValue(
        0x000A,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000B,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000C,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x317
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
        'loc_33C',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_47E')

    def _loc_33C(): pass

    label('loc_33C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_355',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_47E')

    def _loc_355(): pass

    label('loc_355')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36E',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_47E')

    def _loc_36E(): pass

    label('loc_36E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_387',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_47E')

    def _loc_387(): pass

    label('loc_387')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A0',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_47E')

    def _loc_3A0(): pass

    label('loc_3A0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B9',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_47E')

    def _loc_3B9(): pass

    label('loc_3B9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D2',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_47E')

    def _loc_3D2(): pass

    label('loc_3D2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3EB',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_47E')

    def _loc_3EB(): pass

    label('loc_3EB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_404',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_47E')

    def _loc_404(): pass

    label('loc_404')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_41D',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_47E')

    def _loc_41D(): pass

    label('loc_41D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_436',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_47E')

    def _loc_436(): pass

    label('loc_436')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_44F',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_47E')

    def _loc_44F(): pass

    label('loc_44F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_468',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_47E')

    def _loc_468(): pass

    label('loc_468')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_47E',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_47E(): pass

    label('loc_47E')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_493',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_47E')

    def _loc_493(): pass

    label('loc_493')

    Return()

# id: 0x0003 offset: 0x494
@scena.Code('func_03_494')
def func_03_494():
    TalkBegin(0x0008)

    ChrTalk(
        0x0008,
        (
            '#0200410380V#5P………………………………',
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
            '瓦鲁特力尽晕倒了。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x50B
@scena.Code('func_04_50B')
def func_04_50B():
    OP_D2(0x002701C6, 0x002701CB, 0x01)
    OP_D2(0x00290428, 0x0029042C, 0x02)
    OP_D2(0x00290429, 0x0029042D, 0x03)
    OP_D2(0x00290188, 0x0029018C, 0x04)
    OP_D2(0x00290189, 0x0029018D, 0x05)
    OP_D2(0x00270110, 0x00270120, 0x06)
    OP_D2(0x00270111, 0x00270121, 0x07)
    OP_D2(0x00270130, 0x00270140, 0x08)
    OP_D2(0x00270131, 0x00270141, 0x09)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_592'),
        (0x00000005, 'loc_5A9'),
        (0x00000003, 'loc_5C0'),
        (0x00000004, 'loc_5D7'),
        (0x00000006, 'loc_5EE'),
        (0x00000008, 'loc_605'),
        (0x0000000A, 'loc_61C'),
        (0x0000000E, 'loc_633'),
        (0x0000000F, 'loc_64A'),
        (-1, 'loc_661'),
    )

    def _loc_592(): pass

    label('loc_592')

    OP_D2(0x000701D0, 0x000701DC, 0x0A)
    OP_D2(0x000701D1, 0x000701DD, 0x0B)

    Jump('loc_661')

    def _loc_5A9(): pass

    label('loc_5A9')

    OP_D2(0x00070218, 0x00070224, 0x0A)
    OP_D2(0x00070219, 0x00070225, 0x0B)

    Jump('loc_661')

    def _loc_5C0(): pass

    label('loc_5C0')

    OP_D2(0x000701E8, 0x000701F4, 0x0A)
    OP_D2(0x000701E9, 0x000701F5, 0x0B)

    Jump('loc_661')

    def _loc_5D7(): pass

    label('loc_5D7')

    OP_D2(0x0027036E, 0x0027037B, 0x0A)
    OP_D2(0x0027036F, 0x0027037C, 0x0B)

    Jump('loc_661')

    def _loc_5EE(): pass

    label('loc_5EE')

    OP_D2(0x00070230, 0x0007023C, 0x0A)
    OP_D2(0x00070231, 0x0007023D, 0x0B)

    Jump('loc_661')

    def _loc_605(): pass

    label('loc_605')

    OP_D2(0x00270176, 0x00270183, 0x0A)
    OP_D2(0x00270177, 0x00270184, 0x0B)

    Jump('loc_661')

    def _loc_61C(): pass

    label('loc_61C')

    OP_D2(0x000702B4, 0x000702BB, 0x0A)
    OP_D2(0x000702B5, 0x000702BC, 0x0B)

    Jump('loc_661')

    def _loc_633(): pass

    label('loc_633')

    OP_D2(0x002702D6, 0x002702E0, 0x0A)
    OP_D2(0x002702D7, 0x002702E1, 0x0B)

    Jump('loc_661')

    def _loc_64A(): pass

    label('loc_64A')

    OP_D2(0x002702C2, 0x002702CC, 0x0A)
    OP_D2(0x002702C3, 0x002702CD, 0x0B)

    Jump('loc_661')

    def _loc_661(): pass

    label('loc_661')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_68E'),
        (0x00000005, 'loc_6A5'),
        (0x00000003, 'loc_6BC'),
        (0x00000004, 'loc_6D3'),
        (0x00000006, 'loc_6EA'),
        (0x00000008, 'loc_701'),
        (0x0000000A, 'loc_718'),
        (0x0000000E, 'loc_72F'),
        (0x0000000F, 'loc_746'),
        (-1, 'loc_75D'),
    )

    def _loc_68E(): pass

    label('loc_68E')

    OP_D2(0x000701D0, 0x000701DC, 0x0C)
    OP_D2(0x000701D1, 0x000701DD, 0x0D)

    Jump('loc_75D')

    def _loc_6A5(): pass

    label('loc_6A5')

    OP_D2(0x00070218, 0x00070224, 0x0C)
    OP_D2(0x00070219, 0x00070225, 0x0D)

    Jump('loc_75D')

    def _loc_6BC(): pass

    label('loc_6BC')

    OP_D2(0x000701E8, 0x000701F4, 0x0C)
    OP_D2(0x000701E9, 0x000701F5, 0x0D)

    Jump('loc_75D')

    def _loc_6D3(): pass

    label('loc_6D3')

    OP_D2(0x0027036E, 0x0027037B, 0x0C)
    OP_D2(0x0027036F, 0x0027037C, 0x0D)

    Jump('loc_75D')

    def _loc_6EA(): pass

    label('loc_6EA')

    OP_D2(0x00070230, 0x0007023C, 0x0C)
    OP_D2(0x00070231, 0x0007023D, 0x0D)

    Jump('loc_75D')

    def _loc_701(): pass

    label('loc_701')

    OP_D2(0x00270176, 0x00270183, 0x0C)
    OP_D2(0x00270177, 0x00270184, 0x0D)

    Jump('loc_75D')

    def _loc_718(): pass

    label('loc_718')

    OP_D2(0x000702B4, 0x000702BB, 0x0C)
    OP_D2(0x000702B5, 0x000702BC, 0x0D)

    Jump('loc_75D')

    def _loc_72F(): pass

    label('loc_72F')

    OP_D2(0x002702D6, 0x002702E0, 0x0C)
    OP_D2(0x002702D7, 0x002702E1, 0x0D)

    Jump('loc_75D')

    def _loc_746(): pass

    label('loc_746')

    OP_D2(0x002702C2, 0x002702CC, 0x0C)
    OP_D2(0x002702C3, 0x002702CD, 0x0D)

    Jump('loc_75D')

    def _loc_75D(): pass

    label('loc_75D')

    OP_D2(0x0027022A, 0x00270234, 0x0E)
    OP_D2(0x002600A0, 0x002600A5, 0x0F)
    OP_D2(0x00260052, 0x00260057, 0x10)
    OP_D2(0x002601C4, 0x002601C9, 0x11)

    Return()

# id: 0x0005 offset: 0x786
@scena.Code('func_05_786')
def func_05_786():
    OP_D2(0x002701C6, 0x002701CB, 0x01)
    OP_D2(0x00290428, 0x0029042C, 0x02)
    OP_D2(0x00290429, 0x0029042D, 0x03)
    OP_D2(0x00270110, 0x00270120, 0x04)
    OP_D2(0x00270111, 0x00270121, 0x05)
    OP_D2(0x00270130, 0x00270140, 0x06)
    OP_D2(0x00270131, 0x00270141, 0x07)

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7F1',
    )

    OP_D2(0x000701D0, 0x000701DC, 0x08)
    OP_D2(0x000701D1, 0x000701DD, 0x09)

    Jump('loc_916')

    def _loc_7F1(): pass

    label('loc_7F1')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_816',
    )

    OP_D2(0x00070218, 0x00070224, 0x08)
    OP_D2(0x00070219, 0x00070225, 0x09)

    Jump('loc_916')

    def _loc_816(): pass

    label('loc_816')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_83B',
    )

    OP_D2(0x000701E8, 0x000701F4, 0x08)
    OP_D2(0x000701E9, 0x000701F5, 0x09)

    Jump('loc_916')

    def _loc_83B(): pass

    label('loc_83B')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_860',
    )

    OP_D2(0x0027036E, 0x0027037B, 0x08)
    OP_D2(0x0027036F, 0x0027037C, 0x09)

    Jump('loc_916')

    def _loc_860(): pass

    label('loc_860')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_885',
    )

    OP_D2(0x00070230, 0x0007023C, 0x08)
    OP_D2(0x00070231, 0x0007023D, 0x09)

    Jump('loc_916')

    def _loc_885(): pass

    label('loc_885')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8AA',
    )

    OP_D2(0x00270176, 0x00270183, 0x08)
    OP_D2(0x00270177, 0x00270184, 0x09)

    Jump('loc_916')

    def _loc_8AA(): pass

    label('loc_8AA')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8CF',
    )

    OP_D2(0x000702B4, 0x000702BB, 0x08)
    OP_D2(0x000702B5, 0x000702BC, 0x09)

    Jump('loc_916')

    def _loc_8CF(): pass

    label('loc_8CF')

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8F4',
    )

    OP_D2(0x002702D6, 0x002702E0, 0x08)
    OP_D2(0x002702D7, 0x002702E1, 0x09)

    Jump('loc_916')

    def _loc_8F4(): pass

    label('loc_8F4')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_916',
    )

    OP_D2(0x002702C2, 0x002702CC, 0x08)
    OP_D2(0x002702C3, 0x002702CD, 0x09)

    def _loc_916(): pass

    label('loc_916')

    OP_D2(0x0007024A, 0x00070256, 0x0A)
    OP_D2(0x0007024C, 0x00070258, 0x0B)
    OP_D2(0x00070251, 0x0007025D, 0x0C)

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_94F',
    )

    OP_D2(0x000701D1, 0x000701DD, 0x0D)

    Jump('loc_A24')

    def _loc_94F(): pass

    label('loc_94F')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_96A',
    )

    OP_D2(0x00070219, 0x00070225, 0x0D)

    Jump('loc_A24')

    def _loc_96A(): pass

    label('loc_96A')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_985',
    )

    OP_D2(0x000701E9, 0x000701F5, 0x0D)

    Jump('loc_A24')

    def _loc_985(): pass

    label('loc_985')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9A0',
    )

    OP_D2(0x0027036F, 0x0027037C, 0x0D)

    Jump('loc_A24')

    def _loc_9A0(): pass

    label('loc_9A0')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9BB',
    )

    OP_D2(0x00070231, 0x0007023D, 0x0D)

    Jump('loc_A24')

    def _loc_9BB(): pass

    label('loc_9BB')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9D6',
    )

    OP_D2(0x00270177, 0x00270184, 0x0D)

    Jump('loc_A24')

    def _loc_9D6(): pass

    label('loc_9D6')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9F1',
    )

    OP_D2(0x000702B5, 0x000702BC, 0x0D)

    Jump('loc_A24')

    def _loc_9F1(): pass

    label('loc_9F1')

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A0C',
    )

    OP_D2(0x002702D7, 0x002702E1, 0x09)

    Jump('loc_A24')

    def _loc_A0C(): pass

    label('loc_A0C')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A24',
    )

    OP_D2(0x002702C3, 0x002702CD, 0x09)

    def _loc_A24(): pass

    label('loc_A24')

    OP_D2(0x0027022A, 0x00270234, 0x0E)
    OP_D2(0x002600A0, 0x002600A5, 0x0F)
    OP_D2(0x002601A7, 0x002601AC, 0x10)
    OP_D2(0x0027022C, 0x00270236, 0x11)
    OP_D2(0x002601C5, 0x002601CA, 0x12)
    OP_D2(0x00260052, 0x00260057, 0x13)
    OP_D2(0x00070249, 0x00070255, 0x14)
    OP_D2(0x00070248, 0x00070254, 0x15)

    Return()

# id: 0x0006 offset: 0xA75
@scena.Code('func_06_A75')
def func_06_A75():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    Call(0, 0x0004)
    OP_6D(18160, 0, 1020, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4590, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 23580, 0, -420, 270)
    SetChrPos(0x0102, 23550, 0, 850, 270)
    SetChrPos(0x00F8, 24710, 0, -660, 270)
    SetChrPos(0x00F9, 24630, 0, 720, 270)

    @scena.Lambda('lambda_0B0C')
    def lambda_0B0C():
        OP_6B(3960, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0B0C)

    @scena.Lambda('lambda_0B1C')
    def lambda_0B1C():
        OP_8E(0x00FE, 17750, 0, -420, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B1C)

    Sleep(80)

    @scena.Lambda('lambda_0B3C')
    def lambda_0B3C():
        OP_8E(0x00FE, 17580, 0, 850, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0B3C)

    Sleep(100)

    @scena.Lambda('lambda_0B5C')
    def lambda_0B5C():
        OP_8E(0x00FE, 19050, 0, -660, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0B5C)

    Sleep(150)

    @scena.Lambda('lambda_0B7C')
    def lambda_0B7C():
        OP_8E(0x00FE, 18880, 0, 720, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0B7C)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    SetChrChipByIndex(0x0008, 15)
    SetChrPos(0x0008, -18090, 0, 240, 90)
    ClearChrFlags(0x0008, 0x0080)

    NpcTalk(
        0x0008,
        '男人的声音',
        (
            '#0200410168V……怎么是你们几个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000001F4)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C54',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_C92')

    def _loc_C54(): pass

    label('loc_C54')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_C7B',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_C92')

    def _loc_C7B(): pass

    label('loc_C7B')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_C92(): pass

    label('loc_C92')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CBE',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_CFC')

    def _loc_CBE(): pass

    label('loc_CBE')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_CE5',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_CFC')

    def _loc_CE5(): pass

    label('loc_CE5')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_CFC(): pass

    label('loc_CFC')

    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D3D',
    )

    ChrTalk(
        0x0110,
        (
            '#0110410169V#270F<FIXME>むっ…………！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D3D(): pass

    label('loc_D3D')

    OP_1D(0x6F)
    Sleep(500)

    @scena.Lambda('lambda_0D4A')
    def lambda_0D4A():
        OP_6D(-18810, 0, 1110, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0D4A)

    @scena.Lambda('lambda_0D62')
    def lambda_0D62():
        OP_67(0, 5310, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0D62)

    @scena.Lambda('lambda_0D7A')
    def lambda_0D7A():
        OP_6B(3430, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0D7A)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010410170V#1005F#1P『瘦狼』！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0DB9')
    def lambda_0DB9():
        OP_8E(0x00FE, -8980, 0, -450, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0DB9)

    @scena.Lambda('lambda_0DD4')
    def lambda_0DD4():
        OP_6D(-14650, 0, 2440, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0DD4)

    @scena.Lambda('lambda_0DEC')
    def lambda_0DEC():
        OP_67(0, 3910, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0DEC)

    @scena.Lambda('lambda_0E04')
    def lambda_0E04():
        OP_6B(3680, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0E04)

    @scena.Lambda('lambda_0E14')
    def lambda_0E14():
        OP_6E(311, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0E14)

    Sleep(300)

    @scena.Lambda('lambda_0E29')
    def lambda_0E29():
        OP_8E(0x00FE, -8830, 0, 790, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0E29)

    Sleep(100)

    @scena.Lambda('lambda_0E49')
    def lambda_0E49():
        OP_8E(0x00FE, -7060, 0, -1100, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0E49)

    Sleep(300)

    OP_8E(0x00F9, -7100, 0, 370, 6000, 0x00)
    WaitForThreadExit(0x0102, 0x0002)
    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x0101, 6)
    SetChrChipByIndex(0x0102, 8)
    SetChrChipByIndex(0x00F8, 10)
    SetChrChipByIndex(0x00F9, 12)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020410171V#1042F#6P瓦鲁特……\n',
            '你是第二道障碍吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200410172V#254F#5P哼……\n',
            '那种无聊事随你怎么说都好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410173V臭小子，我问你……\n',
            '金那个混蛋为什么没来？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410174V#1035F#6P很遗憾，他现在\n',
            '正在『埃尔赛尤』待命。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410175V#1042F你要是以为他一定会来的话，\n',
            '那就只能失望了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200410176V#254F#5P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410177V#1015F#6P啊，那个……\n',
            '有需要的话也可以帮你传个话哦～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410178V给雾香小姐也行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200410179V#250F#5P啧……臭小鬼，\n',
            '别多管闲事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410180V唉，那个蠢大个子竟然没来，\n',
            '生闷气也没用了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410181V还是赶快清理掉你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410182V#1002F#6P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Sleep(200)

    ClearChrFlags(0x0008, 0x0002)
    SetChrChipByIndex(0x0008, 15)
    SetChrSubChip(0x0008, 0)
    Sleep(200)

    OP_99(0x0008, 0x01, 0x02, 0x000003E8)
    OP_22(0x00BC, 0x00, 0x64)
    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0800)
    SetChrFlags(0x000A, 0x0004)
    SetChrChipByIndex(0x000A, 2)
    SetChrPos(0x000A, -33300, 6900, 2900, 90)
    CreateThread(0x000A, 0x03, 0x00, 0x0002)
    ClearChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000B, 0x0800)
    SetChrFlags(0x000B, 0x0004)
    SetChrChipByIndex(0x000B, 2)
    SetChrPos(0x000B, -33300, 6900, -2900, 90)
    CreateThread(0x000B, 0x03, 0x00, 0x0002)

    @scena.Lambda('lambda_119E')
    def lambda_119E():
        OP_6D(-31560, 5700, 0, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_119E)

    @scena.Lambda('lambda_11B6')
    def lambda_11B6():
        OP_67(0, 6700, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_11B6)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    SetChrPos(0x0101, -9130, 0, -310, 270)
    SetChrPos(0x0102, -9130, 0, 1050, 270)
    SetChrPos(0x00F8, -6990, 0, -720, 270)
    SetChrPos(0x00F9, -6990, 0, 1490, 270)
    SetChrChipByIndex(0x0008, 15)
    SetChrSubChip(0x0008, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x00000010)
    CreateThread(0x000A, 0x00, 0x00, 0x0009)
    Sleep(100)

    @scena.Lambda('lambda_1240')
    def lambda_1240():
        OP_6D(-13900, 500, 410, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1240)

    @scena.Lambda('lambda_1258')
    def lambda_1258():
        OP_67(0, 3000, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1258)

    @scena.Lambda('lambda_1270')
    def lambda_1270():
        OP_6E(288, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1270)

    @scena.Lambda('lambda_1280')
    def lambda_1280():
        OP_6B(3670, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_1280)

    Sleep(100)

    CreateThread(0x000B, 0x00, 0x00, 0x000A)
    WaitForThreadExit(0x000A, 0x0000)
    WaitForThreadExit(0x000B, 0x0000)
    Fade(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x00000010)

    @scena.Lambda('lambda_12B9')
    def lambda_12B9():
        OP_6C(270000, 0)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_12B9)

    OP_71(0x0000, 0x0004)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0200410183V#252F#5P来吧，小鬼们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410184V你们就代替金\n',
            '让我好好享受一番吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_132D')
    def lambda_132D():
        OP_6D(-13930, 500, 410, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_132D)

    @scena.Lambda('lambda_1345')
    def lambda_1345():
        OP_67(0, 2800, -10000, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1345)

    @scena.Lambda('lambda_135D')
    def lambda_135D():
        OP_6B(3000, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_135D)

    SetChrFlags(0x0008, 0x0020)
    SetChrSubChip(0x0008, 2)
    SetChrChipByIndex(0x0008, 16)

    @scena.Lambda('lambda_137C')
    def lambda_137C():
        OP_96(0x00FE, 0xFFFFD120, 0x00000000, 0x0000015E, 0x000005DC, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_137C)

    Sleep(30)

    TerminateThread(0x000A, 0x03)
    SetChrChipByIndex(0x000A, 3)
    SetChrSubChip(0x000A, 0)
    SetChrFlags(0x000A, 0x0020)
    SetChrFlags(0x000A, 0x1000)

    @scena.Lambda('lambda_13B7')
    def lambda_13B7():
        OP_99(0x00FE, 0x00, 0x06, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_13B7)

    @scena.Lambda('lambda_13C7')
    def lambda_13C7():
        OP_91(0x00FE, 5000, 0, 2000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_13C7)

    @scena.Lambda('lambda_13E2')
    def lambda_13E2():
        OP_91(0x00FE, -5000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_13E2)

    @scena.Lambda('lambda_13FD')
    def lambda_13FD():
        OP_91(0x00FE, -5000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_13FD)

    Sleep(30)

    TerminateThread(0x000B, 0x03)
    SetChrChipByIndex(0x000B, 3)
    SetChrSubChip(0x000B, 0)
    SetChrFlags(0x000B, 0x0020)
    SetChrFlags(0x000B, 0x1000)

    @scena.Lambda('lambda_1435')
    def lambda_1435():
        OP_99(0x00FE, 0x00, 0x06, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1435)

    @scena.Lambda('lambda_1445')
    def lambda_1445():
        OP_91(0x00FE, 5000, 0, -2000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_1445)

    @scena.Lambda('lambda_1460')
    def lambda_1460():
        OP_91(0x00FE, -5000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_1460)

    @scena.Lambda('lambda_147B')
    def lambda_147B():
        OP_91(0x00FE, -5000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_147B)

    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x00F8, 0xFF)
    TerminateThread(0x00F9, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    Battle(0x00000461, 0x00000000, 0x00, 0x0000, 0xFF)
    Call(0, 0x000B)

    Return()

# id: 0x0007 offset: 0x14C3
@scena.Code('func_07_14C3')
def func_07_14C3():
    SetChrFlags(0x00FE, 0x0004)
    SetChrChipByIndex(0x00FE, 2)
    SetChrPos(0x00FE, -18950, 1800, -1850, 90)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_14F4')
    def lambda_14F4():
        OP_99(0x00FE, 0x00, 0x07, 0x000005DC)
        Yield()

        Jump('lambda_14F4')

    DispatchAsync2(0x00FE, 0x0001, lambda_14F4)

    @scena.Lambda('lambda_1507')
    def lambda_1507():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1507)

    @scena.Lambda('lambda_1519')
    def lambda_1519():
        OP_8F(0x00FE, -18950, 500, -1850, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1519)

    OP_22(0x0099, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0003)
    OP_22(0x00A4, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0002)

    Return()

# id: 0x0008 offset: 0x1543
@scena.Code('func_08_1543')
def func_08_1543():
    SetChrFlags(0x00FE, 0x0004)
    SetChrChipByIndex(0x00FE, 2)
    SetChrPos(0x00FE, -18950, 1800, 1850, 90)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ClearChrFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_1574')
    def lambda_1574():
        OP_99(0x00FE, 0x00, 0x07, 0x000005DC)
        Yield()

        Jump('lambda_1574')

    DispatchAsync2(0x00FE, 0x0001, lambda_1574)

    @scena.Lambda('lambda_1587')
    def lambda_1587():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1587)

    @scena.Lambda('lambda_1599')
    def lambda_1599():
        OP_8F(0x00FE, -18950, 500, 1850, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1599)

    OP_22(0x0099, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0003)
    OP_22(0x00A4, 0x00, 0x64)
    WaitForThreadExit(0x00FE, 0x0002)

    Return()

# id: 0x0009 offset: 0x15C3
@scena.Code('func_09_15C3')
def func_09_15C3():
    TerminateThread(0x00FE, 0x03)
    SetChrChipByIndex(0x00FE, 3)
    SetChrSubChip(0x00FE, 5)
    OP_8C(0x00FE, 135, 0)
    ClearChrFlags(0x00FE, 0x0800)
    OP_22(0x00A3, 0x00, 0x64)

    @scena.Lambda('lambda_15E8')
    def lambda_15E8():
        OP_99(0x00FE, 0x05, 0x07, 0x00000258)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_15E8)

    @scena.Lambda('lambda_15F8')
    def lambda_15F8():
        OP_96(0x00FE, 0xFFFFAD6C, 0x00000000, 0xFFFFEB4C, 0x000001F4, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_15F8)

    WaitForThreadExit(0x00FE, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    OP_8C(0x00FE, 45, 0)

    @scena.Lambda('lambda_1627')
    def lambda_1627():
        OP_99(0x00FE, 0x05, 0x07, 0x00000320)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1627)

    @scena.Lambda('lambda_1637')
    def lambda_1637():
        OP_96(0x00FE, 0xFFFFBF28, 0x00000000, 0xFFFFF2CC, 0x000003E8, 0x00000DAC)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_1637)

    WaitForThreadExit(0x00FE, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x00FE, 2)
    SetChrSubChip(0x00FE, 0)
    CreateThread(0x00FE, 0x03, 0x00, 0x0002)
    SetChrFlags(0x00FE, 0x0800)

    Return()

# id: 0x000A offset: 0x1670
@scena.Code('func_0A_1670')
def func_0A_1670():
    TerminateThread(0x00FE, 0x03)
    SetChrChipByIndex(0x00FE, 3)
    SetChrSubChip(0x00FE, 5)
    OP_8C(0x00FE, 45, 0)
    ClearChrFlags(0x00FE, 0x0800)
    OP_22(0x00A3, 0x00, 0x64)

    @scena.Lambda('lambda_1695')
    def lambda_1695():
        OP_99(0x00FE, 0x05, 0x07, 0x00000258)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_1695)

    @scena.Lambda('lambda_16A5')
    def lambda_16A5():
        OP_96(0x00FE, 0xFFFFAD6C, 0x00000000, 0x00001694, 0x000001F4, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_16A5)

    WaitForThreadExit(0x00FE, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    OP_8C(0x00FE, 135, 0)

    @scena.Lambda('lambda_16D4')
    def lambda_16D4():
        OP_99(0x00FE, 0x05, 0x07, 0x00000320)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_16D4)

    @scena.Lambda('lambda_16E4')
    def lambda_16E4():
        OP_96(0x00FE, 0xFFFFBF28, 0x00000000, 0x00000F14, 0x000003E8, 0x00000DAC)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_16E4)

    WaitForThreadExit(0x00FE, 0x0001)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x00FE, 2)
    SetChrSubChip(0x00FE, 0)
    CreateThread(0x00FE, 0x03, 0x00, 0x0002)
    SetChrFlags(0x00FE, 0x0800)

    Return()

# id: 0x000B offset: 0x171D
@scena.Code('func_0B_171D')
def func_0B_171D():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x000A, 0x00)
    TerminateThread(0x000B, 0x00)
    TerminateThread(0x0008, 0x00)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0102, 0x00)
    TerminateThread(0x00F8, 0x00)
    TerminateThread(0x00F9, 0x00)
    Call(0, 0x0004)
    OP_6D(-12230, 0, 1670, 0)
    OP_67(0, 4280, -10000, 0)
    OP_6B(4370, 0)
    SetChrPos(0x0101, -13600, 0, -1360, 270)
    SetChrPos(0x0102, -13600, 0, -110, 270)
    SetChrPos(0x00F8, -12000, 0, -1880, 270)
    SetChrPos(0x00F9, -12050, 0, -450, 270)
    SetChrChipByIndex(0x0101, 6)
    SetChrChipByIndex(0x0102, 8)
    SetChrChipByIndex(0x00F8, 10)
    SetChrChipByIndex(0x00F9, 12)
    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)
    SetChrSubChip(0x0002, 0)
    SetChrSubChip(0x0003, 0)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 15)
    SetChrPos(0x0008, -21340, 0, 140, 90)
    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    OP_72(0x0000, 0x0004)
    OP_6D(-18640, 0, 1580, 0)
    OP_67(0, 3710, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(379, 0)
    FadeIn(1000, 0)
    OP_6B(2800, 2000)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0200410203V#254F#5P……啧…………\n',
            '烦人的小鬼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410204V#1019F#6P我，我说……\n',
            '别老是小鬼小鬼的叫啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_194A',
    )

    ChrTalk(
        0x0110,
        (
            '#0110410205V#277F<FIXME>フッ……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110410206Vそのガキとやらの一撃に\n',
            '膝を付いたのはどこの誰だ？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CC5')

    def _loc_194A(): pass

    label('loc_194A')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19AC',
    )

    ChrTalk(
        0x0106,
        (
            '#0050410207V#051F#4P嘿……大叔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050410208V你的脚步好像\n',
            '有点站不稳了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CC5')

    def _loc_19AC(): pass

    label('loc_19AC')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A45',
    )

    ChrTalk(
        0x010B,
        (
            '#0090410209V#210F#4P的确，像小鬼的家伙\n',
            '大概也就一个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090410210V可别把我也混为一谈哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410211V#1022F#5P你，你啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CC5')

    def _loc_1A45(): pass

    label('loc_1A45')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1ACD',
    )

    ChrTalk(
        0x0109,
        (
            '#0180410212V#1066F#4P算了算了，艾丝蒂尔。\n',
            '别发那么大火嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180410213V只不过是年近中年的\n',
            '大叔说些讨厌的话罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CC5')

    def _loc_1ACD(): pass

    label('loc_1ACD')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B4D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040410214V#035F#4P呼，艾丝蒂尔。\n',
            '就原谅他吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040410215V#030F只不过是更年期的男人\n',
            '逞些口舌之能罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CC5')

    def _loc_1B4D(): pass

    label('loc_1B4D')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BCD',
    )

    ChrTalk(
        0x0105,
        (
            '#0060410216V#1162F#4P的确，我可能\n',
            '还不成熟……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060410217V但是，想守护自己\n',
            '所珍视之物的心情却是真实的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CC5')

    def _loc_1BCD(): pass

    label('loc_1BCD')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C41',
    )

    ChrTalk(
        0x0103,
        (
            '#0030410218V#027F#4P算了算了，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410219V只不过是更年期的\n',
            '大叔说些讨厌的话而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CC5')

    def _loc_1C41(): pass

    label('loc_1C41')

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1CC5',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410220V#176F<FIXME>……勝機は我らにある。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100410221V#178F観念してもらおうか、\n',
            '《痩せ狼》ヴァルター……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CC5(): pass

    label('loc_1CC5')

    ChrTalk(
        0x0008,
        (
            '#0200410222V#254F#5P啧……胡说八道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410223V#1035F#4P……瓦鲁特。\n',
            '你并没有同我们死缠到底的必要，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410224V#1042F但是我们……\n',
            '却有必须前进的理由。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410225V即使如此，还是要战下去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410226V#1026F#6P约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200410227V#254F#5P…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410228V#251F哼……真让人扫兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0008, 0)
    SetChrSubChip(0x0008, 1)
    Sleep(500)

    SetChrSubChip(0x0008, 2)
    OP_22(0x00BC, 0x00, 0x64)
    Sleep(500)

    SetChrSubChip(0x0008, 0)
    OP_22(0x0077, 0x00, 0x64)
    OP_22(0x0135, 0x00, 0x64)

    @scena.Lambda('lambda_1E45')
    def lambda_1E45():
        OP_6D(-18010, 0, 6140, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1E45)

    @scena.Lambda('lambda_1E5D')
    def lambda_1E5D():
        OP_67(0, 6340, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1E5D)

    @scena.Lambda('lambda_1E75')
    def lambda_1E75():
        OP_6B(5850, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1E75)

    @scena.Lambda('lambda_1E85')
    def lambda_1E85():
        OP_6E(307, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1E85)

    SetChrChipByIndex(0x000C, 4)
    SetChrPos(0x000C, -45090, 10000, 240, 90)
    ClearChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000C, 0x0020)
    CreateThread(0x000C, 0x01, 0x00, 0x000E)
    OP_8E(0x000C, -22090, 8000, 240, 6000, 0x00)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F29',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_1F67')

    def _loc_1F29(): pass

    label('loc_1F29')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F50',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_1F67')

    def _loc_1F50(): pass

    label('loc_1F50')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_1F67(): pass

    label('loc_1F67')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F93',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_1FD1')

    def _loc_1F93(): pass

    label('loc_1F93')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1FBA',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_1FD1')

    def _loc_1FBA(): pass

    label('loc_1FBA')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_1FD1(): pass

    label('loc_1FD1')

    Sleep(1000)

    SetChrFlags(0x0008, 0x0004)
    SetChrChipByIndex(0x0008, 16)
    SetChrSubChip(0x0008, 1)
    Sleep(500)

    SetChrSubChip(0x0008, 0)
    OP_7D(0x00, 0x0008, 0x0032, 0x01F4)
    OP_96(0x0008, 0xFFFFA9B6, 0x0000157C, 0xFFFFFEAC, 0x00001770, 0x00000FA0)
    OP_7D(0x01, 0x0008, 0x0000, 0x0000)
    SetChrSubChip(0x0008, 1)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 17)
    Fade(500)
    OP_6D(-34060, 1610, 7700, 0)
    OP_67(0, 3300, -10000, 0)
    OP_6B(4530, 0)
    OP_6C(302000, 0)
    OP_6E(350, 0)
    OP_6D(-30430, 0, 9320, 0)
    OP_67(0, 5100, -10000, 0)
    OP_6B(4530, 0)
    OP_6C(315000, 0)
    OP_6E(350, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010410229V#1020F#1P慢、慢着！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200410230V#257F#6P……去告诉金。\n',
            '我和他的胜负留到下次再分。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410231V#253F走了，小鬼们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410232V可别被『白面』吃掉啊，\n',
            '多多注意吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_216C')
    def lambda_216C():
        OP_6D(-17240, 5430, 12640, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_216C)

    @scena.Lambda('lambda_2184')
    def lambda_2184():
        OP_67(0, 5540, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2184)

    @scena.Lambda('lambda_219C')
    def lambda_219C():
        OP_6B(4000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_219C)

    @scena.Lambda('lambda_21AC')
    def lambda_21AC():
        OP_6E(274, 5000)

        ExitThread()

    DispatchAsync(0x00F8, 0x0003, lambda_21AC)

    SetChrFlags(0x0008, 0x0020)

    @scena.Lambda('lambda_21C1')
    def lambda_21C1():
        OP_97(0x000C, 0xFFFFABFA, 0x00001090, 0xFFFEA070, 0x00001770, 0x0001)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_21C1)

    OP_97(0x0008, 0xFFFFABFA, 0x00001090, 0xFFFEA070, 0x00001964, 0x0001)
    WaitForThreadExit(0x000C, 0x0000)
    CreateThread(0x0008, 0x01, 0x00, 0x000F)
    Sleep(1000)

    CreateThread(0x0008, 0x03, 0x00, 0x000C)
    CreateThread(0x0102, 0x01, 0x00, 0x0011)
    Sleep(100)

    CreateThread(0x0101, 0x01, 0x00, 0x0010)
    Sleep(100)

    CreateThread(0x00F8, 0x01, 0x00, 0x0012)
    Sleep(100)

    CreateThread(0x00F9, 0x01, 0x00, 0x0013)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    OP_6D(-18270, 0, 13050, 0)
    OP_67(0, 6140, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x00F8, 65535)
    SetChrChipByIndex(0x00F9, 65535)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010410233V#1015F#6P……走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020410234V#1035F大概是明白没有机会\n',
            '和金先生进行对决了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410235V#1040F和『怪盗绅士』一样，\n',
            '这次看来是完全收手了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010410236V#1025F#5P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2544',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410237V#175F<FIXME>……王都襲撃の罪、ここで\n',
            '償#2Rつぐな#ってもらうつもりだったが……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x010F, 400)

    ChrTalk(
        0x0101,
        (
            '#0010410238V#4P#1002F確かに、クローゼや\n',
            '女王陛下も危なかったし……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410239V#1003F……でも本当に\n',
            '罪を償#2Rつぐな#うべきなのは、\n',
            'あの教授だと思う。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410240V執行者のメンバーは\n',
            '教授の要請に応じた\n',
            'だけみたいだから……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x010F, 0x0101, 400)

    ChrTalk(
        0x010F,
        (
            '#0100410241V#176Fそうか……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100410242V#178F納得できた訳ではないが、\n',
            '今は不問としておこう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ABC')

    def _loc_2544(): pass

    label('loc_2544')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25CF',
    )

    ChrTalk(
        0x0107,
        (
            '#0070410243V#067F嘿嘿，太好了。\n',
            '不用和他打下去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_25A5',
    )

    ChrTurnDirection(0x0101, 0x0107, 400)
    Sleep(300)

    def _loc_25A5(): pass

    label('loc_25A5')

    ChrTalk(
        0x0101,
        (
            '#0010410244V#1016F#5P嗯……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ABC')

    def _loc_25CF(): pass

    label('loc_25CF')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26AA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050410245V#053F确实，既然时机未到，\n',
            '那也只能留待到下次了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050410246V#552F只不过，下次再碰面的话，\n',
            '就绝对免不了要做个了断了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2680',
    )

    ChrTurnDirection(0x0101, 0x0106, 400)
    Sleep(300)

    def _loc_2680(): pass

    label('loc_2680')

    ChrTalk(
        0x0101,
        (
            '#0010410247V#1003F#5P嗯……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ABC')

    def _loc_26AA(): pass

    label('loc_26AA')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_277D',
    )

    ChrTalk(
        0x0103,
        (
            '#0030410248V#026F既然时机未到，\n',
            '也只能继续等待下去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410249V#022F只不过，下次再碰头的话\n',
            '就绝对免不了要做个了断了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2753',
    )

    ChrTurnDirection(0x0101, 0x0103, 400)
    Sleep(300)

    def _loc_2753(): pass

    label('loc_2753')

    ChrTalk(
        0x0101,
        (
            '#0010410250V#1003F#5P嗯……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ABC')

    def _loc_277D(): pass

    label('loc_277D')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_283C',
    )

    ChrTalk(
        0x0105,
        (
            '#0060410251V#1167F既然因缘未尽，决斗\n',
            '总是不可避免的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060410252V#1168F至少现在\n',
            '不用决战，真是万幸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2812',
    )

    ChrTurnDirection(0x0101, 0x0105, 400)
    Sleep(300)

    def _loc_2812(): pass

    label('loc_2812')

    ChrTalk(
        0x0101,
        (
            '#0010410244V#1016F#5P嗯……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ABC')

    def _loc_283C(): pass

    label('loc_283C')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_295F',
    )

    ChrTalk(
        0x0104,
        (
            '#0040410254V#034F哎呀呀，真想看看他和金先生\n',
            '一决胜负啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040410255V#030F不过，就期待\n',
            '下次机会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_28CF',
    )

    ChrTurnDirection(0x0101, 0x0104, 400)
    Sleep(300)

    def _loc_28CF(): pass

    label('loc_28CF')

    ChrTalk(
        0x0101,
        (
            '#0010410256V#1004F#5P下次机会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410257V#1019F这件事结束之后\n',
            '你就要变回皇子殿下了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040410258V#031F哎呀，你在说什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ABC')

    def _loc_295F(): pass

    label('loc_295F')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2A30',
    )

    ChrTalk(
        0x0109,
        (
            '#0180410259V#1062F不过，为了一个女人，\n',
            '两个男人之间展开热战……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180410260V#1061F真是浪漫呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29EB',
    )

    ChrTurnDirection(0x0101, 0x0109, 400)
    Sleep(300)

    def _loc_29EB(): pass

    label('loc_29EB')

    ChrTalk(
        0x0101,
        (
            '#0010410261V#1016F#5P嗯～虽说和雾香小姐\n',
            '好像没有直接关系……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2ABC')

    def _loc_2A30(): pass

    label('loc_2A30')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2ABC',
    )

    ChrTalk(
        0x0110,
        (
            '#0110410262V#272F<FIXME>（……相当の使い手だったな。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110410263V#276F（差しの勝負なら\n',
            '  俺も危なかったかも知れん。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2ABC(): pass

    label('loc_2ABC')

    ChrTalk(
        0x0102,
        (
            '#0020410264V#1040F……不过，这下总算\n',
            '可以继续前进了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410265V赶快启动那里的终端\n',
            '解除锁定吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010410266V#1006F#5P嗯，就这么办！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x2234)
    OP_28(0x009F, 0x01, 0x0010)
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x2B60
@scena.Code('func_0C_2B60')
def func_0C_2B60():
    Sleep(400)

    OP_24(0x0077, 0x5F)
    OP_24(0x0135, 0x5F)
    Sleep(400)

    OP_24(0x0077, 0x5A)
    OP_24(0x0135, 0x5A)
    Sleep(400)

    OP_24(0x0077, 0x55)
    OP_24(0x0135, 0x55)
    Sleep(400)

    OP_24(0x0077, 0x50)
    OP_24(0x0135, 0x50)
    Sleep(400)

    OP_24(0x0077, 0x4B)
    OP_24(0x0135, 0x4B)
    Sleep(400)

    OP_24(0x0077, 0x46)
    OP_24(0x0135, 0x46)
    Sleep(400)

    OP_24(0x0077, 0x3C)
    OP_24(0x0135, 0x3C)
    Sleep(400)

    OP_24(0x0077, 0x32)
    OP_24(0x0135, 0x32)
    Sleep(400)

    OP_24(0x0077, 0x28)
    OP_24(0x0135, 0x28)
    Sleep(400)

    OP_24(0x0077, 0x1E)
    OP_24(0x0135, 0x1E)
    Sleep(400)

    OP_23(0x0077)
    OP_23(0x0135)

    Return()

# id: 0x000D offset: 0x2BEE
@scena.Code('func_0D_2BEE')
def func_0D_2BEE():
    @scena.Lambda('lambda_2BF4')
    def lambda_2BF4():
        OP_8E(0x00FE, 17750, 0, -420, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2BF4)

    Sleep(80)

    @scena.Lambda('lambda_2C14')
    def lambda_2C14():
        OP_8E(0x00FE, 17580, 0, 850, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2C14)

    Sleep(100)

    @scena.Lambda('lambda_2C34')
    def lambda_2C34():
        OP_8E(0x00FE, 19050, 0, -660, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_2C34)

    Sleep(150)

    OP_8E(0x00F9, 18880, 0, 720, 3000, 0x00)

    Return()

# id: 0x000E offset: 0x2C63
@scena.Code('func_0E_2C63')
def func_0E_2C63():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2C78',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('func_0E_2C63')

    def _loc_2C78(): pass

    label('loc_2C78')

    Return()

# id: 0x000F offset: 0x2C79
@scena.Code('func_0F_2C79')
def func_0F_2C79():
    @scena.Lambda('lambda_2C7F')
    def lambda_2C7F():
        OP_91(0x00FE, 0, 0, 50000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2C7F)

    @scena.Lambda('lambda_2C9A')
    def lambda_2C9A():
        OP_91(0x00FE, 0, 0, 50000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_2C9A)

    Sleep(500)

    @scena.Lambda('lambda_2CBA')
    def lambda_2CBA():
        OP_91(0x00FE, 0, 0, 50000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2CBA)

    @scena.Lambda('lambda_2CD5')
    def lambda_2CD5():
        OP_91(0x00FE, 0, 0, 50000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_2CD5)

    Sleep(500)

    @scena.Lambda('lambda_2CF5')
    def lambda_2CF5():
        OP_91(0x00FE, 0, 0, 50000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2CF5)

    @scena.Lambda('lambda_2D10')
    def lambda_2D10():
        OP_91(0x00FE, 0, 0, 50000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_2D10)

    Sleep(400)

    @scena.Lambda('lambda_2D30')
    def lambda_2D30():
        OP_91(0x00FE, 0, 0, 50000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2D30)

    @scena.Lambda('lambda_2D4B')
    def lambda_2D4B():
        OP_91(0x00FE, 0, 0, 50000, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_2D4B)

    Sleep(300)

    ClearChrFlags(0x000C, 0x0001)
    ClearChrFlags(0x0008, 0x0001)

    @scena.Lambda('lambda_2D75')
    def lambda_2D75():
        OP_91(0x00FE, 0, 0, 50000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2D75)

    @scena.Lambda('lambda_2D90')
    def lambda_2D90():
        OP_91(0x00FE, 0, 0, 50000, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_2D90)

    Sleep(200)

    @scena.Lambda('lambda_2DB0')
    def lambda_2DB0():
        OP_91(0x00FE, 0, 0, 50000, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2DB0)

    @scena.Lambda('lambda_2DCB')
    def lambda_2DCB():
        OP_91(0x00FE, 0, 0, 50000, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_2DCB)

    Sleep(100)

    @scena.Lambda('lambda_2DEB')
    def lambda_2DEB():
        OP_91(0x00FE, 0, 0, 50000, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2DEB)

    @scena.Lambda('lambda_2E06')
    def lambda_2E06():
        OP_91(0x00FE, 0, 0, 50000, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_2E06)

    Sleep(100)

    @scena.Lambda('lambda_2E26')
    def lambda_2E26():
        OP_91(0x00FE, 0, 0, 50000, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2E26)

    @scena.Lambda('lambda_2E41')
    def lambda_2E41():
        OP_91(0x00FE, 0, 0, 50000, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_2E41)

    Return()

# id: 0x0010 offset: 0x2E57
@scena.Code('func_10_2E57')
def func_10_2E57():
    OP_8E(0x00FE, -18690, 0, 12600, 6000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0011 offset: 0x2E73
@scena.Code('func_11_2E73')
def func_11_2E73():
    OP_8E(0x00FE, -17510, 0, 12820, 6000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0012 offset: 0x2E8F
@scena.Code('func_12_2E8F')
def func_12_2E8F():
    OP_8E(0x00FE, -18390, 0, 11100, 6000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0013 offset: 0x2EAB
@scena.Code('func_13_2EAB')
def func_13_2EAB():
    OP_8E(0x00FE, -16880, 0, 11170, 6000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0014 offset: 0x2EC7
@scena.Code('func_14_2EC7')
def func_14_2EC7():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    Call(0, 0x0005)
    OP_6D(18160, 0, 1020, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4590, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 23580, 0, -420, 270)
    SetChrPos(0x0102, 23550, 0, 850, 270)
    SetChrPos(0x00F8, 24710, 0, -660, 270)
    SetChrPos(0x00F9, 24630, 0, 720, 270)

    @scena.Lambda('lambda_2F5E')
    def lambda_2F5E():
        OP_6B(3960, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2F5E)

    @scena.Lambda('lambda_2F6E')
    def lambda_2F6E():
        OP_8E(0x00FE, 17750, 0, -420, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2F6E)

    Sleep(80)

    @scena.Lambda('lambda_2F8E')
    def lambda_2F8E():
        OP_8E(0x00FE, 17580, 0, 850, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2F8E)

    Sleep(100)

    @scena.Lambda('lambda_2FAE')
    def lambda_2FAE():
        OP_8E(0x00FE, 19050, 0, -660, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_2FAE)

    Sleep(150)

    @scena.Lambda('lambda_2FCE')
    def lambda_2FCE():
        OP_8E(0x00FE, 18880, 0, 720, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2FCE)

    FadeIn(1000, 0)
    WaitForThreadExit(0x00F9, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    SetChrChipByIndex(0x0008, 15)
    SetChrPos(0x0008, -18090, 0, 240, 90)
    ClearChrFlags(0x0008, 0x0080)

    NpcTalk(
        0x0008,
        '男人的声音',
        (
            '#0200410185V呼呼……\n',
            '我都等得不耐烦啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000001F4)
    OP_62(0x0108, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3117',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_30D6',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_3114')

    def _loc_30D6(): pass

    label('loc_30D6')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_30FD',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_3114')

    def _loc_30FD(): pass

    label('loc_30FD')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_3114(): pass

    label('loc_3114')

    Jump('loc_317C')

    def _loc_3117(): pass

    label('loc_3117')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_313E',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_317C')

    def _loc_313E(): pass

    label('loc_313E')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3165',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_317C')

    def _loc_3165(): pass

    label('loc_3165')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_317C(): pass

    label('loc_317C')

    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_31BD',
    )

    ChrTalk(
        0x0110,
        (
            '#0110410169V#270F<FIXME>むっ…………！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_31BD(): pass

    label('loc_31BD')

    OP_1D(0x6F)
    Sleep(500)

    @scena.Lambda('lambda_31CA')
    def lambda_31CA():
        OP_6D(-18810, 0, 1110, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_31CA)

    @scena.Lambda('lambda_31E2')
    def lambda_31E2():
        OP_67(0, 5310, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_31E2)

    @scena.Lambda('lambda_31FA')
    def lambda_31FA():
        OP_6B(3430, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_31FA)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010410187V#1005F#1P墨镜男！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410188V#1042F『瘦狼』吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0101, 17480, 0, -710, 270)
    SetChrPos(0x0102, 17440, 0, 930, 270)
    SetChrPos(0x0108, 16010, 0, 200, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_32AB',
    )

    SetChrPos(0x00F9, 18670, 0, 90, 270)

    Jump('loc_32BC')

    def _loc_32AB(): pass

    label('loc_32AB')

    SetChrPos(0x00F8, 18670, 0, 90, 270)

    def _loc_32BC(): pass

    label('loc_32BC')

    @scena.Lambda('lambda_32C2')
    def lambda_32C2():
        OP_8E(0x00FE, -10070, 0, 210, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_32C2)

    @scena.Lambda('lambda_32DD')
    def lambda_32DD():
        OP_6D(-13930, 0, 1180, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_32DD)

    @scena.Lambda('lambda_32F5')
    def lambda_32F5():
        OP_67(0, 3910, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_32F5)

    @scena.Lambda('lambda_330D')
    def lambda_330D():
        OP_6B(3680, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_330D)

    @scena.Lambda('lambda_331D')
    def lambda_331D():
        OP_6E(311, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_331D)

    Sleep(50)

    @scena.Lambda('lambda_3332')
    def lambda_3332():
        OP_8E(0x00FE, -8700, 0, -1200, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3332)

    Sleep(100)

    @scena.Lambda('lambda_3352')
    def lambda_3352():
        OP_8E(0x00FE, -8900, 0, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3352)

    Sleep(40)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3397',
    )

    @scena.Lambda('lambda_337F')
    def lambda_337F():
        OP_8E(0x00FE, -7500, 0, -410, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_337F)

    Jump('loc_33B2')

    def _loc_3397(): pass

    label('loc_3397')

    @scena.Lambda('lambda_339D')
    def lambda_339D():
        OP_8E(0x00FE, -7500, 0, -410, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_339D)

    def _loc_33B2(): pass

    label('loc_33B2')

    WaitForThreadExit(0x0102, 0x0002)
    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x0101, 4)
    SetChrChipByIndex(0x0102, 6)
    SetChrChipByIndex(0x0108, 21)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33E5',
    )

    SetChrChipByIndex(0x00F9, 8)

    Jump('loc_33EA')

    def _loc_33E5(): pass

    label('loc_33E5')

    SetChrChipByIndex(0x00F8, 8)

    def _loc_33EA(): pass

    label('loc_33EA')

    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)
    SetChrSubChip(0x0002, 0)
    SetChrSubChip(0x0003, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0108,
        (
            '#0080410189V#572F……#6P瓦鲁特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200410190V#251F#5P呼呼……终于来了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410191V既然来到这里，\n',
            '想必已经做好了心理准备吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080410192V#074F#6P嗯……\n',
            '从师父那里继承的『活人』之拳…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410193V#072F为了粉碎你的邪拳，\n',
            '我会发挥出它的全部精髓的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200410194V#257F#5P……呼呼…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410195V看来老头子\n',
            '的预料果然应验了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0108, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0108,
        (
            '#0080410196V#073F#6P师父的……预料！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410197V#076F什么意思，瓦鲁特！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410198V你和师父的决斗\n',
            '果然和我有关吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200410199V#253F#5P哈哈……所以我不是说过了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410200V要想知道这些的话\n',
            '就先打败我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Sleep(200)

    ClearChrFlags(0x0008, 0x0002)
    SetChrChipByIndex(0x0008, 15)
    SetChrSubChip(0x0008, 0)
    Sleep(200)

    OP_99(0x0008, 0x01, 0x02, 0x000003E8)
    OP_22(0x00BC, 0x00, 0x64)
    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0800)
    SetChrFlags(0x000A, 0x0004)
    SetChrChipByIndex(0x000A, 2)
    SetChrPos(0x000A, -33300, 6900, 2900, 90)
    CreateThread(0x000A, 0x03, 0x00, 0x0002)
    ClearChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000B, 0x0800)
    SetChrFlags(0x000B, 0x0004)
    SetChrChipByIndex(0x000B, 2)
    SetChrPos(0x000B, -33300, 6900, -2900, 90)
    CreateThread(0x000B, 0x03, 0x00, 0x0002)

    @scena.Lambda('lambda_36EA')
    def lambda_36EA():
        OP_6D(-31560, 5700, 0, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_36EA)

    @scena.Lambda('lambda_3702')
    def lambda_3702():
        OP_67(0, 6700, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3702)

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    SetChrPos(0x0108, -9000, 0, 210, 270)
    SetChrPos(0x0101, -7300, 0, -770, 270)
    SetChrPos(0x0102, -7300, 0, 1190, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3772',
    )

    SetChrPos(0x00F9, -5040, 0, 240, 270)

    Jump('loc_3783')

    def _loc_3772(): pass

    label('loc_3772')

    SetChrPos(0x00F8, -5040, 0, 240, 270)

    def _loc_3783(): pass

    label('loc_3783')

    SetChrChipByIndex(0x0008, 15)
    SetChrSubChip(0x0008, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x00000010)
    CreateThread(0x000A, 0x00, 0x00, 0x0009)
    Sleep(100)

    @scena.Lambda('lambda_37AD')
    def lambda_37AD():
        OP_6D(-13900, 500, 410, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_37AD)

    @scena.Lambda('lambda_37C5')
    def lambda_37C5():
        OP_67(0, 3000, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_37C5)

    @scena.Lambda('lambda_37DD')
    def lambda_37DD():
        OP_6E(288, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_37DD)

    @scena.Lambda('lambda_37ED')
    def lambda_37ED():
        OP_6B(3670, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_37ED)

    Sleep(100)

    CreateThread(0x000B, 0x00, 0x00, 0x000A)
    WaitForThreadExit(0x000A, 0x0000)
    WaitForThreadExit(0x000B, 0x0000)
    Fade(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x00000010)

    @scena.Lambda('lambda_3826')
    def lambda_3826():
        OP_6C(270000, 0)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3826)

    OP_71(0x0000, 0x0004)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0200410201V#257F那种软弱无用的拳法，\n',
            '我会在此地将其彻底埋葬……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410202V#253F来，决一死战吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_38AA')
    def lambda_38AA():
        OP_6D(-13930, 500, 410, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_38AA)

    @scena.Lambda('lambda_38C2')
    def lambda_38C2():
        OP_67(0, 2920, -10000, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_38C2)

    @scena.Lambda('lambda_38DA')
    def lambda_38DA():
        OP_6B(3000, 250)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_38DA)

    SetChrChipByIndex(0x0108, 20)
    SetChrFlags(0x0108, 0x1000)

    @scena.Lambda('lambda_38F4')
    def lambda_38F4():
        OP_91(0x00FE, -5000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0000, lambda_38F4)

    Sleep(30)

    SetChrFlags(0x0008, 0x0020)
    SetChrChipByIndex(0x0008, 19)
    SetChrSubChip(0x0008, 2)

    @scena.Lambda('lambda_3923')
    def lambda_3923():
        OP_96(0x00FE, 0xFFFFD120, 0x00000000, 0x0000015E, 0x000005DC, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_3923)

    TerminateThread(0x000A, 0x03)
    SetChrChipByIndex(0x000A, 3)
    SetChrSubChip(0x000A, 0)
    SetChrFlags(0x000A, 0x0020)
    SetChrFlags(0x000A, 0x1000)

    @scena.Lambda('lambda_3959')
    def lambda_3959():
        OP_99(0x00FE, 0x00, 0x06, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3959)

    @scena.Lambda('lambda_3969')
    def lambda_3969():
        OP_91(0x00FE, 5000, 0, 2000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_3969)

    @scena.Lambda('lambda_3984')
    def lambda_3984():
        OP_91(0x00FE, -5000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3984)

    @scena.Lambda('lambda_399F')
    def lambda_399F():
        OP_91(0x00FE, -5000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_399F)

    Sleep(30)

    TerminateThread(0x000B, 0x03)
    SetChrChipByIndex(0x000B, 3)
    SetChrSubChip(0x000B, 0)
    SetChrFlags(0x000B, 0x0020)
    SetChrFlags(0x000B, 0x1000)

    @scena.Lambda('lambda_39D7')
    def lambda_39D7():
        OP_99(0x00FE, 0x00, 0x06, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_39D7)

    @scena.Lambda('lambda_39E7')
    def lambda_39E7():
        OP_91(0x00FE, 5000, 0, -2000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_39E7)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A2C',
    )

    SetChrChipByIndex(0x00F9, 8)

    @scena.Lambda('lambda_3A14')
    def lambda_3A14():
        OP_91(0x00FE, -5000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_3A14)

    Jump('loc_3A4C')

    def _loc_3A2C(): pass

    label('loc_3A2C')

    SetChrChipByIndex(0x00F8, 8)

    @scena.Lambda('lambda_3A37')
    def lambda_3A37():
        OP_91(0x00FE, -5000, 0, 0, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_3A37)

    def _loc_3A4C(): pass

    label('loc_3A4C')

    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x00F8, 0xFF)
    TerminateThread(0x00F9, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    Battle(0x00000461, 0x00000000, 0x00, 0x0000, 0xFF)
    Call(0, 0x0015)

    Return()

# id: 0x0015 offset: 0x3A7F
@scena.Code('func_15_3A7F')
def func_15_3A7F():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x000A, 0x00)
    TerminateThread(0x000B, 0x00)
    TerminateThread(0x0008, 0x00)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0102, 0x00)
    TerminateThread(0x00F8, 0x00)
    TerminateThread(0x00F9, 0x00)
    Call(0, 0x0005)
    OP_6D(-19390, 0, 1250, 0)
    OP_67(0, 4700, -10000, 0)
    OP_6B(6360, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    OP_6D(-6100, 0, 720, 0)
    OP_67(0, 6850, -10000, 0)
    OP_6B(7340, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrPos(0x0008, -18090, 0, -3270, 0)
    SetChrPos(0x0108, -18090, 0, 3750, 180)
    SetChrPos(0x0101, -10300, 0, -600, 270)
    SetChrPos(0x0102, -10400, 0, 800, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B99',
    )

    SetChrPos(0x00F9, -9200, 0, 0, 270)

    Jump('loc_3BAA')

    def _loc_3B99(): pass

    label('loc_3B99')

    SetChrPos(0x00F8, -9200, 0, 0, 270)

    def _loc_3BAA(): pass

    label('loc_3BAA')

    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x00F8, 65535)
    SetChrChipByIndex(0x00F9, 65535)
    SetChrSubChip(0x0000, 0)
    SetChrSubChip(0x0001, 0)
    SetChrSubChip(0x0002, 0)
    SetChrSubChip(0x0003, 0)
    SetChrChipByIndex(0x0008, 15)
    SetChrSubChip(0x0008, 0)
    LoadEffect(0x00, 'scraft\\sc007_12.eff')
    LoadEffect(0x01, 'scraft\\sc007_17.eff')
    OP_12(0x00011170, 0x00041EB0, 0x00000000)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_3C24')
    def lambda_3C24():
        OP_6D(-19390, 0, 1500, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3C24)

    OP_67(0, 5210, -10000, 3000)
    OP_0D()
    Fade(500)
    OP_12(0x00011170, 0x00029810, 0x00000000)
    OP_6B(4270, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0200410267V#259F#6P这……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410268V你这家伙……什么时候\n',
            '练就了这等功夫……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080410269V#074F瓦鲁特……\n',
            '你确实是个天才。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410270V但是也正因为如此，\n',
            '导致了你疏于修练。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410271V#072F而所谓功夫，只有靠单调枯燥的\n',
            '刻苦锻炼才能取得成就……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410272V虽然我的资质愚鲁，但经过多年苦练，\n',
            '一样可以达到不逊于你的境界。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200410273V#255F#6P………………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410274V#257F哼哼哼……你的资质愚鲁吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410275V#253F但那老头子\n',
            '可不是这样想啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080410276V#073F………哎……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_1D(0x53)
    Sleep(500)

    @scena.Lambda('lambda_3E81')
    def lambda_3E81():
        OP_6B(3600, 12000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3E81)

    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0200410277V#253F老头子曾和我说过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410278V抛开活人、杀人的理念不谈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410279V单论资质和才能……\n',
            '你统统都在我之上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0108, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0108,
        (
            '#0080410280V#076F什…什么…！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200410281V#253F#6P而老头子又打算让更有才能的弟子\n',
            '继承『泰斗流』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410282V……这话的含义，\n',
            '就算你再迟钝也能明白吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080410283V#075F但、但是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410284V#072F说我比你有资质\n',
            '开玩笑也要看场合吧！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410285V而且师父，也不可能\n',
            '不顾及雾香的感情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200410286V#250F……呼呼呼……\n',
            '所以说你这家伙头脑真简单。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410287V失去了流派的继承权，\n',
            '却还厚着脸皮和师父的女儿在一起……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410288V那种事……\n',
            '你以为我能接受吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080410289V#572F……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200410290V#251F所以我向老头子提出请求，\n',
            '想以和你决胜负的方式来决定继承权的归属。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410291V但是，老头子他却这么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410292V#257F『──金会在无意识中\n',
            '对你容让留情』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410293V『无论武术，还是女人』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410294V#255F『如果你总是现在这个样子……\n',
            '那他的武术就永远无法取得大成』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080410295V#073F…………什……什么…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200410296V#253F#6P呼呼……我当时年轻气盛，\n',
            '听了这种话之后，更加接受不了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410297V而老头子提出…代替你\n',
            '和我决一死战……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410298V#257F结果我──战胜了老头子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080410299V#072F……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200410300V#253F#6P呼呼呼……这就是\n',
            '我和老头子死斗的理由。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410301V如你所愿，我把一切都告诉你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080410302V#074F……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410303V我一直想知道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410304V师父当年为何要\n',
            '向你提出决斗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410305V#572F如今终于……明白答案了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200410306V#255F#6P……什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080410307V#072F瓦鲁特……\n',
            '其实你误会了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410308V我也是之后\n',
            '才从雾香那里得知……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410309V#074F在当时，龙牙师父\n',
            '似乎就已经身患重病了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410310V听说是恶性肿瘤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0200410311V#258F#6P……什…什么…！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080410312V#072F正因如此，师父\n',
            '才向你提出决战的要求。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410313V目的当然是想亲身告诉你什么是\n',
            '武术的真正含义……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410314V同时也打算对未成熟的我\n',
            '显示武术的极致吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410315V#572F然而，师父最大的愿望……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410316V#074F就是将武术家的生命\n',
            '在与第一号弟子的战斗中\n',
            '结束掉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200410317V#254F#6P……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410318V#252F……呼呼……那算什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410319V那种蠢话……\n',
            '……怎么可能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410320V那就是说，\n',
            '我只是被老头子利用了而已吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410321V如果是那样的话……我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080410322V#074F的确……\n',
            '师傅的做法也许有些自作主张。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410323V#072F但是，习武者追求最强境界\n',
            '的信念，本身不也是出于利己的想法吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410324V这也许正是我们武术家\n',
            '所必须背负的宿命也说不定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410325V#572F所以师父……\n',
            '才会如此武断地做出决定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410326V用这种极端的方式，让你我二人\n',
            '感受到武术的光与暗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200410327V#254F#6P……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(100)

    Fade(250)
    SetChrChipByIndex(0x0108, 21)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0108,
        (
            '#0080410328V#072F……瓦鲁特，接招吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200410329V#255F#6P什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080410330V#072F我要把从师傅和你身上学到，\n',
            '并在游击士职业中磨练而成的\n',
            '『泰斗』精华，全部都寄托在这一拳上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410331V这一拳，要把你这个堕入修罗道的\n',
            '不成器师兄彻底打醒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410332V#074F这或许也是我这个当师弟的\n',
            '能为你做的最后一件事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200410333V#255F#6P……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410334V#257F……哼…………\n',
            '真能吹牛啊………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    SetChrChipByIndex(0x0008, 14)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0200410335V#253F那我就将在结社中磨练出来的\n',
            '全部秘技凝集在这一拳中……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410336V将『泰斗』的一切彻底埋葬！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    OP_6D(-19320, 0, 0, 0)
    OP_67(0, 4770, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -8300, 0, -600, 270)
    SetChrPos(0x0102, -8400, 0, 800, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C11',
    )

    SetChrPos(0x00F9, -7200, 0, 0, 270)

    Jump('loc_4C22')

    def _loc_4C11(): pass

    label('loc_4C11')

    SetChrPos(0x00F8, -7200, 0, 0, 270)

    def _loc_4C22(): pass

    label('loc_4C22')

    OP_71(0x0000, 0x0004)
    OP_0D()
    PlayEffect(0x00, 0x00, 0x0108, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(100)

    PlayEffect(0x00, 0x01, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x0108,
        (
            '#0080410337V#072F#4P……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200410338V#255F#5P……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ClearMapFlags(0x00000010)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 12)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 16)
    OP_0D()

    @scena.Lambda('lambda_4D2D')
    def lambda_4D2D():
        OP_99(0x00FE, 0x00, 0x07, 0x00000708)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_4D2D)

    @scena.Lambda('lambda_4D3D')
    def lambda_4D3D():
        OP_99(0x00FE, 0x00, 0x02, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4D3D)

    WaitForThreadExit(0x0008, 0x0001)
    Sleep(700)

    @scena.Lambda('lambda_4D57')
    def lambda_4D57():
        OP_7C(0x00000064, 0x00000000, 0x000003E8, 0x000003E8)
        Yield()

        Jump('lambda_4D57')

    DispatchAsync2(0x0101, 0x0003, lambda_4D57)

    OP_22(0x0085, 0x00, 0x64)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrTalk(
        0x0108,
        (
            '#077F#1K#4P嗬啊啊啊啊啊啊啊啊啊……！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0008,
        (
            '#0200410340V#259F#1K#1P唔哦哦哦哦哦哦哦哦哦……！',
            TxtCtl.Enter,
        ),
    )

    OP_56(0x01)
    OP_59()
    Sleep(1000)

    OP_6D(-13000, 0, 0, 1500)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010410341V#1020F#6P（好、好厉害……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410342V#1043F#4P（这样下去必有一方……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    OP_67(0, 4770, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    OP_0D()

    @scena.Lambda('lambda_4E95')
    def lambda_4E95():
        OP_6B(4000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4E95)

    ChrTalk(
        0x0108,
        (
            '#076F#4P#30A哦哦哦哦哦哦哦哦哦哦哦哦……！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0008,
        (
            '#0200410344V#258F#1P#30A啊啊啊啊啊啊啊啊啊啊啊啊……！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(5000)

    OP_56(0x00)
    WaitForThreadExit(0x0101, 0x0002)

    @scena.Lambda('lambda_4F1D')
    def lambda_4F1D():
        OP_6B(3000, 200)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4F1D)

    TerminateThread(0x0101, 0x03)
    OP_82(0x00, 0x00)
    OP_82(0x01, 0x00)
    OP_23(0x0085)
    SetChrFlags(0x0108, 0x0020)
    SetChrFlags(0x0108, 0x1000)
    SetChrFlags(0x0008, 0x0020)
    SetChrFlags(0x0008, 0x0040)
    OP_7D(0x00, 0x0108, 0x0032, 0x01F4)
    OP_7D(0x00, 0x0008, 0x0032, 0x01F4)

    @scena.Lambda('lambda_4F5E')
    def lambda_4F5E():
        OP_8E(0x00FE, -18090, 0, 3750, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4F5E)

    @scena.Lambda('lambda_4F79')
    def lambda_4F79():
        OP_8E(0x00FE, -18090, 0, -3270, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_4F79)

    SetChrChipByIndex(0x0108, 10)
    SetChrSubChip(0x0108, 3)
    SetChrChipByIndex(0x0008, 17)
    SetChrSubChip(0x0008, 1)
    PlayEffect(0x01, 0x00, 0x00FF, -18090, 800, 240, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x000000C8, 0x000000C8, 0x00000BB8, 0x00000064)
    FadeOut(100, 16777215, -1)
    WaitForThreadExit(0x0108, 0x0001)
    ClearChrFlags(0x0108, 0x0020)
    ClearChrFlags(0x0108, 0x1000)
    ClearChrFlags(0x0008, 0x0020)
    ClearChrFlags(0x0008, 0x0040)
    OP_7D(0x01, 0x0108, 0x0000, 0x0000)
    OP_7D(0x01, 0x0008, 0x0000, 0x0000)
    OP_0D()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x00000010)
    OP_6D(-19390, 0, 1500, 0)
    OP_67(0, 4700, -10000, 0)
    OP_6B(3550, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    OP_72(0x0000, 0x0004)
    FadeIn(2000, 16777215)
    OP_0D()
    Sleep(2000)

    ChrTalk(
        0x0008,
        (
            '#0200410345V#254F#5P……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080410346V#074F#6P……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410347V#572F……………唔…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 11)
    OP_99(0x0108, 0x00, 0x01, 0x000004B0)

    @scena.Lambda('lambda_5132')
    def lambda_5132():
        OP_6D(-19390, 0, -500, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5132)

    OP_22(0x020C, 0x00, 0x64)
    OP_99(0x0108, 0x01, 0x03, 0x000004B0)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020410348V#1044F#1P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410349V#1020F#1P金，金先生！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 1)
    OP_0D()
    OP_8C(0x0008, 180, 400)
    SetChrPos(0x0008, -18090, 0, 3500, 180)

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x20),
            Expr.Or2,
            Expr.Return,
        ),
    )

    ClearChrFlags(0x0008, 0x0001)
    SetChrFlags(0x0008, 0x0002)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 0)

    ChrTalk(
        0x0008,
        (
            '#0200410350V#253F#6P#40W呼呼呼……\n',
            '……真没办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5231')
    def lambda_5231():
        OP_6D(-19390, 0, 3500, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5231)

    OP_99(0x0008, 0x00, 0x04, 0x000003E8)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    Sleep(1000)

    OP_99(0x0008, 0x04, 0x06, 0x00000320)
    Sleep(200)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0200410351V#253F#2P#40W……拥有这等功夫，\n',
            '却把它埋藏在污泥之中……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410352V#257F#40W呼呼……老头子的话\n',
            '………我总算明白了………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410353V#250F#60W……呼……美味……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200410354V#80W香烟……真是……\n',
            '…………美味啊……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0008, 24)
    OP_99(0x0008, 0x18, 0x1E, 0x000005DC)
    Sleep(200)

    @scena.Lambda('lambda_537C')
    def lambda_537C():
        OP_6D(-19390, 0, 4000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_537C)

    SetChrSubChip(0x0008, 10)
    OP_99(0x0008, 0x0A, 0x12, 0x000005DC)
    OP_22(0x020C, 0x00, 0x64)
    OP_99(0x0008, 0x13, 0x17, 0x000005DC)
    Sleep(1000)

    Fade(500)
    OP_6D(-14570, 0, 810, 0)
    OP_67(0, 5410, -10000, 0)
    OP_6B(3890, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_547E',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_543D',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_547B')

    def _loc_543D(): pass

    label('loc_543D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5464',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_547B')

    def _loc_5464(): pass

    label('loc_5464')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_547B(): pass

    label('loc_547B')

    Jump('loc_54E3')

    def _loc_547E(): pass

    label('loc_547E')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_54A5',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_54E3')

    def _loc_54A5(): pass

    label('loc_54A5')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_54CC',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_54E3')

    def _loc_54CC(): pass

    label('loc_54CC')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_54E3(): pass

    label('loc_54E3')

    Sleep(100)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010410355V#1025F#6P难，难不成……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410356V#1040F#2P嗯……\n',
            '看来是金先生赢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5567')
    def lambda_5567():
        OP_6D(-17900, 0, -2700, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_5567)

    @scena.Lambda('lambda_557F')
    def lambda_557F():
        OP_67(0, 5260, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_557F)

    @scena.Lambda('lambda_5597')
    def lambda_5597():
        OP_6B(3580, 2500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_5597)

    CreateThread(0x0101, 0x01, 0x00, 0x0017)
    Sleep(200)

    CreateThread(0x0102, 0x01, 0x00, 0x0018)
    Sleep(150)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_55D0',
    )

    CreateThread(0x00F9, 0x01, 0x00, 0x0019)

    Jump('loc_55D7')

    def _loc_55D0(): pass

    label('loc_55D0')

    CreateThread(0x00F8, 0x01, 0x00, 0x001A)

    def _loc_55D7(): pass

    label('loc_55D7')

    WaitForThreadExit(0x0102, 0x0001)
    WaitForThreadExit(0x0102, 0x0001)
    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0102, 0x0002)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5635',
    )

    ChrTalk(
        0x0106,
        (
            '#0050410357V#051F嘿嘿……\n',
            '成功了嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5830')

    def _loc_5635(): pass

    label('loc_5635')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5673',
    )

    ChrTalk(
        0x0103,
        (
            '#0030410358V#021F金先生……你成功了呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5830')

    def _loc_5673(): pass

    label('loc_5673')

    If(
        (
            (Expr.Eval, "OP_42(0x0F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_56B2',
    )

    ChrTalk(
        0x0110,
        (
            '#0110410359V#275F<FIXME>フッ……見事だ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5830')

    def _loc_56B2(): pass

    label('loc_56B2')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_56EF',
    )

    ChrTalk(
        0x0104,
        (
            '#0040410360V#031F呼……\n',
            '漂亮的胜利哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5830')

    def _loc_56EF(): pass

    label('loc_56EF')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5729',
    )

    ChrTalk(
        0x0109,
        (
            '#0180410361V#1061F呀～！\n',
            '真是厉害！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5830')

    def _loc_5729(): pass

    label('loc_5729')

    If(
        (
            (Expr.Eval, "OP_42(0x0E)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_576E',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410362V#171Fジン殿……\n',
            '見事な勝利でした。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5830')

    def _loc_576E(): pass

    label('loc_576E')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_57A7',
    )

    ChrTalk(
        0x0105,
        (
            '#0060410363V#1168F……漂亮的胜利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5830')

    def _loc_57A7(): pass

    label('loc_57A7')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_57E6',
    )

    ChrTalk(
        0x0107,
        (
            '#0070410364V#067F哇～……\n',
            '好，好厉害……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5830')

    def _loc_57E6(): pass

    label('loc_57E6')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5830',
    )

    ChrTalk(
        0x010B,
        (
            '#0090410365V#210F真、真不敢相信……\n',
            '实在是大开眼界啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5830(): pass

    label('loc_5830')

    ChrTalk(
        0x0101,
        (
            '#0010410366V#1001F#6P嗯嗯！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410367V#1018F真没想到！和这么厉害的人\n',
            '正面决斗竟然还能赢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080410368V#074F#5P……不………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_58BE')
    def lambda_58BE():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x00000BB8, 0x000007D0)
        Yield()

        Jump('lambda_58BE')

    DispatchAsync2(0x0108, 0x0003, lambda_58BE)

    Sleep(300)

    OP_99(0x0108, 0x03, 0x00, 0x00000320)
    TerminateThread(0x0108, 0x03)
    Fade(500)
    SetChrChipByIndex(0x0108, 65535)
    SetChrSubChip(0x0108, 0)
    OP_0D()

    @scena.Lambda('lambda_58FD')
    def lambda_58FD():
        OP_8C(0x0102, 270, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_58FD)

    Sleep(200)

    OP_8C(0x0108, 90, 300)
    Sleep(500)

    ChrTalk(
        0x0108,
        (
            '#0080410369V#074F#5P我之所以能够获胜，只是因为\n',
            '我背负着『泰斗流』之名而战。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410370V#572F如果那家伙\n',
            '也使用正宗的『泰斗』武术\n',
            '来应战的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410371V倒下的\n',
            '大概会是我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410372V#1016F#6P真是的～没那种事啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410373V#1015F对了金先生……\n',
            '有没有受伤？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410374V#1044F需要治疗一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080410375V#074F#5P不……没问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410376V#070F……瓦鲁特那家伙\n',
            '暂时还不会醒来，\n',
            '就放他在这里也没关系吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410377V现在我们赶快往上走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410378V#1006F#6P……嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410379V#1040F那么，\n',
            '去操纵那里的终端吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -17410, 0, 4440, 180)
    ClearChrFlags(0x0009, 0x0001)
    SetChrFlags(0x0009, 0x0002)
    SetChrFlags(0x0009, 0x0010)
    SetChrChipByIndex(0x0009, 0)
    SetChrSubChip(0x0009, 23)
    ClearChrFlags(0x0009, 0x0080)
    OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_A2(0x2235)
    OP_28(0x009F, 0x01, 0x0020)

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x20),
            Expr.Not,
            Expr.And2,
            Expr.Return,
        ),
    )

    EventEnd(0x00)
    OP_1D(0x40)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x40),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0016 offset: 0x5BAB
@scena.Code('func_16_5BAB')
def func_16_5BAB():
    @scena.Lambda('lambda_5BB1')
    def lambda_5BB1():
        OP_8E(0x00FE, 17580, 0, 850, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5BB1)

    Sleep(40)

    @scena.Lambda('lambda_5BD1')
    def lambda_5BD1():
        OP_8E(0x00FE, 17550, 0, -220, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_5BD1)

    Sleep(100)

    @scena.Lambda('lambda_5BF1')
    def lambda_5BF1():
        OP_8E(0x00FE, 18710, 0, 1270, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5BF1)

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5C2F',
    )

    OP_8E(0x00F9, 18630, 0, -780, 3000, 0x00)

    Jump('loc_5C43')

    def _loc_5C2F(): pass

    label('loc_5C2F')

    OP_8E(0x00F8, 18630, 0, -780, 3000, 0x00)

    def _loc_5C43(): pass

    label('loc_5C43')

    Return()

# id: 0x0017 offset: 0x5C44
@scena.Code('func_17_5C44')
def func_17_5C44():
    OP_8E(0x00FE, -16370, 0, -4210, 5000, 0x00)
    OP_8C(0x00FE, 270, 400)

    Return()

# id: 0x0018 offset: 0x5C60
@scena.Code('func_18_5C60')
def func_18_5C60():
    OP_8E(0x00FE, -16530, 0, -2990, 5000, 0x00)
    OP_8C(0x00FE, 225, 400)

    Return()

# id: 0x0019 offset: 0x5C7C
@scena.Code('func_19_5C7C')
def func_19_5C7C():
    OP_8E(0x00FE, -15320, 0, -3760, 5000, 0x00)
    OP_8C(0x00FE, 270, 400)

    Return()

# id: 0x001A offset: 0x5C98
@scena.Code('func_1A_5C98')
def func_1A_5C98():
    OP_8E(0x00FE, -15320, 0, -3760, 5000, 0x00)
    OP_8C(0x00FE, 270, 400)

    Return()

# id: 0x001B offset: 0x5CB4
@scena.Code('func_1B_5CB4')
def func_1B_5CB4():
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '向上层区域方向的隔离壁，\n',
            '以及传送门的锁定解除。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(200)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5303._SN', 115, 0, 0)
    IdleLoop()

    Return()

# id: 0x001C offset: 0x5D20
@scena.Code('func_1C_5D20')
def func_1C_5D20():
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
        'loc_5D37',
    )

    Call(0, 0x001E)
    Call(0, 0x001F)

    def _loc_5D37(): pass

    label('loc_5D37')

    OP_6D(-33350, 0, 660, 0)
    OP_67(0, 5840, -10000, 0)
    OP_6B(3430, 0)
    OP_6C(302000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -31400, 0, -720, 270)
    SetChrPos(0x0102, -31400, 0, 210, 270)
    SetChrPos(0x00F8, -29800, 0, -1260, 270)
    SetChrPos(0x00F9, -29800, 0, 10, 270)
    FadeIn(1000, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '向上层区域方向的隔离壁，\n',
            '以及传送门的锁定已经解除了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(1000)
    OP_71(0x0001, 0x0004)
    OP_0D()
    Sleep(500)

    OP_64(0x00, 0x0001)
    OP_A2(0x2236)
    OP_28(0x009F, 0x01, 0x0040)
    EventEnd(0x00)

    Return()

# id: 0x001D offset: 0x5E37
@scena.Code('func_1D_5E37')
def func_1D_5E37():
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
        'loc_5E4E',
    )

    Call(0, 0x001E)
    Call(0, 0x001F)

    def _loc_5E4E(): pass

    label('loc_5E4E')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5E63',
    )

    Call(0, 0x0006)

    Jump('loc_5E67')

    def _loc_5E63(): pass

    label('loc_5E63')

    Call(0, 0x0014)

    def _loc_5E67(): pass

    label('loc_5E67')

    Return()

# id: 0x001E offset: 0x5E68
@scena.Code('func_1E_5E68')
def func_1E_5E68():
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
        (0x00000000, 'loc_5EE2'),
        (0x00000001, 'loc_5EE8'),
        (-1, 'loc_5EEE'),
    )

    def _loc_5EE2(): pass

    label('loc_5EE2')

    OP_A2(0x1200)

    Jump('loc_5EEE')

    def _loc_5EE8(): pass

    label('loc_5EE8')

    OP_A2(0x1201)

    Jump('loc_5EEE')

    def _loc_5EEE(): pass

    label('loc_5EEE')

    Return()

# id: 0x001F offset: 0x5EEF
@scena.Code('func_1F_5EEF')
def func_1F_5EEF():
    FadeOut(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
            0x000A,
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

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

# id: 0x0020 offset: 0x5F82
@scena.Code('func_20_5F82')
def func_20_5F82():
    FadeOut(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x0002,
            0x00FF,
        ),
        (
            0x0005,
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
            0x000A,
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

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
