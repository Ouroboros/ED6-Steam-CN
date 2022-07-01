import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4405_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4405   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '丹克'),
    TXT(0x02, '菲利奥'),
    TXT(0x03, '特务兵'),
    TXT(0x04, '特务兵'),
    TXT(0x05, '特务兵'),
    TXT(0x06, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4405.x'
    header.mapIndex       = 1
    header.bgm            = 34
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x19DC
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
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01330._CH', 'ED6_DT07/CH01330P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP'),
        ('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP'),
        ('ED6_DT07/CH00340._CH', 'ED6_DT07/CH00340P._CP'),
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT07/CH00344._CH', 'ED6_DT07/CH00344P._CP'),
        ('ED6_DT06/CH20042._CH', 'ED6_DT06/CH20042P._CP'),
        ('ED6_DT07/CH00440._CH', 'ED6_DT07/CH00440P._CP'),
        ('ED6_DT07/CH00441._CH', 'ED6_DT07/CH00441P._CP'),
    ]

# id: 0x10002 offset: 0x132
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 1500,
            z                   = 0,
            y                   = 10870,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 500,
            z                   = 0,
            y                   = 450,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x1D2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1D2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1D2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 1050,
            triggerZ            = 0,
            triggerY            = 10640,
            triggerRange        = 800,
            actorX              = 150,
            actorZ              = 1700,
            actorY              = 10640,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1F6
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_202'),
        (-1, 'loc_216'),
    )

    def _loc_202(): pass

    label('loc_202')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 4, 0x163C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_213',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0005)

    def _loc_213(): pass

    label('loc_213')

    Jump('loc_216')

    def _loc_216(): pass

    label('loc_216')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 4, 0x163C)),
            Expr.Return,
        ),
        'loc_2BD',
    )

    SetChrPos(0x0009, 4840, 0, -2540, 0)
    SetChrPos(0x0008, 4250, 0, -210, 270)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0002)
    SetChrFlags(0x000C, 0x0002)
    SetChrFlags(0x000A, 0x0002)
    SetChrFlags(0x000B, 0x0800)
    SetChrFlags(0x000C, 0x0800)
    SetChrFlags(0x000A, 0x0800)
    SetChrChipByIndex(0x000A, 14)
    SetChrChipByIndex(0x000B, 14)
    SetChrChipByIndex(0x000C, 14)
    SetChrSubChip(0x000A, 5)
    SetChrSubChip(0x000B, 6)
    SetChrSubChip(0x000C, 0)
    SetChrPos(0x000A, 4350, 0, -1320, 90)
    SetChrPos(0x000B, 3100, 0, -2250, 90)
    SetChrPos(0x000C, 2980, 0, 200, 90)

    def _loc_2BD(): pass

    label('loc_2BD')

    Return()

# id: 0x0001 offset: 0x2BE
@scena.Code('Init')
def Init():
    OP_71(0x0001, 0x0004)

    Return()

# id: 0x0002 offset: 0x2C4
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
        'loc_2E9',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_42B')

    def _loc_2E9(): pass

    label('loc_2E9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_302',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_42B')

    def _loc_302(): pass

    label('loc_302')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_31B',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_42B')

    def _loc_31B(): pass

    label('loc_31B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_334',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_42B')

    def _loc_334(): pass

    label('loc_334')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34D',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_42B')

    def _loc_34D(): pass

    label('loc_34D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_366',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_42B')

    def _loc_366(): pass

    label('loc_366')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37F',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_42B')

    def _loc_37F(): pass

    label('loc_37F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_398',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_42B')

    def _loc_398(): pass

    label('loc_398')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B1',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_42B')

    def _loc_3B1(): pass

    label('loc_3B1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3CA',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_42B')

    def _loc_3CA(): pass

    label('loc_3CA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E3',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_42B')

    def _loc_3E3(): pass

    label('loc_3E3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3FC',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_42B')

    def _loc_3FC(): pass

    label('loc_3FC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_415',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_42B')

    def _loc_415(): pass

    label('loc_415')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_42B',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_42B(): pass

    label('loc_42B')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_440',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_42B')

    def _loc_440(): pass

    label('loc_440')

    Return()

# id: 0x0003 offset: 0x441
@scena.Code('func_03_441')
def func_03_441():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 4, 0x163C)),
            Expr.Return,
        ),
        'loc_526',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_4A3',
    )

    ChrTalk(
        0x00FE,
        (
            '这、这些家伙\n',
            '记得是情报部的特务兵吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '样品的引擎\n',
            '到底打算怎样处理？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_526')

    def _loc_4A3(): pass

    label('loc_4A3')

    ChrTalk(
        0x00FE,
        (
            '样、样品在签字仪式之前\n',
            '２４小时交替\n',
            '换人监视的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这些家伙从上了锁\n',
            '的门突然破门而入……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一转眼就把引擎\n',
            '给抢走了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    def _loc_526(): pass

    label('loc_526')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x52A
@scena.Code('func_04_52A')
def func_04_52A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 4, 0x163C)),
            Expr.Return,
        ),
        'loc_588',
    )

    ChrTalk(
        0x00FE,
        (
            '这些家伙，把引擎\n',
            '运去码头方向了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可恶，这可是女王陛下\n',
            '寄存的重要物品啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_588(): pass

    label('loc_588')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x58C
@scena.Code('func_05_58C')
def func_05_58C():
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
        'loc_59F',
    )

    Call(0, 0x000C)

    def _loc_59F(): pass

    label('loc_59F')

    OP_4A(0x0009, 255)
    OP_4A(0x0008, 255)
    OP_6D(2320, 0, 13530, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0008, 3350, 0, 4000, 180)
    SetChrPos(0x0009, 4390, 0, 4000, 180)
    SetChrPos(0x000A, 3720, 0, 2280, 0)
    SetChrPos(0x000B, 4770, 0, 960, 0)
    SetChrPos(0x000C, 3440, 0, 750, 0)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x00F7, 0x0080)
    SetChrFlags(0x0109, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)

    @scena.Lambda('lambda_065D')
    def lambda_065D():
        OP_6D(3240, 0, 3110, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_065D)

    @scena.Lambda('lambda_0675')
    def lambda_0675():
        OP_67(0, 7500, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0675)

    @scena.Lambda('lambda_068D')
    def lambda_068D():
        OP_6B(2740, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_068D)

    FadeIn(2000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0008,
        (
            '#3230270384V#5P你、你们……\n',
            '到底想怎样！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3230270385V#5P做这种事\n',
            '以为就这么完了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4340270386V#6P呼，我们早已有所觉悟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2620270387V#6P不想受伤的话，\n',
            '还是乖乖待着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2620270388V#6P我们没有任何想要加害于\n',
            '一般市民的意思。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2630270389V#6P只是……\n',
            '在不阻挠我们的情况下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#3130270390V#2P呜，呜。\n',
            '就饶我一命吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 3)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_83F',
    )

    SetChrChipByIndex(0x0106, 7)

    Jump('loc_844')

    def _loc_83F(): pass

    label('loc_83F')

    SetChrChipByIndex(0x0103, 5)

    def _loc_844(): pass

    label('loc_844')

    SetChrChipByIndex(0x0109, 9)
    ClearChrFlags(0x0101, 0x0080)
    ClearChrFlags(0x00F7, 0x0080)
    ClearChrFlags(0x0109, 0x0080)
    SetChrPos(0x0101, 10400, 0, 0, 270)
    SetChrPos(0x00F7, 11500, 0, 500, 270)
    SetChrPos(0x0109, 11500, 0, -1000, 270)

    ChrTalk(
        0x0101,
        (
            '#0010270391V#1P一般市民以外的人\n',
            '就不会留情了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_093F')
    def lambda_093F():
        OP_6D(7050, 0, 1380, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_093F)

    @scena.Lambda('lambda_0957')
    def lambda_0957():
        OP_67(0, 7500, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0957)

    @scena.Lambda('lambda_096F')
    def lambda_096F():
        OP_6B(2740, 1500)

        ExitThread()

    DispatchAsync(0x00F7, 0x0002, lambda_096F)

    @scena.Lambda('lambda_097F')
    def lambda_097F():
        OP_6E(295, 1500)

        ExitThread()

    DispatchAsync(0x00F7, 0x0003, lambda_097F)

    @scena.Lambda('lambda_098F')
    def lambda_098F():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_098F)

    Sleep(50)

    @scena.Lambda('lambda_09A2')
    def lambda_09A2():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_09A2)

    Sleep(50)

    @scena.Lambda('lambda_09B5')
    def lambda_09B5():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_09B5)

    Sleep(50)

    @scena.Lambda('lambda_09C8')
    def lambda_09C8():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_09C8)

    Sleep(50)

    @scena.Lambda('lambda_09DB')
    def lambda_09DB():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_09DB)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    WaitForThreadExit(0x00F7, 0x0002)
    WaitForThreadExit(0x00F7, 0x0003)

    ChrTalk(
        0x000A,
        (
            '#4340270392V#4P什……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2620270393V#6P你们……是游击士吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270394V#1060F#5P虽然有一个不是… ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AF2',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270395V#053F#2P终于找到了……\n',
            '找得好苦啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270396V#054F根据协会规定，\n',
            '以骚乱破坏活动等的嫌疑\n',
            '逮捕你们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B6E')

    def _loc_AF2(): pass

    label('loc_AF2')

    ChrTalk(
        0x0103,
        (
            '#0030270397V#027F#2P终于找到了……\n',
            '真是大费周章啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270398V#024F根据协会规约，\n',
            '以骚乱破坏活动等的嫌疑\n',
            '逮捕你们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B6E(): pass

    label('loc_B6E')

    ChrTalk(
        0x0101,
        (
            '#0010270399V#1006F#5P赶快\n',
            '束手就擒吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2630270400V可恶……\n',
            '怎么被发现的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x000B, 11)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#2620270401V#6P算了，收拾他们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x00D8, 0x00, 0x64)
    SetChrChipByIndex(0x000A, 15)
    Sleep(200)

    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x000C, 11)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#2P#1K解决他们！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x000A,
        (
            '#4340270403V#1P#1K解决他们！',
            TxtCtl.Enter,
        ),
    )

    OP_56(0x01)
    OP_59()

    @scena.Lambda('lambda_0C60')
    def lambda_0C60():
        OP_6D(7950, 0, 330, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0C60)

    @scena.Lambda('lambda_0C78')
    def lambda_0C78():
        OP_6B(2200, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0C78)

    SetChrChipByIndex(0x000A, 16)
    SetChrChipByIndex(0x000B, 12)
    SetChrChipByIndex(0x000C, 12)

    @scena.Lambda('lambda_0C97')
    def lambda_0C97():
        OP_8F(0x00FE, 6840, 0, 520, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_0C97)

    @scena.Lambda('lambda_0CB2')
    def lambda_0CB2():
        OP_8F(0x00FE, 8140, 0, 290, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0CB2)

    Sleep(50)

    @scena.Lambda('lambda_0CD2')
    def lambda_0CD2():
        OP_8F(0x00FE, 6220, 0, 1620, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_0CD2)

    @scena.Lambda('lambda_0CED')
    def lambda_0CED():
        OP_8F(0x00FE, 9190, 0, 790, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0000, lambda_0CED)

    Sleep(50)

    @scena.Lambda('lambda_0D0D')
    def lambda_0D0D():
        OP_8F(0x00FE, 5770, 0, -220, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_0D0D)

    @scena.Lambda('lambda_0D28')
    def lambda_0D28():
        OP_8F(0x00FE, 8870, 0, -940, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0109, 0x0000, lambda_0D28)

    Sleep(200)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x00F7, 0xFF)
    TerminateThread(0x0109, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    Battle(0x0000045C, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_D73'),
        (-1, 'loc_D78'),
    )

    def _loc_D73(): pass

    label('loc_D73')

    OP_B4(0x00)

    Jump('loc_D78')

    def _loc_D78(): pass

    label('loc_D78')

    Call(0, 0x0006)

    Return()

# id: 0x0006 offset: 0xD7D
@scena.Code('func_06_D7D')
def func_06_D7D():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    Sleep(1000)

    OP_6D(4990, 0, -810, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2640, 0)
    OP_6C(315000, 0)
    OP_6E(247, 0)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x00F7, 65535)
    SetChrChipByIndex(0x0109, 65535)
    SetChrFlags(0x000B, 0x0002)
    SetChrFlags(0x000C, 0x0002)
    SetChrFlags(0x000B, 0x0800)
    SetChrFlags(0x000C, 0x0800)
    SetChrChipByIndex(0x000A, 13)
    SetChrChipByIndex(0x000B, 14)
    SetChrChipByIndex(0x000C, 14)
    SetChrSubChip(0x000A, 3)
    SetChrSubChip(0x000B, 6)
    SetChrSubChip(0x000C, 0)
    SetChrPos(0x0101, 6550, 0, -800, 270)
    SetChrPos(0x00F7, 6580, 0, -2100, 270)
    SetChrPos(0x0109, 7740, 0, -1420, 270)
    SetChrPos(0x0008, 3350, 0, 4000, 180)
    SetChrPos(0x0009, 4390, 0, 4000, 180)
    SetChrPos(0x000A, 4350, 0, -1320, 90)
    SetChrPos(0x000B, 3100, 0, -2250, 90)
    SetChrPos(0x000C, 2980, 0, 200, 90)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#4340270404V#5P算、算了……\n',
            '这样就能拖延时间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4340270405V#5P之后就全部交给\n',
            '上尉殿下了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270406V#1004F#2P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#4340270407V#5P情、情报部荣光永存……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x020C, 0x00, 0x64)
    SetChrFlags(0x000A, 0x0800)
    SetChrFlags(0x000A, 0x0002)
    SetChrChipByIndex(0x000A, 14)
    SetChrSubChip(0x000A, 5)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010270408V#1020F#2P慢，慢着！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270409V#1068F糟糕，晕过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00F7, 400)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1051',
    )

    ChrTalk(
        0x0101,
        (
            '#0010270410V#1019F#2P对了，阿加特。\n',
            '『上尉』难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050270411V#552F#6P哼……\n',
            '是那只母狐狸吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10CB')

    def _loc_1051(): pass

    label('loc_1051')

    ChrTalk(
        0x0101,
        (
            '#0010270412V#1019F#2P对了，雪拉姐。\n',
            '『上尉』难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030270413V#022F#6P嗯嗯……\n',
            '是那个顽固的女人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10CB(): pass

    label('loc_10CB')

    @scena.Lambda('lambda_10D1')
    def lambda_10D1():
        OP_6D(6450, 0, 120, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_10D1)

    @scena.Lambda('lambda_10E9')
    def lambda_10E9():
        OP_8E(0x00FE, 7000, 0, 800, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_10E9)

    Sleep(400)

    @scena.Lambda('lambda_1109')
    def lambda_1109():
        OP_8E(0x00FE, 6000, 0, 800, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1109)

    Sleep(400)

    @scena.Lambda('lambda_1129')
    def lambda_1129():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_1129')

    DispatchAsync2(0x0101, 0x0002, lambda_1129)

    @scena.Lambda('lambda_113A')
    def lambda_113A():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_113A')

    DispatchAsync2(0x00F7, 0x0002, lambda_113A)

    @scena.Lambda('lambda_114B')
    def lambda_114B():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_114B')

    DispatchAsync2(0x0109, 0x0002, lambda_114B)

    WaitForThreadExit(0x0009, 0x0001)
    OP_8C(0x0009, 180, 400)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x00F7, 0x02)
    TerminateThread(0x0109, 0x02)
    WaitForThreadExit(0x0008, 0x0001)
    OP_8C(0x0008, 180, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#3230270414V#5P你们几位……\n',
            '来得真是时候啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3130270415V#2P谢谢……\n',
            '你们是救命恩人啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270416V#1016F#6P嘿嘿……\n',
            '这是我们应该做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x0101, 315, 400)

    ChrTalk(
        0x0101,
        (
            '#0010270417V#1004F#6P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1261')
    def lambda_1261():
        OP_6D(-890, 0, 9800, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1261)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(1000)

    Fade(1000)
    OP_6D(6450, 0, 120, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2640, 0)
    OP_6C(315000, 0)
    OP_6E(247, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010270418V#1020F#6P#3S啊啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 45, 600)

    @scena.Lambda('lambda_12F1')
    def lambda_12F1():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_12F1')

    DispatchAsync2(0x0009, 0x0001, lambda_12F1)

    @scena.Lambda('lambda_1302')
    def lambda_1302():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_1302')

    DispatchAsync2(0x0008, 0x0001, lambda_1302)

    CreateThread(0x0101, 0x01, 0x00, 0x0007)
    Sleep(500)

    @scena.Lambda('lambda_131F')
    def lambda_131F():
        OP_6D(3120, 0, 9680, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_131F)

    @scena.Lambda('lambda_1337')
    def lambda_1337():
        OP_6B(2760, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1337)

    Sleep(2500)

    CreateThread(0x00F7, 0x01, 0x00, 0x0008)
    Sleep(1000)

    CreateThread(0x0109, 0x01, 0x00, 0x0009)
    WaitForThreadExit(0x00F7, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13A1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270419V#052F#6P什么、怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13CD')

    def _loc_13A1(): pass

    label('loc_13A1')

    ChrTalk(
        0x0103,
        (
            '#0030270420V#023F#6P怎么了、艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13CD(): pass

    label('loc_13CD')

    WaitForThreadExit(0x0109, 0x0001)

    ChrTalk(
        0x0109,
        (
            '#0180270421V#1064F#4P好大的\n',
            '导力器装置啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180270422V用来干什么的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 90, 500)

    ChrTalk(
        0x0101,
        (
            '#0010270423V#1020F#5P那是为埃尔赛尤\n',
            '开发的高性能导力引擎哦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010270424V记得应该有两个……',
            TxtCtl.Enter,
        ),
    )

    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0009, 0x01)
    CreateThread(0x0008, 0x01, 0x00, 0x000A)
    Sleep(300)

    CreateThread(0x0009, 0x01, 0x00, 0x000B)
    CloseMessageWindow()
    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0009, 0x0001)
    OP_6D(2660, 0, 7880, 1000)

    ChrTalk(
        0x0008,
        (
            '#3230270425V#5P啊啊，这些家伙的同伙\n',
            '用搬运车将它载走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#3230270426V#5P载往前方的码头方向……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x0101, 180, 500)

    @scena.Lambda('lambda_154F')
    def lambda_154F():
        OP_8C(0x00F7, 180, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_154F)

    OP_8C(0x0109, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010270427V#1005F#6P你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1629',
    )

    ChrTalk(
        0x0106,
        (
            '#0050270428V#552F#6P可恶，不好的预感。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_15CB')
    def lambda_15CB():
        OP_6D(3120, 0, 9680, 1000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_15CB)

    OP_8C(0x0106, 315, 400)
    WaitForThreadExit(0x00F7, 0x0001)

    ChrTalk(
        0x0106,
        (
            '#0050270429V#054F#6P艾丝蒂尔、凯文！\n',
            '我们赶紧去码头吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16BA')

    def _loc_1629(): pass

    label('loc_1629')

    ChrTalk(
        0x0103,
        (
            '#0030270430V#522F#6P有不好的预感呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_165B')
    def lambda_165B():
        OP_6D(3120, 0, 9680, 1000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_165B)

    OP_8C(0x0103, 315, 400)
    WaitForThreadExit(0x00F7, 0x0001)

    ChrTalk(
        0x0103,
        (
            '#0030270431V#024F#6P艾丝蒂尔、凯文先生！\n',
            '我们赶紧去码头吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16BA(): pass

    label('loc_16BA')

    OP_8C(0x0101, 135, 500)

    ChrTalk(
        0x0101,
        (
            '#0010270432V#1005F#5P明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180270433V#1062F#2P好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6D(2990, 0, 9730, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 2990, 0, 9730, 90)
    SetChrPos(0x0001, 2990, 0, 9730, 90)
    SetChrPos(0x0002, 2990, 0, 9730, 90)
    OP_69(0x0000, 0x00000000)
    SetChrPos(0x0009, 4840, 0, -2540, 0)
    SetChrPos(0x0008, 4250, 0, -210, 270)
    OP_4B(0x0009, 255)
    OP_4B(0x0008, 255)
    OP_A2(0x163C)
    OP_28(0x008E, 0x01, 0x0004)
    OP_28(0x008E, 0x01, 0x0008)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x17CD
@scena.Code('func_07_17CD')
def func_07_17CD():
    OP_8E(0x00FE, 10540, 0, 2870, 5000, 0x00)
    OP_8E(0x00FE, 10640, 0, 6770, 5000, 0x00)
    OP_8E(0x00FE, 2300, 0, 9600, 5000, 0x00)
    OP_8C(0x00FE, 270, 400)

    Return()

# id: 0x0008 offset: 0x1811
@scena.Code('func_08_1811')
def func_08_1811():
    OP_8E(0x00FE, 6470, 0, -600, 5000, 0x00)
    OP_8E(0x00FE, 10540, 0, 2870, 5000, 0x00)
    OP_8E(0x00FE, 10640, 0, 6770, 5000, 0x00)
    OP_8E(0x00FE, 3580, 0, 8620, 5000, 0x00)
    OP_8C(0x00FE, 270, 400)

    Return()

# id: 0x0009 offset: 0x1869
@scena.Code('func_09_1869')
def func_09_1869():
    OP_8E(0x00FE, 10540, 0, 2870, 5000, 0x00)
    OP_8E(0x00FE, 10640, 0, 6770, 5000, 0x00)
    OP_8E(0x00FE, 3630, 0, 10170, 5000, 0x00)
    OP_8C(0x00FE, 270, 400)

    Return()

# id: 0x000A offset: 0x18AD
@scena.Code('func_0A_18AD')
def func_0A_18AD():
    OP_8E(0x00FE, 3550, 0, 3020, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x000B offset: 0x18C9
@scena.Code('func_0B_18C9')
def func_0B_18C9():
    OP_8E(0x00FE, 4640, 0, 2800, 2000, 0x00)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x000C offset: 0x18E5
@scena.Code('func_0C_18E5')
def func_0C_18E5():
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
        (0x00000000, 'loc_195F'),
        (0x00000001, 'loc_1965'),
        (-1, 'loc_196B'),
    )

    def _loc_195F(): pass

    label('loc_195F')

    OP_A2(0x1200)

    Jump('loc_196B')

    def _loc_1965(): pass

    label('loc_1965')

    OP_A2(0x1201)

    Jump('loc_196B')

    def _loc_196B(): pass

    label('loc_196B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1979',
    )

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    Jump('loc_197D')

    def _loc_1979(): pass

    label('loc_1979')

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    def _loc_197D(): pass

    label('loc_197D')

    Return()

# id: 0x000D offset: 0x197E
@scena.Code('func_0D_197E')
def func_0D_197E():
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有埃尔赛尤用的新型引擎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
