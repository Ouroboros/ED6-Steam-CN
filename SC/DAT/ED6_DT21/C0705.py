import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0705_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0705   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '怪盗布卢布兰'),
    TXT(0x02, '跳梁小丑'),
    TXT(0x03, '跳梁小丑'),
    TXT(0x04, '福音'),
    TXT(0x05, '幻惑之铃露茜奥拉'),
    TXT(0x06, '瘦狼瓦鲁特'),
    TXT(0x07, '小丑肯帕雷拉'),
    TXT(0x08, '红色飞艇'),
    TXT(0x09, '红色飞艇的踪影'),
    TXT(0x0A, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0705.x'
    header.mapIndex       = 1
    header.bgm            = 33
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x33F1
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
        ('ED6_DT27/CH03530._CH', 'ED6_DT27/CH03530P._CP'),
        ('ED6_DT29/CH12160._CH', 'ED6_DT29/CH12160P._CP'),
        ('ED6_DT27/CH04530._CH', 'ED6_DT27/CH04530P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
        ('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP'),
        ('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT29/CH12161._CH', 'ED6_DT29/CH12161P._CP'),
        ('ED6_DT26/CH20273._CH', 'ED6_DT26/CH20273P._CP'),
        ('ED6_DT27/CH03520._CH', 'ED6_DT27/CH03520P._CP'),
        ('ED6_DT27/CH03500._CH', 'ED6_DT27/CH03500P._CP'),
        ('ED6_DT27/CH03600._CH', 'ED6_DT27/CH03600P._CP'),
        ('ED6_DT26/CH20431._CH', 'ED6_DT26/CH20431P._CP'),
        ('ED6_DT27/CH03500._CH', 'ED6_DT27/CH03500P._CP'),
    ]

# id: 0x10002 offset: 0x122
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
            dword_10            = 458759,
            chipIndex           = 7,
            npcIndex            = 0x01E6,
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
            dword_10            = 10,
            chipIndex           = 10,
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
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0180,
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
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0180,
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
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x242
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x242
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x242
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x242
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_261',
    )

    OP_A3(0x10F1)
    SetMapFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0008)

    Jump('loc_2B8')

    def _loc_261(): pass

    label('loc_261')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_280',
    )

    OP_A3(0x10F2)
    SetMapFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x70),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0009)

    Jump('loc_2B8')

    def _loc_280(): pass

    label('loc_280')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_29F',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x0003)

    Jump('loc_2B8')

    def _loc_29F(): pass

    label('loc_29F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 5, 0x1E05)),
            Expr.Return,
        ),
        'loc_2B8',
    )

    SetMapFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, 0x000A)

    def _loc_2B8(): pass

    label('loc_2B8')

    Return()

# id: 0x0001 offset: 0x2B9
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2CA',
    )

    OP_22(0x00EB, 0x01, 0x50)

    def _loc_2CA(): pass

    label('loc_2CA')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x454),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2DF',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x6F),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2DF(): pass

    label('loc_2DF')

    Return()

# id: 0x0002 offset: 0x2E0
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
        'loc_305',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_447')

    def _loc_305(): pass

    label('loc_305')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_31E',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_447')

    def _loc_31E(): pass

    label('loc_31E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_337',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_447')

    def _loc_337(): pass

    label('loc_337')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_350',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_447')

    def _loc_350(): pass

    label('loc_350')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_369',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_447')

    def _loc_369(): pass

    label('loc_369')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_382',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_447')

    def _loc_382(): pass

    label('loc_382')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_39B',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_447')

    def _loc_39B(): pass

    label('loc_39B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B4',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_447')

    def _loc_3B4(): pass

    label('loc_3B4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3CD',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_447')

    def _loc_3CD(): pass

    label('loc_3CD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E6',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_447')

    def _loc_3E6(): pass

    label('loc_3E6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3FF',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_447')

    def _loc_3FF(): pass

    label('loc_3FF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_418',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_447')

    def _loc_418(): pass

    label('loc_418')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_431',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_447')

    def _loc_431(): pass

    label('loc_431')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_447',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_447(): pass

    label('loc_447')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_45C',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_447')

    def _loc_45C(): pass

    label('loc_45C')

    Return()

# id: 0x0003 offset: 0x45D
@scena.Code('func_03_45D')
def func_03_45D():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_82(0x80, 0x00)
    OP_71(0x0009, 0x0004)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_79(0x00, 0x0002)
    OP_79(0x01, 0x0002)
    OP_79(0x02, 0x0002)
    OP_79(0x03, 0x0002)
    OP_79(0x04, 0x0002)
    OP_7B()
    OP_6D(40, 0, 35830, 0)
    OP_67(0, 7740, -10000, 0)
    OP_6B(3700, 0)
    UnlockAchievement(0x66, 0x01, 0x00, 0x00)
    OP_6C(45000, 0)
    OP_6E(297, 0)
    SetChrPos(0x000C, 40, 0, -7480, 0)
    ClearChrFlags(0x000C, 0x0080)
    OP_22(0x01C3, 0x00, 0x64)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_0515')
    def lambda_0515():
        OP_6D(40, 0, 0, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0515)

    Sleep(5000)

    OP_8E(0x000C, 40, 0, 0, 2000, 0x00)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0210300001V#240F『翡翠之塔』──\n',
            '看来和报告一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    @scena.Lambda('lambda_058F')
    def lambda_058F():
        OP_6D(370, 0, 9730, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_058F)

    @scena.Lambda('lambda_05A7')
    def lambda_05A7():
        OP_6B(3000, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_05A7)

    @scena.Lambda('lambda_05B7')
    def lambda_05B7():
        OP_67(0, 6900, -10000, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_05B7)

    OP_8E(0x000C, 160, 0, 8230, 2000, 0x00)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0210300002V#244F和王城封印区域有密切关联的\n',
            '『设备塔』的一角……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210300003V利用了表里两面的『第二结界』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210300004V#241F呵呵，教授也调查得够仔细的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_DB()
    OP_A1(0x0010, 0x0007)
    SetChrPos(0x0010, -25390, 1500, 11620, 180)
    OP_72(0x0007, 0x0004)
    OP_22(0x0079, 0x01, 0x46)
    Sleep(1000)

    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_24(0x0079, 0x50)
    Sleep(1000)

    @scena.Lambda('lambda_06D1')
    def lambda_06D1():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_06D1)

    OP_24(0x0079, 0x55)
    Sleep(1000)

    @scena.Lambda('lambda_06E8')
    def lambda_06E8():
        ChrTurnDirection(0x00FE, 0x0010, 100)
        Yield()

        Jump('lambda_06E8')

    DispatchAsync2(0x000C, 0x0001, lambda_06E8)

    OP_24(0x0079, 0x5A)

    @scena.Lambda('lambda_06FD')
    def lambda_06FD():
        OP_8E(0x00FE, 21060, 1500, 11130, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_06FD)

    Sleep(1000)

    OP_24(0x0079, 0x5F)
    Sleep(1000)

    OP_24(0x0079, 0x64)
    WaitForThreadExit(0x0010, 0x0001)
    TerminateThread(0x000C, 0x01)
    Fade(500)
    OP_6D(15450, 0, 9560, 0)
    OP_67(0, 8440, -10000, 0)
    OP_6B(4120, 0)
    UnlockAchievement(0x66, 0x02, 0x00, 0x00)
    OP_6C(45000, 0)
    OP_6E(433, 0)
    OP_71(0x0007, 0x0004)
    OP_A1(0x000F, 0x0008)
    SetChrPos(0x000F, 18810, 5000, 10000, 90)
    OP_72(0x0008, 0x0004)
    OP_B0(0x0008, 0x14)
    OP_71(0x0008, 0x0020)
    OP_6F(0x0008, 830)
    OP_70(0x0008, 0x00000352)

    @scena.Lambda('lambda_07B1')
    def lambda_07B1():
        OP_6D(19500, 250, 8310, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_07B1)

    @scena.Lambda('lambda_07C9')
    def lambda_07C9():
        OP_67(0, 6470, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_07C9)

    UnlockAchievement(0x66, 0x03, 0x00, 0x00)

    @scena.Lambda('lambda_07E6')
    def lambda_07E6():
        OP_6E(364, 10000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_07E6)

    @scena.Lambda('lambda_07F6')
    def lambda_07F6():
        OP_8F(0x000F, 21810, -1000, 10000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_07F6)

    @scena.Lambda('lambda_0811')
    def lambda_0811():
        OP_8C(0x000F, 0, 10)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_0811)

    Sleep(1000)

    @scena.Lambda('lambda_0824')
    def lambda_0824():
        OP_8F(0x000F, 21810, -1000, 10000, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_0824)

    @scena.Lambda('lambda_083F')
    def lambda_083F():
        OP_8C(0x000F, 0, 12)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_083F)

    Sleep(1000)

    @scena.Lambda('lambda_0852')
    def lambda_0852():
        OP_8F(0x000F, 21810, -1000, 10000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_0852)

    @scena.Lambda('lambda_086D')
    def lambda_086D():
        OP_8C(0x000F, 0, 15)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_086D)

    Sleep(1000)

    @scena.Lambda('lambda_0880')
    def lambda_0880():
        OP_8F(0x000F, 21810, -1000, 10000, 800, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_0880)

    @scena.Lambda('lambda_089B')
    def lambda_089B():
        OP_8C(0x000F, 0, 12)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_089B)

    Sleep(1500)

    @scena.Lambda('lambda_08AE')
    def lambda_08AE():
        OP_8C(0x000F, 0, 10)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_08AE)

    @scena.Lambda('lambda_08BC')
    def lambda_08BC():
        OP_8F(0x000F, 21810, -1000, 10000, 500, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0000, lambda_08BC)

    WaitForThreadExit(0x000F, 0x0000)
    WaitForThreadExit(0x000F, 0x0001)
    CreateThread(0x000C, 0x00, 0x00, 0x0005)
    OP_72(0x0008, 0x0020)
    OP_D8(0x08, 0x012C)
    OP_6F(0x0008, 1220)
    OP_70(0x0008, 0x0000050A)
    Sleep(1000)

    OP_22(0x00FD, 0x00, 0x64)
    OP_73(0x0008)
    OP_71(0x0008, 0x0020)
    OP_6F(0x0008, 1290)
    OP_70(0x0008, 0x0000051D)
    Yield()
    Sleep(100)

    CreateThread(0x000E, 0x00, 0x00, 0x0007)
    Sleep(800)

    CreateThread(0x000D, 0x00, 0x00, 0x0006)
    Sleep(1500)

    CreateThread(0x000F, 0x00, 0x00, 0x0004)
    WaitForThreadExit(0x000D, 0x0000)
    Sleep(200)

    OP_DC()

    ChrTalk(
        0x000D,
        (
            '#0200300005V#252F#2P哟，久等了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000E, 0x0000)

    ChrTalk(
        0x000E,
        (
            '#0190300006V#851F#5P呵呵，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000C, 0x0000)

    ChrTalk(
        0x000C,
        (
            '#0210300007V#243F#6P哎呀……\n',
            '你们竟然会来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210300008V#240F我还以为\n',
            '会是莱维过来接我呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210300009V今天刮的什么风？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0190300010V#850F#5P呵呵，莱维\n',
            '正在陪着教授呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190300011V所以就改由我们\n',
            '来迎接你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0200300012V#250F#2P反正到下一阶段之前\n',
            '也没什么好做的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200300013V就当是来消磨时间吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0210300014V#241F#6P呵呵，说得倒轻巧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210300015V不过教授和莱维\n',
            '既然在一起……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210300016V这么说终于要进行\n',
            '最后的试验了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0200300017V#252F#2P呼呼，好像是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200300018V『福音计划』也\n',
            '终于到下一阶段了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0190300019V#853F#5P人偶和猎兵的准备也很顺利。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0190300020V#850F这样一来，如果『β』完成了，\n',
            '我看就会变得非常忙碌了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/E0800._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0xC57
@scena.Code('func_04_C57')
def func_04_C57():
    OP_72(0x0008, 0x0020)
    OP_6F(0x0008, 1300)
    OP_70(0x0008, 0x00000564)
    Sleep(500)

    OP_22(0x00FD, 0x00, 0x64)
    OP_73(0x0008)
    OP_71(0x0008, 0x0020)
    OP_6F(0x0008, 800)
    OP_70(0x0008, 0x00000384)

    Return()

# id: 0x0005 offset: 0xC8B
@scena.Code('func_05_C8B')
def func_05_C8B():
    OP_8E(0x00FE, 6980, 250, 9730, 3000, 0x00)
    OP_8E(0x00FE, 13810, 250, 6430, 2000, 0x00)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x0006 offset: 0xCBB
@scena.Code('func_06_CBB')
def func_06_CBB():
    SetChrChipByIndex(0x00FE, 14)
    SetChrSubChip(0x00FE, 0)
    SetChrFlags(0x00FE, 0x0040)
    SetChrBattleFlags(0x00FE, 0x0020)
    ClearChrFlags(0x00FE, 0x0080)
    OP_89(0x00FE, 21840, 2300, 9970, 0)
    OP_8E(0x00FE, 21810, 2300, 7610, 2000, 0x00)
    SetChrFlags(0x00FE, 0x0004)
    OP_8E(0x00FE, 19320, 2360, 6810, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0004)
    OP_8C(0x00FE, 270, 400)
    SetChrChipByIndex(0x00FE, 13)
    SetChrSubChip(0x00FE, 0)

    Return()

# id: 0x0007 offset: 0xD29
@scena.Code('func_07_D29')
def func_07_D29():
    SetChrFlags(0x00FE, 0x0040)
    SetChrBattleFlags(0x00FE, 0x0020)
    ClearChrFlags(0x00FE, 0x0080)
    OP_89(0x00FE, 21840, 2300, 9970, 0)
    OP_8E(0x00FE, 21810, 2300, 7610, 2000, 0x00)
    SetChrFlags(0x00FE, 0x0004)
    OP_8E(0x00FE, 18810, 2350, 7570, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0004)
    OP_8C(0x00FE, 270, 400)

    Return()

# id: 0x0008 offset: 0xD83
@scena.Code('func_08_D83')
def func_08_D83():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_6D(60, 0, -2000, 0)
    OP_67(0, 8910, -10000, 0)
    OP_6B(4370, 0)
    OP_6C(21000, 0)
    OP_6E(254, 0)
    OP_22(0x01C3, 0x00, 0x64)
    SetChrFlags(0x0008, 0x0004)
    SetChrPos(0x0008, 4059, 3450, 6990, 315)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0008, 0x0001)
    OP_82(0x80, 0x00)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_79(0x00, 0x0002)
    OP_79(0x01, 0x0002)
    OP_79(0x02, 0x0002)
    OP_79(0x03, 0x0002)
    OP_79(0x04, 0x0002)
    OP_7B()
    Sleep(1000)

    @scena.Lambda('lambda_0E41')
    def lambda_0E41():
        OP_6D(520, 0, 12220, 4000)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_0E41)

    OP_C8(0x0200, 0x0046, 'C_PLAC19._CH', 0x01, 0x03E8)
    FadeIn(1000, 0)
    WaitForThreadExit(0x000B, 0x0000)
    Sleep(1000)

    Fade(1000)
    OP_6D(1400, 0, 14000, 0)
    OP_67(0, 6630, -10000, 0)
    OP_6B(2029, 0)
    OP_6C(9000, 0)
    OP_6E(507, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0170340001V#231F#8P──这里是『怪盗绅士』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170340002V设置完成了。\n',
            '仪式开始之前会在此待命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C3605._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0xF45
@scena.Code('func_09_F45')
def func_09_F45():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_6D(1220, 950, 14960, 0)
    OP_67(0, 8600, -10000, 0)
    OP_6B(2830, 0)
    OP_6C(45000, 0)
    OP_6E(408, 0)
    SetChrPos(0x0008, 40, 950, 12620, 0)
    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0004)
    SetChrPos(0x0008, 4059, 3450, 6990, 315)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0008, 0x0001)
    OP_82(0x80, 0x00)
    OP_72(0x0000, 0x0008)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0008)
    OP_72(0x0003, 0x0008)
    OP_72(0x0004, 0x0008)
    OP_72(0x0000, 0x0020)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    OP_72(0x0004, 0x0020)
    OP_6F(0x0000, 60)
    OP_6F(0x0001, 60)
    OP_6F(0x0002, 60)
    OP_6F(0x0003, 60)
    OP_6F(0x0004, 60)
    OP_70(0x0000, 0x0000003C)
    OP_70(0x0001, 0x0000003C)
    OP_70(0x0002, 0x0000003C)
    OP_70(0x0003, 0x0000003C)
    LoadEffect(0x01, 'map\\\\mp061_00.eff')
    PlayEffect(0x01, 0xFF, 0x00FF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    OP_E8(0xD0, 0x07, 0x00, 0x00)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    OP_B0(0x0000, 0x50)
    OP_B0(0x0001, 0x50)
    OP_B0(0x0002, 0x50)
    OP_B0(0x0003, 0x50)
    OP_B0(0x0004, 0x50)
    OP_22(0x0099, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0x00000000)
    OP_73(0x0001)
    OP_22(0x0099, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0x00000000)
    OP_73(0x0002)
    OP_22(0x0099, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0x00000000)
    OP_73(0x0003)
    OP_22(0x0099, 0x00, 0x64)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0x00000000)
    OP_73(0x0004)
    OP_22(0x0099, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000000)
    OP_73(0x0000)
    OP_79(0x00, 0x0001)
    OP_79(0x01, 0x0001)
    OP_79(0x02, 0x0001)
    OP_79(0x03, 0x0001)
    OP_79(0x04, 0x0001)
    OP_7B()
    Fade(1000)
    OP_11(0xA0, 0xB4, 0xFF, 0x00017ED0, 0x00038E28, 0x00000000)
    OP_6D(-32090, 30000, -26260, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(300, 0)
    OP_0D()
    LoadEffect(0x00, 'map\\mp049_03.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, -32090, 30000, -26260, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0138, 0x00, 0x64)
    Sleep(3000)

    SetMapFlags(0x02000000)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_E8(0xE8, 0x03, 0x00, 0x00)
    OP_A2(0x10F1)
    NewScene('ED6_DT21/C3605._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x120C
@scena.Code('func_0A_120C')
def func_0A_120C():
    Call(0, 0x000B)
    Call(0, 0x000C)

    Return()

# id: 0x000B offset: 0x1215
@scena.Code('func_0B_1215')
def func_0B_1215():
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
        'loc_122C',
    )

    Call(0, 0x000D)
    Call(0, 0x000E)

    def _loc_122C(): pass

    label('loc_122C')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_124D'),
        (0x00000005, 'loc_1264'),
        (0x00000004, 'loc_127B'),
        (0x00000006, 'loc_1292'),
        (0x00000007, 'loc_12A9'),
        (0x00000008, 'loc_12C0'),
        (-1, 'loc_12D7'),
    )

    def _loc_124D(): pass

    label('loc_124D')

    OP_D2(0x000701D0, 0x000701DC, 0x0F)
    OP_D2(0x000701D1, 0x000701DD, 0x10)

    Jump('loc_12D7')

    def _loc_1264(): pass

    label('loc_1264')

    OP_D2(0x00070218, 0x00070224, 0x0F)
    OP_D2(0x00070219, 0x00070225, 0x10)

    Jump('loc_12D7')

    def _loc_127B(): pass

    label('loc_127B')

    OP_D2(0x00070200, 0x0007020C, 0x0F)
    OP_D2(0x00070201, 0x0007020D, 0x10)

    Jump('loc_12D7')

    def _loc_1292(): pass

    label('loc_1292')

    OP_D2(0x00070230, 0x0007023C, 0x0F)
    OP_D2(0x00070231, 0x0007023D, 0x10)

    Jump('loc_12D7')

    def _loc_12A9(): pass

    label('loc_12A9')

    OP_D2(0x00070248, 0x00070254, 0x0F)
    OP_D2(0x00070249, 0x00070255, 0x10)

    Jump('loc_12D7')

    def _loc_12C0(): pass

    label('loc_12C0')

    OP_D2(0x00270176, 0x00270183, 0x0F)
    OP_D2(0x00270177, 0x00270184, 0x10)

    Jump('loc_12D7')

    def _loc_12D7(): pass

    label('loc_12D7')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_12F8'),
        (0x00000005, 'loc_130F'),
        (0x00000004, 'loc_1326'),
        (0x00000006, 'loc_133D'),
        (0x00000007, 'loc_1354'),
        (0x00000008, 'loc_136B'),
        (-1, 'loc_1382'),
    )

    def _loc_12F8(): pass

    label('loc_12F8')

    OP_D2(0x000701D0, 0x000701DC, 0x11)
    OP_D2(0x000701D1, 0x000701DD, 0x12)

    Jump('loc_1382')

    def _loc_130F(): pass

    label('loc_130F')

    OP_D2(0x00070218, 0x00070224, 0x11)
    OP_D2(0x00070219, 0x00070225, 0x12)

    Jump('loc_1382')

    def _loc_1326(): pass

    label('loc_1326')

    OP_D2(0x00070200, 0x0007020C, 0x11)
    OP_D2(0x00070201, 0x0007020D, 0x12)

    Jump('loc_1382')

    def _loc_133D(): pass

    label('loc_133D')

    OP_D2(0x00070230, 0x0007023C, 0x11)
    OP_D2(0x00070231, 0x0007023D, 0x12)

    Jump('loc_1382')

    def _loc_1354(): pass

    label('loc_1354')

    OP_D2(0x00070248, 0x00070254, 0x11)
    OP_D2(0x00070249, 0x00070255, 0x12)

    Jump('loc_1382')

    def _loc_136B(): pass

    label('loc_136B')

    OP_D2(0x00270176, 0x00270183, 0x11)
    OP_D2(0x00270177, 0x00270184, 0x12)

    Jump('loc_1382')

    def _loc_1382(): pass

    label('loc_1382')

    OP_D2(0x0027026E, 0x00270278, 0x13)
    OP_6D(720, 0, -6220, 0)
    OP_67(0, 9730, -10000, 0)
    OP_6B(1820, 0)
    OP_6C(45000, 0)
    OP_6E(500, 0)
    SetChrPos(0x0008, 700, 950, 12150, 180)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0101, -650, -1750, -7480, 0)
    SetChrPos(0x0102, 740, -1750, -7480, 0)
    SetChrPos(0x00F8, -750, -1750, -7480, 0)
    SetChrPos(0x00F9, 820, -1750, -7480, 0)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrFlags(0x00F8, 0x0080)
    SetChrFlags(0x00F9, 0x0080)
    OP_71(0x0005, 0x0004)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_70(0x0000, 0x00000008)
    OP_70(0x0001, 0x00000008)
    OP_70(0x0002, 0x00000008)
    OP_70(0x0003, 0x00000008)
    OP_70(0x0004, 0x00000008)
    LoadEffect(0x01, 'map\\\\mp061_00.eff')
    PlayEffect(0x01, 0xFF, 0x00FF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_14DA')
    def lambda_14DA():
        OP_6D(600, 0, -350, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_14DA)

    ClearChrFlags(0x0101, 0x0080)

    @scena.Lambda('lambda_14F7')
    def lambda_14F7():
        OP_8E(0x00FE, -350, 0, -2009, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_14F7)

    Sleep(100)

    ClearChrFlags(0x0102, 0x0080)

    @scena.Lambda('lambda_151C')
    def lambda_151C():
        OP_8E(0x00FE, 950, 0, -2040, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_151C)

    Sleep(800)

    ClearChrFlags(0x00F8, 0x0080)

    @scena.Lambda('lambda_1541')
    def lambda_1541():
        OP_8E(0x00FE, -750, 0, -3590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_1541)

    Sleep(100)

    ClearChrFlags(0x00F9, 0x0080)

    @scena.Lambda('lambda_1566')
    def lambda_1566():
        OP_8E(0x00FE, 820, 0, -3520, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_1566)

    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010340774V#1020F#5P这、这里是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15F3',
    )

    ChrTalk(
        0x0109,
        (
            '#0180340775V#1063F#6P好像来到塔顶了……\n',
            '  ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16F4')

    def _loc_15F3(): pass

    label('loc_15F3')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1633',
    )

    ChrTalk(
        0x0106,
        (
            '#0050340776V#057F#6P好像来到塔顶了……\n',
            '  ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16F4')

    def _loc_1633(): pass

    label('loc_1633')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1673',
    )

    ChrTalk(
        0x0103,
        (
            '#0030340777V#022F#6P好像来到塔顶了……\n',
            '  ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16F4')

    def _loc_1673(): pass

    label('loc_1673')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16B3',
    )

    ChrTalk(
        0x0108,
        (
            '#0080340778V#072F#6P好像来到塔顶了……\n',
            '  ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16F4')

    def _loc_16B3(): pass

    label('loc_16B3')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_16F4',
    )

    ChrTalk(
        0x0107,
        (
            '#0070340779V#065F#6P好、好像来到塔顶了……\n',
            '  ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16F4(): pass

    label('loc_16F4')

    ChrTalk(
        0x0102,
        (
            '#0020340780V#1043F#5P包围塔顶的『结界』\n',
            '内侧吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '男人的声音',
        (
            '#0170340781V#4P呵呵……\n',
            '动作还挺快的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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
        'loc_17C4',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_1802')

    def _loc_17C4(): pass

    label('loc_17C4')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17EB',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_1802')

    def _loc_17EB(): pass

    label('loc_17EB')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_1802(): pass

    label('loc_1802')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_182E',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_186C')

    def _loc_182E(): pass

    label('loc_182E')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1855',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_186C')

    def _loc_1855(): pass

    label('loc_1855')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_186C(): pass

    label('loc_186C')

    Sleep(1000)

    OP_1D(0x6F)
    Sleep(500)

    @scena.Lambda('lambda_187E')
    def lambda_187E():
        OP_6D(1800, 0, 8900, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_187E)

    @scena.Lambda('lambda_1896')
    def lambda_1896():
        OP_67(0, 5400, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1896)

    @scena.Lambda('lambda_18AE')
    def lambda_18AE():
        OP_6B(2520, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_18AE)

    Sleep(2500)

    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 3)

    @scena.Lambda('lambda_18CD')
    def lambda_18CD():
        OP_8E(0x00FE, -700, 0, 4650, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_18CD)

    Sleep(200)

    SetChrSubChip(0x0102, 0)
    SetChrChipByIndex(0x0102, 5)

    @scena.Lambda('lambda_18F7')
    def lambda_18F7():
        OP_8E(0x00FE, 700, 0, 4520, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_18F7)

    Sleep(200)

    SetChrSubChip(0x00F8, 0)
    SetChrChipByIndex(0x00F8, 15)

    @scena.Lambda('lambda_1921')
    def lambda_1921():
        OP_8E(0x00FE, -800, 0, 2930, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_1921)

    Sleep(200)

    SetChrSubChip(0x00F9, 0)
    SetChrChipByIndex(0x00F9, 17)

    @scena.Lambda('lambda_194B')
    def lambda_194B():
        OP_8E(0x00FE, 800, 0, 2800, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_194B)

    WaitForThreadExit(0x00F9, 0x0001)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010340782V#1002F#6P果然来了啊……\n',
            '这个变态假面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A91',
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
            TXT(0x00, '【◆布卢布兰的挑战全部完成】\n'),
            TXT(0x01, '【◆布卢布兰的挑战完成１个以上】\n'),
            TXT(0x02, '【◆无视布卢布兰的挑战】\n'),
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
        (0x00000000, 'loc_1A43'),
        (0x00000001, 'loc_1A5A'),
        (0x00000002, 'loc_1A71'),
        (-1, 'loc_1A88'),
    )

    def _loc_1A43(): pass

    label('loc_1A43')

    OP_28(0x006C, 0x04, 0x10)
    OP_28(0x0077, 0x04, 0x10)
    OP_28(0x0078, 0x04, 0x10)
    OP_28(0x00C4, 0x04, 0x10)

    Jump('loc_1A88')

    def _loc_1A5A(): pass

    label('loc_1A5A')

    OP_28(0x006C, 0x04, 0x10)
    OP_28(0x0077, 0x03, 0x10)
    OP_28(0x0078, 0x03, 0x10)
    OP_28(0x00C4, 0x03, 0x10)

    Jump('loc_1A88')

    def _loc_1A71(): pass

    label('loc_1A71')

    OP_28(0x006C, 0x03, 0x10)
    OP_28(0x0077, 0x03, 0x10)
    OP_28(0x0078, 0x03, 0x10)
    OP_28(0x00C4, 0x03, 0x10)

    Jump('loc_1A88')

    def _loc_1A88(): pass

    label('loc_1A88')

    FadeIn(300, 0)

    def _loc_1A91(): pass

    label('loc_1A91')

    If(
        (
            (Expr.Eval, "OP_29(0x006C, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1AA5',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1AA5(): pass

    label('loc_1AA5')

    If(
        (
            (Expr.Eval, "OP_29(0x0077, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1AB9',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1AB9(): pass

    label('loc_1AB9')

    If(
        (
            (Expr.Eval, "OP_29(0x0078, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1ACD',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1ACD(): pass

    label('loc_1ACD')

    If(
        (
            (Expr.Eval, "OP_29(0x00C4, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1AE1',
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    def _loc_1AE1(): pass

    label('loc_1AE1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BA1',
    )

    ChrTalk(
        0x0008,
        (
            '#0170340783V#232F呼……\n',
            '别说得那么难听嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170340784V再怎么说，你们也完成过我的挑战。\n',
            '连这点风度都没有的话可是很伤脑筋的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340785V#1019F#6P要、要你多管闲事！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CF9')

    def _loc_1BA1(): pass

    label('loc_1BA1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Geq,
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1C66',
    )

    ChrTalk(
        0x0008,
        (
            '#0170340786V#230F哎呀哎呀，说得这么难听。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170340787V你们不是也曾响应过我的挑战吗。\n',
            '表现出一点风度来也不算什么吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340788V#1019F#6P没、没风度真是抱歉啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CF9')

    def _loc_1C66(): pass

    label('loc_1C66')

    ChrTalk(
        0x0008,
        (
            '#0170340789V#231F哼，说得真难听。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170340790V不但没有胆量响应我的挑战，\n',
            '就连一点风度也完全没有吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340791V#1019F#6P什、什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CF9(): pass

    label('loc_1CF9')

    ChrTalk(
        0x0008,
        (
            '#0170340792V#230F这个暂且不说……\n',
            '咱们还真是好久不见了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170340793V#231F『漆黑之牙』──\n',
            '约修亚·阿斯特雷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340794V#1035F#4P……没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340795V#1042F让我疑惑的是，\n',
            '为什么你会配合教授的计划……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0170340796V#230F呼呼，别人先姑且不论，\n',
            '我自己是因为有点兴趣。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170340797V#233F这个叫利贝尔的国家\n',
            '洋溢着不可思议的气质。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170340798V人，土地，甚至空气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170340799V#231F这种气质是真是假\n',
            '我想要亲自确认一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170340800V因为越是面临困难，\n',
            '它就越会绽放光芒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340801V#1042F#4P原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340802V#1035F某种程度上，你和教授\n',
            '可能很像。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0170340803V#231F哈哈，我所追求的是美，\n',
            '而教授却明显不同。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170340804V这点你也应该知道才对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340805V#1042F#4P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25BD',
    )

    ChrTalk(
        0x0008,
        (
            '#0170340806V#230F不过，没想到公主殿下\n',
            '会来到这种地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170340807V莫非是已经决定接受\n',
            '我的崇敬之心了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060340808V#047F#4P很遗憾……\n',
            '我不是那种会\n',
            '响应你期望的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060340809V#043F如果真是高尚的人\n',
            '又怎会感到迷惘呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060340810V将『埃尔赛尤』还给陛下的时候，\n',
            '也是我必须作出回答的时候。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060340811V#049F我……我很害怕这一刻的到来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340812V#1026F#5P科洛丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340813V#1043F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0170340814V#231F啊哈哈！\n',
            '那股恐惧正是高尚的证据！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170340815V这是那些在地上匍匐的蝼蚁们\n',
            '向往不已的翅膀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 2)
    OP_0D()
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 19)
    OP_99(0x0008, 0x00, 0x0E, 0x000007D0)

    @scena.Lambda('lambda_223C')
    def lambda_223C():
        OP_6D(1280, 0, 7850, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_223C)

    @scena.Lambda('lambda_2254')
    def lambda_2254():
        OP_67(0, 5250, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2254)

    @scena.Lambda('lambda_226C')
    def lambda_226C():
        OP_6B(2520, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_226C)

    SetChrPos(0x0009, 6410, 8800, 5150, 270)
    SetChrPos(0x000A, -6950, 8800, 3250, 90)
    OP_9F(0x0009, 0xFF, 0x00, 0x00, 0x00, 0x00000000)
    OP_9F(0x000A, 0xFF, 0x00, 0x00, 0x00, 0x00000000)
    SetChrFlags(0x0009, 0x0004)
    SetChrFlags(0x000A, 0x0004)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)

    @scena.Lambda('lambda_22C8')
    def lambda_22C8():
        OP_96(0x00FE, 0x0000190A, 0x00000320, 0x0000141E, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_22C8)

    OP_9F(0x0009, 0x64, 0x64, 0xFF, 0xFF, 0x00000064)
    OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000064)
    WaitForThreadExit(0x0009, 0x0001)
    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x000001F4, 0x00000BB8, 0x00000064)
    CreateThread(0x0009, 0x03, 0x00, 0x0002)

    @scena.Lambda('lambda_231E')
    def lambda_231E():
        OP_96(0x00FE, 0xFFFFE4DA, 0x00000320, 0x00000CB2, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_231E)

    OP_9F(0x000A, 0x64, 0x64, 0xFF, 0xFF, 0x00000064)
    OP_9F(0x000A, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000064)
    WaitForThreadExit(0x000A, 0x0001)
    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x000001F4, 0x00000BB8, 0x00000064)
    CreateThread(0x000A, 0x03, 0x00, 0x0002)
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
        'loc_23CD',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_240B')

    def _loc_23CD(): pass

    label('loc_23CD')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_23F4',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_240B')

    def _loc_23F4(): pass

    label('loc_23F4')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_240B(): pass

    label('loc_240B')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2437',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_2475')

    def _loc_2437(): pass

    label('loc_2437')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_245E',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_2475')

    def _loc_245E(): pass

    label('loc_245E')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_2475(): pass

    label('loc_2475')

    Sleep(1000)

    @scena.Lambda('lambda_2480')
    def lambda_2480():
        OP_8C(0x00FE, 270, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2480)

    Sleep(50)

    @scena.Lambda('lambda_2493')
    def lambda_2493():
        OP_8C(0x00FE, 90, 600)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2493)

    Sleep(50)

    @scena.Lambda('lambda_24A6')
    def lambda_24A6():
        OP_8C(0x00FE, 270, 600)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_24A6)

    Sleep(50)

    @scena.Lambda('lambda_24B9')
    def lambda_24B9():
        OP_8C(0x00FE, 90, 600)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_24B9)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0105,
        (
            '#0060340816V#042F#6P！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340817V#1020F#5P哇哇！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340818V#1046F#6P强袭用人形兵器——\n',
            '『跳梁小丑』！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x00D8, 0x00, 0x64)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 2)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0170340819V#231F来吧，让我看看！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170340820V那道连覆满阴影的大地\n',
            '也能照亮的光辉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CA4')

    def _loc_25BD(): pass

    label('loc_25BD')

    ChrTalk(
        0x0008,
        (
            '#0170340821V#232F话说回来，你们\n',
            '也该稍微机警一点吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170340822V你们收到了报告\n',
            '应该知道我在这里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170340823V既然如此还带公主殿下来\n',
            '也太没脑子了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340824V#1019F#6P开、开什么玩笑！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340825V谁要把科洛丝给你这种人啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_26F7',
    )

    ChrTalk(
        0x0107,
        (
            '#0070340826V#065F#4P啊呜……\n',
            '(怎、怎么会有这样的人？)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26F7(): pass

    label('loc_26F7')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2749',
    )

    ChrTalk(
        0x0108,
        (
            '#0080340827V#075F#4P怎么说呢……\n',
            '是非常厚颜无耻的大哥哥呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_282B')

    def _loc_2749(): pass

    label('loc_2749')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2797',
    )

    ChrTalk(
        0x0103,
        (
            '#0030340828V#025F#4P真是的……\n',
            '厚颜无耻也要有个限度吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_282B')

    def _loc_2797(): pass

    label('loc_2797')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_27E1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050340829V#551F#4P哼……\n',
            '厚颜无耻也要有个限度吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_282B')

    def _loc_27E1(): pass

    label('loc_27E1')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_282B',
    )

    ChrTalk(
        0x0109,
        (
            '#0180340830V#1068F#4P怎么说呢……\n',
            '算是非常厚颜无耻吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_282B(): pass

    label('loc_282B')

    ChrTalk(
        0x0102,
        (
            '#0020340831V#1035F#4P布卢布兰……\n',
            '游戏就到此为止吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340832V#1042F我们是为了阻止\n',
            '『结社』的计划而来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340833V那么彼此之间，\n',
            '要做的事只有一件吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0170340834V#231F呵呵……没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    OP_22(0x00D5, 0x00, 0x64)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 2)
    OP_0D()
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 19)
    OP_99(0x0008, 0x00, 0x0E, 0x000007D0)

    @scena.Lambda('lambda_2927')
    def lambda_2927():
        OP_6D(1280, 0, 7850, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2927)

    @scena.Lambda('lambda_293F')
    def lambda_293F():
        OP_67(0, 5250, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_293F)

    @scena.Lambda('lambda_2957')
    def lambda_2957():
        OP_6B(2520, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2957)

    SetChrPos(0x0009, 6410, 8800, 5150, 270)
    SetChrPos(0x000A, -6950, 8800, 3250, 90)
    OP_9F(0x0009, 0xFF, 0x00, 0x00, 0x00, 0x00000000)
    OP_9F(0x000A, 0xFF, 0x00, 0x00, 0x00, 0x00000000)
    SetChrFlags(0x0009, 0x0004)
    SetChrFlags(0x000A, 0x0004)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)

    @scena.Lambda('lambda_29B3')
    def lambda_29B3():
        OP_96(0x00FE, 0x0000190A, 0x00000320, 0x0000141E, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_29B3)

    OP_9F(0x0009, 0x64, 0x64, 0xFF, 0xFF, 0x00000064)
    OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000064)
    WaitForThreadExit(0x0009, 0x0001)
    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x000001F4, 0x00000BB8, 0x00000064)
    CreateThread(0x0009, 0x03, 0x00, 0x0002)

    @scena.Lambda('lambda_2A09')
    def lambda_2A09():
        OP_96(0x00FE, 0xFFFFE4DA, 0x00000320, 0x00000CB2, 0x000003E8, 0x00001388)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2A09)

    OP_9F(0x000A, 0x64, 0x64, 0xFF, 0xFF, 0x00000064)
    OP_9F(0x000A, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000064)
    WaitForThreadExit(0x000A, 0x0001)
    OP_22(0x00C8, 0x00, 0x64)
    OP_7C(0x00000000, 0x000001F4, 0x00000BB8, 0x00000064)
    CreateThread(0x000A, 0x03, 0x00, 0x0002)
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
        'loc_2AB8',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_2AF6')

    def _loc_2AB8(): pass

    label('loc_2AB8')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2ADF',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_2AF6')

    def _loc_2ADF(): pass

    label('loc_2ADF')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_2AF6(): pass

    label('loc_2AF6')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B22',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_2B60')

    def _loc_2B22(): pass

    label('loc_2B22')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B49',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_2B60')

    def _loc_2B49(): pass

    label('loc_2B49')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_2B60(): pass

    label('loc_2B60')

    Sleep(1000)

    @scena.Lambda('lambda_2B6B')
    def lambda_2B6B():
        OP_8C(0x00FE, 270, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2B6B)

    Sleep(50)

    @scena.Lambda('lambda_2B7E')
    def lambda_2B7E():
        OP_8C(0x00FE, 90, 600)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2B7E)

    Sleep(50)

    @scena.Lambda('lambda_2B91')
    def lambda_2B91():
        OP_8C(0x00FE, 270, 600)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_2B91)

    Sleep(50)

    @scena.Lambda('lambda_2BA4')
    def lambda_2BA4():
        OP_8C(0x00FE, 90, 600)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2BA4)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010340817V#1020F#5P哇哇！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340818V#1046F#6P强袭用人形兵器——\n',
            '『跳梁小丑』！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0x00D8, 0x00, 0x64)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 2)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0170340837V#231F『漆黑之牙』……\n',
            '这还是第一次跟你比试吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170340838V加上『剑圣』的女儿\n',
            '就让我尽情地享受吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_2CA4(): pass

    label('loc_2CA4')

    @scena.Lambda('lambda_2CAA')
    def lambda_2CAA():
        OP_6D(440, 0, 5440, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2CAA)

    @scena.Lambda('lambda_2CC2')
    def lambda_2CC2():
        OP_6B(2000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2CC2)

    OP_22(0x023B, 0x00, 0x64)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 9)
    OP_7D(0x00, 0x0008, 0x0032, 0x01F4)

    @scena.Lambda('lambda_2CE9')
    def lambda_2CE9():
        OP_96(0x00FE, 0x0000001E, 0x00000000, 0x000018CE, 0x000005DC, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2CE9)

    Sleep(100)

    TerminateThread(0x0009, 0x03)
    SetChrFlags(0x0009, 0x1000)
    SetChrSubChip(0x0009, 0)
    SetChrChipByIndex(0x0009, 8)

    @scena.Lambda('lambda_2D1F')
    def lambda_2D1F():
        OP_8E(0x00FE, 1530, 800, 4420, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2D1F)

    TerminateThread(0x000A, 0x03)
    SetChrFlags(0x000A, 0x1000)
    SetChrSubChip(0x000A, 0)
    SetChrChipByIndex(0x000A, 8)

    @scena.Lambda('lambda_2D4D')
    def lambda_2D4D():
        OP_8E(0x00FE, -2640, 800, 3600, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_2D4D)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x0008, 0x01)
    OP_7D(0x01, 0x0008, 0x0000, 0x0000)
    Battle(0x00000454, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_2D99'),
        (-1, 'loc_2D9E'),
    )

    def _loc_2D99(): pass

    label('loc_2D99')

    OP_B4(0x00)

    Jump('loc_2D9E')

    def _loc_2D9E(): pass

    label('loc_2D9E')

    Return()

# id: 0x000C offset: 0x2D9F
@scena.Code('func_0C_2D9F')
def func_0C_2D9F():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_6D(330, 200, 12720, 0)
    OP_67(0, 3720, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(0, 0)
    OP_6E(501, 0)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000A, 0x01)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    OP_71(0x0005, 0x0004)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_70(0x0000, 0x00000008)
    OP_70(0x0001, 0x00000008)
    OP_70(0x0002, 0x00000008)
    OP_70(0x0003, 0x00000008)
    OP_70(0x0004, 0x00000008)
    OP_7B()
    LoadEffect(0x01, 'map\\\\mp061_00.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    SetChrPos(0x0008, 700, 950, 12150, 180)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0101, -530, 0, 5830, 0)
    SetChrPos(0x0102, 660, 0, 5640, 0)
    SetChrPos(0x00F8, -790, 0, 3690, 0)
    SetChrPos(0x00F9, 920, 0, 3630, 0)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_2F0E'),
        (0x00000005, 'loc_2F1B'),
        (0x00000004, 'loc_2F28'),
        (0x00000006, 'loc_2F35'),
        (0x00000007, 'loc_2F42'),
        (0x00000008, 'loc_2F4F'),
        (-1, 'loc_2F5C'),
    )

    def _loc_2F0E(): pass

    label('loc_2F0E')

    OP_D2(0x000701D0, 0x000701DC, 0x0F)

    Jump('loc_2F5C')

    def _loc_2F1B(): pass

    label('loc_2F1B')

    OP_D2(0x00070218, 0x00070224, 0x0F)

    Jump('loc_2F5C')

    def _loc_2F28(): pass

    label('loc_2F28')

    OP_D2(0x00070200, 0x0007020C, 0x0F)

    Jump('loc_2F5C')

    def _loc_2F35(): pass

    label('loc_2F35')

    OP_D2(0x00070230, 0x0007023C, 0x0F)

    Jump('loc_2F5C')

    def _loc_2F42(): pass

    label('loc_2F42')

    OP_D2(0x00070248, 0x00070254, 0x0F)

    Jump('loc_2F5C')

    def _loc_2F4F(): pass

    label('loc_2F4F')

    OP_D2(0x00270176, 0x00270183, 0x0F)

    Jump('loc_2F5C')

    def _loc_2F5C(): pass

    label('loc_2F5C')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_2F7D'),
        (0x00000005, 'loc_2F8A'),
        (0x00000004, 'loc_2F97'),
        (0x00000006, 'loc_2FA4'),
        (0x00000007, 'loc_2FB1'),
        (0x00000008, 'loc_2FBE'),
        (-1, 'loc_2FCB'),
    )

    def _loc_2F7D(): pass

    label('loc_2F7D')

    OP_D2(0x000701D0, 0x000701DC, 0x11)

    Jump('loc_2FCB')

    def _loc_2F8A(): pass

    label('loc_2F8A')

    OP_D2(0x00070218, 0x00070224, 0x11)

    Jump('loc_2FCB')

    def _loc_2F97(): pass

    label('loc_2F97')

    OP_D2(0x00070200, 0x0007020C, 0x11)

    Jump('loc_2FCB')

    def _loc_2FA4(): pass

    label('loc_2FA4')

    OP_D2(0x00070230, 0x0007023C, 0x11)

    Jump('loc_2FCB')

    def _loc_2FB1(): pass

    label('loc_2FB1')

    OP_D2(0x00070248, 0x00070254, 0x11)

    Jump('loc_2FCB')

    def _loc_2FBE(): pass

    label('loc_2FBE')

    OP_D2(0x00270176, 0x00270183, 0x11)

    Jump('loc_2FCB')

    def _loc_2FCB(): pass

    label('loc_2FCB')

    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 2)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 3)
    SetChrSubChip(0x0102, 0)
    SetChrChipByIndex(0x0102, 5)
    SetChrSubChip(0x00F8, 0)
    SetChrChipByIndex(0x00F8, 15)
    SetChrSubChip(0x00F9, 0)
    SetChrChipByIndex(0x00F9, 17)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0170340839V#230F#5P呼……\n',
            '比我预料中的还要能干。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170340840V#231F那么我也要动真格的了──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    OP_22(0x0099, 0x00, 0x64)
    OP_23(0x00EB)
    OP_20(0x000007D0)
    Fade(500)
    OP_6B(2500, 0)
    OP_82(0x01, 0x02)
    OP_82(0x81, 0x02)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_82(0x83, 0x02)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_79(0x00, 0x0002)
    OP_79(0x01, 0x0002)
    OP_79(0x02, 0x0002)
    OP_79(0x03, 0x0002)
    OP_79(0x04, 0x0002)
    OP_7B()
    Sleep(500)

    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    OP_72(0x0001, 0x0020)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 0x0000003C)
    Sleep(100)

    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 0x0000003C)
    Sleep(100)

    OP_72(0x0003, 0x0020)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 0x0000003C)
    Sleep(100)

    OP_72(0x0004, 0x0020)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 0x0000003C)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x0008, 0, 600)
    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0170340841V#233F#6P唔！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340842V#1042F#6P！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    OP_6D(5030, 3860, 11650, 0)
    OP_67(0, 1590, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(43000, 0)
    OP_6E(363, 0)
    OP_0D()

    @scena.Lambda('lambda_323C')
    def lambda_323C():
        OP_6B(5500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_323C)

    Sleep(500)

    OP_22(0x0139, 0x00, 0x64)
    LoadEffect(0x02, 'map\\mp049_02.eff')
    PlayEffect(0x02, 0x02, 0x00FF, 0, 0, 6720, 0, 0, 0, 550, 550, 550, 0x00FF, 0, 0, 0, 0)
    Sleep(800)

    OP_82(0x80, 0x00)
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C0707._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x32BD
@scena.Code('func_0D_32BD')
def func_0D_32BD():
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
        (0x00000000, 'loc_3337'),
        (0x00000001, 'loc_333D'),
        (-1, 'loc_3343'),
    )

    def _loc_3337(): pass

    label('loc_3337')

    OP_A2(0x1200)

    Jump('loc_3343')

    def _loc_333D(): pass

    label('loc_333D')

    OP_A2(0x1201)

    Jump('loc_3343')

    def _loc_3343(): pass

    label('loc_3343')

    Return()

# id: 0x000E offset: 0x3344
@scena.Code('func_0E_3344')
def func_0E_3344():
    FadeOut(0, 0, -1)
    OP_6D(-66940, 250, 36210, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
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
            0x0006,
            0x0004,
            0x0007,
            0x0008,
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
