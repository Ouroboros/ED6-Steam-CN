import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1400_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1400   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1400.x'
    header.mapIndex       = 1
    header.bgm            = 16
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
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

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH02080._CH', 'ED6_DT07/CH02080P._CP'),
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
        ('ED6_DT07/CH01650._CH', 'ED6_DT07/CH01650P._CP'),
        ('ED6_DT06/CH20045._CH', 'ED6_DT06/CH20045P._CP'),
        ('ED6_DT06/CH20039._CH', 'ED6_DT06/CH20039P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '卫兵',
            x                   = 8250,
            z                   = 0,
            y                   = -12000,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '卫兵',
            x                   = -2400,
            z                   = 0,
            y                   = -7500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '卡尔科斯',
            x                   = -2100,
            z                   = 0,
            y                   = -20100,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '卡尔科斯',
            x                   = 2500,
            z                   = 0,
            y                   = -7500,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '金发青年',
            x                   = 19250,
            z                   = 0,
            y                   = 14430,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '摩尔根将军',
            x                   = 209710,
            z                   = 0,
            y                   = 11740,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '亚妮拉丝',
            x                   = -10600,
            z                   = 0,
            y                   = -29900,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = -9000,
            z                   = 11750,
            y                   = 3000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 9000,
            z                   = 11750,
            y                   = 3000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '目标用摄像机',
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
        ScenaNpcData(
            name                = '钢壁之路方向',
            x                   = 11890,
            z                   = 40,
            y                   = -60460,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x24A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x24A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 8810,
            y           = -1000,
            z           = -12035,
            range       = 3000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000013,
        ),
        ScenaEventData(
            x           = 3830,
            y           = -1000,
            z           = -43570,
            range       = 10270,
            dword_10    = 0x00000BB8,
            dword_14    = 0xFFFF5880,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000001E,
        ),
    )

# id: 0x10004 offset: 0x28A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x28A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_2B4',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0008)
    ChrSetPos(0x0008, 8230, 0, -10540, 270)

    Jump('loc_30A')

    def _loc_2B4(): pass

    label('loc_2B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_2CF',
    )

    ChrSetPos(0x0008, 8230, 0, -10540, 270)

    Jump('loc_30A')

    def _loc_2CF(): pass

    label('loc_2CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_2D9',
    )

    Jump('loc_30A')

    def _loc_2D9(): pass

    label('loc_2D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 7, 0x317)),
            Expr.Return,
        ),
        'loc_2E8',
    )

    ChrClearFlags(0x000E, 0x0080)

    Jump('loc_30A')

    def _loc_2E8(): pass

    label('loc_2E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_2F2',
    )

    Jump('loc_30A')

    def _loc_2F2(): pass

    label('loc_2F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 1, 0x311)),
            Expr.Return,
        ),
        'loc_30A',
    )

    ChrSetPos(0x0008, 8300, 0, -10500, 180)

    def _loc_30A(): pass

    label('loc_30A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_31D',
    )

    MapSetFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_0E_2587)

    def _loc_31D(): pass

    label('loc_31D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_330',
    )

    MapSetFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_14_2C1E)

    def _loc_330(): pass

    label('loc_330')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_33C'),
        (-1, 'loc_34E'),
    )

    def _loc_33C(): pass

    label('loc_33C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 5, 0x30D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_34B',
    )

    SetScenaFlags(ScenaFlag(0x0061, 5, 0x30D))
    Event(0, func_0D_1FF6)

    def _loc_34B(): pass

    label('loc_34B')

    Jump('loc_34E')

    def _loc_34E(): pass

    label('loc_34E')

    Return()

# id: 0x0001 offset: 0x34F
@scena.Code('func_01_34F')
def func_01_34F():
    OP_16(0x02, 4000, -122000, -130000, 196677)
    OP_6F(0x0003, 0)
    OP_72(0x0003, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_377',
    )

    Jump('loc_392')

    def _loc_377(): pass

    label('loc_377')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 1, 0x311)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_386',
    )

    Jump('loc_392')

    def _loc_386(): pass

    label('loc_386')

    OP_6F(0x0001, 0)
    OP_72(0x0001, 0x0010)

    def _loc_392(): pass

    label('loc_392')

    Return()

# id: 0x0002 offset: 0x393
@scena.Code('func_02_393')
def func_02_393():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3A8',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_393')

    def _loc_3A8(): pass

    label('loc_3A8')

    Return()

# id: 0x0003 offset: 0x3A9
@scena.Code('func_03_3A9')
def func_03_3A9():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3CC',
    )

    OP_8D(0x00FE, -7000, -13000, 3500, -25300, 2000)

    Jump('func_03_3A9')

    def _loc_3CC(): pass

    label('loc_3CC')

    Return()

# id: 0x0004 offset: 0x3CD
@scena.Code('func_04_3CD')
def func_04_3CD():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3F0',
    )

    OP_8D(0x00FE, -15100, -32400, -9800, -27500, 2000)

    Jump('func_04_3CD')

    def _loc_3F0(): pass

    label('loc_3F0')

    Return()

# id: 0x0005 offset: 0x3F1
@scena.Code('func_05_3F1')
def func_05_3F1():
    EventBegin(0x00)

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
        10,
        0,
        (
            TXT(0x00, '④到达哈肯门。\n'),
            TXT(0x01, '③和梅贝尔会面。\n'),
            TXT(0x02, '⑥和摩尔根将军会面。\n'),
            TXT(0x03, '⑧赶往拉文努村。\n'),
            TXT(0x04, '<874C>被王国军释放。\n'),
            TXT(0x05, '<874D>赶往湖畔旅馆。\n'),
            TXT(0x06, '标志解除光线\n'),
            TXT(0x07, '取消\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_4B3'),
        (0x00000001, 'loc_4FC'),
        (0x00000002, 'loc_523'),
        (0x00000003, 'loc_55A'),
        (0x00000004, 'loc_596'),
        (0x00000005, 'loc_5E1'),
        (0x00000006, 'loc_62F'),
        (-1, 'loc_673'),
    )

    def _loc_4B3(): pass

    label('loc_4B3')

    SetScenaFlags(ScenaFlag(0x0043, 1, 0x219))
    SetScenaFlags(ScenaFlag(0x0040, 2, 0x202))
    SetScenaFlags(ScenaFlag(0x0040, 3, 0x203))
    SetScenaFlags(ScenaFlag(0x0040, 5, 0x205))
    SetScenaFlags(ScenaFlag(0x0040, 7, 0x207))
    SetScenaFlags(ScenaFlag(0x0042, 7, 0x217))
    SetScenaFlags(ScenaFlag(0x0040, 6, 0x206))
    SetScenaFlags(ScenaFlag(0x0042, 2, 0x212))
    SetScenaFlags(ScenaFlag(0x0042, 3, 0x213))
    SetScenaFlags(ScenaFlag(0x0047, 1, 0x239))
    SetScenaFlags(ScenaFlag(0x0049, 7, 0x24F))
    SetScenaFlags(ScenaFlag(0x004B, 1, 0x259))
    SetScenaFlags(ScenaFlag(0x004C, 1, 0x261))
    SetScenaFlags(ScenaFlag(0x0060, 1, 0x301))
    SetScenaFlags(ScenaFlag(0x0061, 4, 0x30C))

    ChrTalk(
        0x0101,
        (
            '#000F④到达哈肯门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_68A')

    def _loc_4FC(): pass

    label('loc_4FC')

    SetScenaFlags(ScenaFlag(0x0060, 1, 0x301))
    SetScenaFlags(ScenaFlag(0x0061, 2, 0x30A))
    SetScenaFlags(ScenaFlag(0x0061, 3, 0x30B))

    ChrTalk(
        0x0101,
        (
            '#000F③和梅贝尔会面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_68A')

    def _loc_523(): pass

    label('loc_523')

    SetScenaFlags(ScenaFlag(0x0060, 1, 0x301))
    SetScenaFlags(ScenaFlag(0x0061, 2, 0x30A))
    SetScenaFlags(ScenaFlag(0x0061, 3, 0x30B))
    SetScenaFlags(ScenaFlag(0x0061, 4, 0x30C))
    SetScenaFlags(ScenaFlag(0x0062, 0, 0x310))
    SetScenaFlags(ScenaFlag(0x0062, 2, 0x312))
    SetScenaFlags(ScenaFlag(0x0062, 3, 0x313))

    ChrTalk(
        0x0101,
        (
            '#000F⑥和摩尔根将军会面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_68A')

    def _loc_55A(): pass

    label('loc_55A')

    SetScenaFlags(ScenaFlag(0x0060, 1, 0x301))
    SetScenaFlags(ScenaFlag(0x0061, 2, 0x30A))
    SetScenaFlags(ScenaFlag(0x0061, 3, 0x30B))
    SetScenaFlags(ScenaFlag(0x0061, 4, 0x30C))
    SetScenaFlags(ScenaFlag(0x0062, 0, 0x310))
    SetScenaFlags(ScenaFlag(0x0062, 2, 0x312))
    SetScenaFlags(ScenaFlag(0x0062, 4, 0x314))
    SetScenaFlags(ScenaFlag(0x0062, 7, 0x317))
    SetScenaFlags(ScenaFlag(0x0063, 0, 0x318))
    SetScenaFlags(ScenaFlag(0x0062, 3, 0x313))

    ChrTalk(
        0x0101,
        (
            '#000F⑧赶往拉文努村。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_68A')

    def _loc_596(): pass

    label('loc_596')

    SetScenaFlags(ScenaFlag(0x0060, 1, 0x301))
    SetScenaFlags(ScenaFlag(0x0061, 2, 0x30A))
    SetScenaFlags(ScenaFlag(0x0061, 3, 0x30B))
    SetScenaFlags(ScenaFlag(0x0061, 4, 0x30C))
    SetScenaFlags(ScenaFlag(0x0062, 0, 0x310))
    SetScenaFlags(ScenaFlag(0x0062, 2, 0x312))
    SetScenaFlags(ScenaFlag(0x0062, 4, 0x314))
    SetScenaFlags(ScenaFlag(0x0062, 7, 0x317))
    SetScenaFlags(ScenaFlag(0x0063, 0, 0x318))
    SetScenaFlags(ScenaFlag(0x0063, 3, 0x31B))
    SetScenaFlags(ScenaFlag(0x0063, 4, 0x31C))
    SetScenaFlags(ScenaFlag(0x0063, 5, 0x31D))
    SetScenaFlags(ScenaFlag(0x0063, 6, 0x31E))
    SetScenaFlags(ScenaFlag(0x0065, 3, 0x32B))
    SetScenaFlags(ScenaFlag(0x0062, 3, 0x313))

    ChrTalk(
        0x0101,
        (
            '#000F<874C>被王国军释放。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_68A')

    def _loc_5E1(): pass

    label('loc_5E1')

    SetScenaFlags(ScenaFlag(0x0060, 1, 0x301))
    SetScenaFlags(ScenaFlag(0x0061, 2, 0x30A))
    SetScenaFlags(ScenaFlag(0x0061, 3, 0x30B))
    SetScenaFlags(ScenaFlag(0x0061, 4, 0x30C))
    SetScenaFlags(ScenaFlag(0x0062, 0, 0x310))
    SetScenaFlags(ScenaFlag(0x0062, 2, 0x312))
    SetScenaFlags(ScenaFlag(0x0062, 4, 0x314))
    SetScenaFlags(ScenaFlag(0x0062, 7, 0x317))
    SetScenaFlags(ScenaFlag(0x0063, 0, 0x318))
    SetScenaFlags(ScenaFlag(0x0063, 3, 0x31B))
    SetScenaFlags(ScenaFlag(0x0063, 4, 0x31C))
    SetScenaFlags(ScenaFlag(0x0063, 5, 0x31D))
    SetScenaFlags(ScenaFlag(0x0063, 6, 0x31E))
    SetScenaFlags(ScenaFlag(0x0065, 3, 0x32B))
    SetScenaFlags(ScenaFlag(0x0067, 2, 0x33A))
    SetScenaFlags(ScenaFlag(0x0062, 3, 0x313))

    ChrTalk(
        0x0101,
        (
            '#000F<874D>赶往湖畔旅馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_68A')

    def _loc_62F(): pass

    label('loc_62F')

    ClearScenaFlags(ScenaFlag(0x0060, 1, 0x301))
    ClearScenaFlags(ScenaFlag(0x0061, 2, 0x30A))
    ClearScenaFlags(ScenaFlag(0x0061, 3, 0x30B))
    ClearScenaFlags(ScenaFlag(0x0061, 4, 0x30C))
    ClearScenaFlags(ScenaFlag(0x0062, 0, 0x310))
    ClearScenaFlags(ScenaFlag(0x0062, 2, 0x312))
    ClearScenaFlags(ScenaFlag(0x0062, 4, 0x314))
    ClearScenaFlags(ScenaFlag(0x0062, 7, 0x317))
    ClearScenaFlags(ScenaFlag(0x0063, 0, 0x318))
    ClearScenaFlags(ScenaFlag(0x0063, 3, 0x31B))
    ClearScenaFlags(ScenaFlag(0x0063, 4, 0x31C))
    ClearScenaFlags(ScenaFlag(0x0063, 5, 0x31D))
    ClearScenaFlags(ScenaFlag(0x0063, 6, 0x31E))
    ClearScenaFlags(ScenaFlag(0x0065, 3, 0x32B))
    ClearScenaFlags(ScenaFlag(0x0067, 2, 0x33A))
    ClearScenaFlags(ScenaFlag(0x0062, 3, 0x313))

    ChrTalk(
        0x0101,
        (
            '#000F照射。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_68A')

    def _loc_673(): pass

    label('loc_673')

    ChrTalk(
        0x0101,
        (
            '#000F什么也不做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_68A(): pass

    label('loc_68A')

    OP_5F(0x0000)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x690
@scena.Code('func_06_690')
def func_06_690():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_6D5',
    )

    ChrTalk(
        0x00FE,
        (
            '哦，你们是上次的游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '找将军阁下有事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D2C')

    def _loc_6D5(): pass

    label('loc_6D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_714',
    )

    ChrTalk(
        0x00FE,
        (
            '找将军阁下有事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在他应该\n',
            '十分繁忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D2C')

    def _loc_714(): pass

    label('loc_714')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_74A',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '找将军阁下有事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D2C')

    def _loc_74A(): pass

    label('loc_74A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_7B1',
    )

    ChrTalk(
        0x00FE,
        (
            '记得你们是上次的游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '抱歉啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '将军是那样说的，\n',
            '连一只猫都不能放进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D2C')

    def _loc_7B1(): pass

    label('loc_7B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_7F8',
    )

    ChrTalk(
        0x00FE,
        (
            '抱歉啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '将军是那样说的，\n',
            '连一只猫都不能放进去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D2C')

    def _loc_7F8(): pass

    label('loc_7F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 0, 0x310)),
            Expr.Return,
        ),
        'loc_867',
    )

    ChrTalk(
        0x00FE,
        (
            '#2420020828V将军的办公室在走廊尽头的左边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2420020829V请记住不要\n',
            '随便进入其它无关的场所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D2C')

    def _loc_867(): pass

    label('loc_867')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 6, 0x30E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CD9',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0061, 6, 0x30E))
    OP_69(0x0008, 1000)

    ChrTalk(
        0x0008,
        (
            '#2420020727V你们几个……\n',
            '到底从哪里进来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2420020728V钢壁之路的监察站\n',
            '应该还没有解除的呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020729V#010F我们是柏斯市的\n',
            '梅贝尔市长派来的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020730V能不能请您\n',
            '向摩尔根将军通报一下？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '在没有表明游击士身份的情况下，\n',
            '众人对市长的委托进行了说明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#2420020731V是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2420020732V你们的来意我已经明白了，\n',
            '不过非常不凑巧，将军现在不在这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2420020733V他去现场指挥搜索行动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020734V#020F来的不是时候呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020735V那将军大概什么时候会回来？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2420020736V唔……应该在今天之内吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2420020737V那边的休息所里有酒馆，\n',
            '或者你们先到那里等一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2420020738V将军一回来我就去通知你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 7, 0x30F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B7B',
    )

    ChrTalk(
        0x0101,
        (
            '#0010020739V#004F休息所……还有酒馆……\n',
            '为什么会有这种设施呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BC3')

    def _loc_B7B(): pass

    label('loc_B7B')

    ChrTalk(
        0x0101,
        (
            '#0010020740V#000F酒馆就是刚才的那个地方吧。\n',
            '为什么会有那种设施呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BC3(): pass

    label('loc_BC3')

    ChrTalk(
        0x0008,
        (
            '#2420020741V不管怎么说这里是和帝国接壤的国境呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2420020742V出入国境的审查很严格，\n',
            '所以有很多旅行者被耽误了行程。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020743V#010F原来如此。这样一来，\n',
            '像旅馆这样的设施就必不可少了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020744V#020F那么，就照你的意思，\n',
            '我们去酒馆里等候消息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0035, 0x01, 0x0100)
    EventEnd(0x01)

    Jump('loc_D2C')

    def _loc_CD9(): pass

    label('loc_CD9')

    ChrTalk(
        0x0008,
        (
            '那边的休息所里有酒馆，\n',
            '你们先到那里等一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '将军一回来我就去通知你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D2C(): pass

    label('loc_D2C')

    TalkEnd(0x0008)

    Return()

# id: 0x0007 offset: 0xD30
@scena.Code('func_07_D30')
def func_07_D30():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_D93',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎来到哈肯大门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '空贼们被逮捕了，\n',
            '终于可以从第一级警戒体制中\n',
            '解放出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FE2')

    def _loc_D93(): pass

    label('loc_D93')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_DF7',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然找到了定期船，\n',
            '不过犯人还是没有下落啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在国境守备队\n',
            '仍然在全力搜索之中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FE2')

    def _loc_DF7(): pass

    label('loc_DF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_EC6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_EAB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '欢迎来到哈肯大门！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呀？你们……\n',
            '你们是之前被关进监狱的游击士吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#509F这种事情偏偏记得这么清楚～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，反正嫌疑已经洗清了，\n',
            '这不是很好嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EC3')

    def _loc_EAB(): pass

    label('loc_EAB')

    ChrTalk(
        0x00FE,
        (
            '欢迎来到哈肯大门！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EC3(): pass

    label('loc_EC3')

    Jump('loc_FE2')

    def _loc_EC6(): pass

    label('loc_EC6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_F01',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎来到哈肯大门！\n',
            '打算去埃雷波尼亚帝国吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FE2')

    def _loc_F01(): pass

    label('loc_F01')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_F53',
    )

    ChrTalk(
        0x00FE,
        (
            '将军的怒吼声\n',
            '站在这里都能听得到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你、你们\n',
            '到底做了些什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FE2')

    def _loc_F53(): pass

    label('loc_F53')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 0, 0x310)),
            Expr.Return,
        ),
        'loc_F9E',
    )

    ChrTalk(
        0x00FE,
        (
            '现在这个关所处于戒严状态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请你们注意，\n',
            '不要随便走动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FE2')

    def _loc_F9E(): pass

    label('loc_F9E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 4, 0x30C)),
            Expr.Return,
        ),
        'loc_FE2',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎来到哈肯大门！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……啊，什么？\n',
            '你们穿过街道了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FE2(): pass

    label('loc_FE2')

    TalkEnd(0x0009)

    Return()

# id: 0x0008 offset: 0xFE6
@scena.Code('func_08_FE6')
def func_08_FE6():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_10E7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1090',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '我的出国手续\n',
            '终于办理好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是滞留在这里时\n',
            '吃饭住宿也把旅费都用完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，反正我的人生\n',
            '也是走到哪里算哪里，\n',
            '怎样都无所谓啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10E4')

    def _loc_1090(): pass

    label('loc_1090')

    ChrTalk(
        0x00FE,
        (
            '我的出国手续\n',
            '终于办理好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是滞留在这里时\n',
            '吃饭住宿也把旅费都用完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10E4(): pass

    label('loc_10E4')

    Jump('loc_1401')

    def _loc_10E7(): pass

    label('loc_10E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0063, 0, 0x318)),
            Expr.Return,
        ),
        'loc_11EF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_11AF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '一个人是不是幸福，\n',
            '要看最后他对人生\n',
            '是否满足。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果本人感到满足的话，\n',
            '不管谁再说什么，\n',
            '他的人生都是幸福的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我的人生格言就是\n',
            '走到哪里算哪里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '谁说我也没有用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11EC')

    def _loc_11AF(): pass

    label('loc_11AF')

    ChrTalk(
        0x00FE,
        (
            '我的人生格言就是\n',
            '走到哪里算哪里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '谁说我也没有用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11EC(): pass

    label('loc_11EC')

    Jump('loc_1401')

    def _loc_11EF(): pass

    label('loc_11EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_126B',
    )

    ChrTalk(
        0x00FE,
        (
            '反正即使认真地对待生活，\n',
            '该遭遇不幸的时候仍然会遭遇不幸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然如此，\n',
            '还是以随遇而安的态度活着比较轻松。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1401')

    def _loc_126B(): pass

    label('loc_126B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 0, 0x310)),
            Expr.Return,
        ),
        'loc_12DC',
    )

    ChrTalk(
        0x00FE,
        (
            '百日战役结束之后，\n',
            '到帝国旅行的人\n',
            '一直都很少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那场战争对利贝尔的人民\n',
            '果然留下了很深的创伤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1401')

    def _loc_12DC(): pass

    label('loc_12DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 4, 0x30C)),
            Expr.Return,
        ),
        'loc_1401',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_13A0',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '我本来想要\n',
            '去帝国那边旅行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过现在好像\n',
            '不能办理出境手续了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，反正我的人生\n',
            '也是走到哪里算哪里，\n',
            '怎样都无所谓啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想要去帝国旅行\n',
            '也是一时兴起罢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1401')

    def _loc_13A0(): pass

    label('loc_13A0')

    ChrTalk(
        0x00FE,
        (
            '现在好像不能\n',
            '办理出境手续了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，反正我的人生\n',
            '也是走到哪里算哪里，\n',
            '怎样都无所谓啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1401(): pass

    label('loc_1401')

    TalkEnd(0x000A)

    Return()

# id: 0x0009 offset: 0x1405
@scena.Code('func_09_1405')
def func_09_1405():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_147E',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵，没想到第一次的任务　\n',
            '竟然是突入空贼的基地……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '漫无计划的人生\n',
            '就是由各种各样的经历组成的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1570')

    def _loc_147E(): pass

    label('loc_147E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_1570',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1524',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '我本来想要\n',
            '去帝国那边旅行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由于没有旅费，\n',
            '我加入了国境守备队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '算了，\n',
            '我的人生本来就是漫无计划的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我一点都没有后悔过哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1570')

    def _loc_1524(): pass

    label('loc_1524')

    ChrTalk(
        0x00FE,
        (
            '我本来想要\n',
            '去帝国那边旅行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '由于没有旅费，\n',
            '我加入了国境守备队。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1570(): pass

    label('loc_1570')

    TalkEnd(0x000B)

    Return()

# id: 0x000A offset: 0x1574
@scena.Code('func_0A_1574')
def func_0A_1574():
    TalkBegin(0x000E)
    ChrTurnDirection(0x00FE, 0x0103, 0)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006C, 0, 0x360)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_182D',
    )

    SetScenaFlags(ScenaFlag(0x006C, 0, 0x360))
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '#0120021267V#814F啊，难道……\n',
            '这不是雪拉扎德前辈吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120021268V#850F很久不见了啊。\n',
            '自从您去修行之后就再没见面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021269V#020F这不是亚妮拉丝吗。\n',
            '你在这里做什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120021270V#810F嗯～\n',
            '协会委托我来这边消灭通缉魔兽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120021271V街道的封锁被解除了，\n',
            '我也终于能把委托给完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021272V#020F是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021273V对了，\n',
            '你已经找到所谓的剑之道了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120021274V#819F呵呵，请别问了。\n',
            '我还处在修行阶段呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120021275V#810F说起来，\n',
            '前辈您也是在执行协会的任务吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021276V#020F是啊，不过我和你的任务性质不同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120021277V#810F是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120021278V这个地方最近\n',
            '发生了很多事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120021279V您路上一定要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A09')

    def _loc_182D(): pass

    label('loc_182D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1994',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '#0120021280V#810F啊，雪拉扎德前辈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120021281V前辈，您在调查那个失踪的定期船事件，\n',
            '是真的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120021282V#856F不好意思，\n',
            '这次我没能帮上什么忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030021283V#020F你就别说这么见外的话啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030021284V而且这次的事件\n',
            '不多不少也和我们有关系的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0120021285V#814F原来是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120021286V#810F不管怎么说，\n',
            '你们一定要小心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A09')

    def _loc_1994(): pass

    label('loc_1994')

    ChrTalk(
        0x00FE,
        (
            '#0120021287V#856F最近，\n',
            '柏斯支部的游击士都在忙于工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120021288V由于发生了定期船的事件，\n',
            '人手变得不够用了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A09(): pass

    label('loc_1A09')

    TalkEnd(0x000E)

    Return()

# id: 0x000B offset: 0x1A0D
@scena.Code('func_0B_1A0D')
def func_0B_1A0D():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1AD7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A97',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '出动如此大规模的国境守备队\n',
            '还是百日战役以来的第一次啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '帝国那边不要误会\n',
            '我们有什么大的军事行动就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AD4')

    def _loc_1A97(): pass

    label('loc_1A97')

    ChrTalk(
        0x00FE,
        (
            '出动如此大规模的国境守备队\n',
            '还是百日战役以来的第一次啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AD4(): pass

    label('loc_1AD4')

    Jump('loc_1C67')

    def _loc_1AD7(): pass

    label('loc_1AD7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_1B42',
    )

    ChrTalk(
        0x00FE,
        (
            '听说摩尔根将军\n',
            '改变了搜索的方针。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是因为\n',
            '王国军新设立的情报部\n',
            '给搜索来了很多情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C67')

    def _loc_1B42(): pass

    label('loc_1B42')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_1BD5',
    )

    ChrTalk(
        0x00FE,
        (
            '针对空贼团的搜索\n',
            '好像陷入了困境。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '警备飞艇对北部山岳一带\n',
            '进行了全方位的搜索……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过暂时好像还没有\n',
            '找到什么重要的线索啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C67')

    def _loc_1BD5(): pass

    label('loc_1BD5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 0, 0x310)),
            Expr.Return,
        ),
        'loc_1C67',
    )

    ChrTalk(
        0x00FE,
        (
            '国境守备队经常要\n',
            '随时面对来自帝国的威胁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论什么时候，\n',
            '我们都一定要非常谨慎才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为不知道\n',
            '帝国又会找什么借口实行侵略。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C67(): pass

    label('loc_1C67')

    TalkEnd(0x000F)

    Return()

# id: 0x000C offset: 0x1C6B
@scena.Code('func_0C_1C6B')
def func_0C_1C6B():
    TalkBegin(0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_1CBA',
    )

    ChrTalk(
        0x00FE,
        (
            '今天的天气很好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从这里可以很清楚望到帝国那边的领土。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FF2')

    def _loc_1CBA(): pass

    label('loc_1CBA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_1DD1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D6A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '幸好帝国现在\n',
            '还没有什么军事行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '两国缔结了不侵犯条约，\n',
            '他们没有动静也是理所当然的啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过相互之间的紧张关系\n',
            '是不会这么容易被化解的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1DCE')

    def _loc_1D6A(): pass

    label('loc_1D6A')

    ChrTalk(
        0x00FE,
        (
            '幸好帝国现在\n',
            '还没有什么军事行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '两国缔结了不侵犯条约，\n',
            '他们没有动静也是理所当然的啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1DCE(): pass

    label('loc_1DCE')

    Jump('loc_1FF2')

    def _loc_1DD1(): pass

    label('loc_1DD1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_1F34',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1EBF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '以前，国境线前面不远处\n',
            '有一个被称为哈梅尔的帝国小村落。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过现在已经不能再看到那个村子啦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据说在百日战役的时候，\n',
            '那个村子消失在战火之中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果不是利贝尔军反击战造成的，\n',
            '那么消失的原因是什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F31')

    def _loc_1EBF(): pass

    label('loc_1EBF')

    ChrTalk(
        0x00FE,
        (
            '以前，国境线前面不远处\n',
            '有一个被称为哈梅尔的帝国小村落。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据说在百日战役的时候，\n',
            '那个村子消失在战火之中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F31(): pass

    label('loc_1F31')

    Jump('loc_1FF2')

    def _loc_1F34(): pass

    label('loc_1F34')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 0, 0x310)),
            Expr.Return,
        ),
        'loc_1FF2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FBE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '虽然这已经是十年之前的事情了。\n',
            '但在这里站岗我还是觉得紧张。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望帝国军队\n',
            '不要再次发动袭击\n',
            '将这道门攻破……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1FF2')

    def _loc_1FBE(): pass

    label('loc_1FBE')

    ChrTalk(
        0x00FE,
        (
            '希望帝国军队\n',
            '不要再次发动袭击\n',
            '将这道门攻破……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1FF2(): pass

    label('loc_1FF2')

    TalkEnd(0x0010)

    Return()

# id: 0x000D offset: 0x1FF6
@scena.Code('func_0D_1FF6')
def func_0D_1FF6():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    ChrSetPos(0x0101, 7940, 30, -38220, 0)
    ChrSetPos(0x0102, 6200, 0, -38720, 0)
    ChrSetPos(0x0103, 7430, 0, -40110, 0)
    CameraMove(14550, 11750, 700, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(5560, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_12(0x00009470, 0x0003D090, 0x00000000)
    FadeIn(2000, 0)
    CameraMove(-8310, 11750, 800, 5000)
    Fade(1000)
    CameraMove(-440, 11200, -19210, 0)
    OP_67(0, 4860, -10000, 0)
    CameraSetDistance(6560, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_20DC')
    def lambda_20DC():
        CameraSetDistance(3250, 9000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_20DC)

    @scena.Lambda('lambda_20EC')
    def lambda_20EC():
        OP_67(0, 8000, -10000, 9000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_20EC)

    Sleep(3000)

    @scena.Lambda('lambda_2109')
    def lambda_2109():
        OP_6C(45000, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_2109)

    @scena.Lambda('lambda_2119')
    def lambda_2119():
        CameraMove(7190, 50, -38190, 6000)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_2119)

    OP_12(0x00009470, 0x000186A0, 0x00001B58)
    Sleep(6000)

    ChrTalk(
        0x0101,
        (
            '#0010020708V#004F这、这就是哈肯大门……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020709V真是大得夸张啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020710V#020F作为连通帝国方面的唯一关口，\n',
            '这里是抵御威胁保卫王国的屏障……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020711V由于在１０年前的战争中被破坏过，\n',
            '所以又重新加固了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020712V#000F也就是说，这里的另一侧\n',
            '就已经不再是利贝尔王国了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020713V#012F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020714V那边就是埃雷波尼亚帝国的领土，\n',
            '一个以『黄金军马』为国徽的军事国家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020715V#002F埃雷波尼亚帝国……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020716V#015F…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020020717V#010F那么，\n',
            '我们赶快去和摩尔根将军会面吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020718V大门的旁边有营房……\n',
            '我们就去那边看看吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010020719V#006F嗯，ＯＫ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020720V#020F在那之前……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020721V你们两个先把\n',
            '胸前的游击士徽章摘下来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020722V要是被摩尔根将军看到就麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0103, 400)
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010020723V#000F啊，我都忘了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(143, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔和约修亚把游击士徽章摘了下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010020724V#008F不、不知怎么搞的，\n',
            '感觉很不习惯呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020725V#010F嗯，的确感觉有些不适应。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020726V#021F呵呵，这就证明\n',
            '你们已经习惯游击士这个身份了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x000E offset: 0x2587
@scena.Code('func_0E_2587')
def func_0E_2587():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-15040, 500, -25820, 0)
    SetScenaFlags(ScenaFlag(0x0062, 0, 0x310))
    ChrSetPos(0x0101, -14860, 500, -23500, 180)
    ChrSetPos(0x0103, -14860, 500, -23500, 180)
    ChrSetPos(0x0102, -14860, 500, -23500, 180)
    ChrSetPos(0x000C, -14860, 500, -23500, 180)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0040)
    Sleep(500)

    OP_70(0x0000, 20)
    OP_73(0x0000)
    ChrSetPos(0x0011, -15050, 500, -29150, 0)
    CreateThread(0x0103, 0x00, 0x00, func_0F_2997)
    CreateThread(0x0102, 0x00, 0x00, func_10_29C7)
    CreateThread(0x0101, 0x00, 0x00, func_11_29FC)
    CreateThread(0x000C, 0x00, 0x00, func_12_2A31)
    Sleep(2000)

    CameraMove(-10900, 0, -27570, 1500)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010020812V#509F#2P……喂，\n',
            '为什么你这么自然而然就跟过来了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020813V#025F而且刚才又在\n',
            '绝妙的时机来向我们搭话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '金发青年',
        (
            '#0040020814V#035F呵呵，被发现了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020815V好像有什么有趣的事情，\n',
            '所以我也想顺便参观一下嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020816V#030F好了，你们不用介意我，\n',
            '去和那个将军谈话就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1200)

    ChrTalk(
        0x0101,
        (
            '#0010020817V#005F#3S#2P肯定是要介意的呀！#2S',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    ChrMoveTo(0x0101, -11190, 0, -28000, 3000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010020818V#009F#2P喂，你赶快回去吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '金发青年',
        (
            '#0040020819V#034F小气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000C, 270, 400)
    ChrWalkTo(0x000C, -15000, 0, -27740, 2000, 0x00)
    ChrWalkTo(0x000C, -14860, 500, -23760, 3000, 0x00)
    OP_72(0x0000, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_6F(0x0000, 20)
    OP_70(0x0000, 0)
    OP_73(0x0000)
    OP_71(0x0000, 0x0800)
    ChrSetFlags(0x000C, 0x0080)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020020820V#017F捉摸不透的人……\n',
            '他到底来王国做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020821V#020F确实不是什么简单的人物。\n',
            '该怎么说呢，从各种意义上都是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010020822V#509F为了社会和人类，\n',
            '这样的怪人我们还是置之不理的好！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020823V赶快去将军那里吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x000F offset: 0x2997
@scena.Code('func_0F_2997')
def func_0F_2997():
    ChrWalkTo(0x00FE, -15000, 0, -27740, 3000, 0x00)
    ChrWalkTo(0x00FE, -8900, 0, -28180, 3000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0010 offset: 0x29C7
@scena.Code('func_10_29C7')
def func_10_29C7():
    Sleep(1000)

    ChrWalkTo(0x00FE, -15000, 0, -27740, 3000, 0x00)
    ChrWalkTo(0x00FE, -10120, 0, -28800, 3000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0011 offset: 0x29FC
@scena.Code('func_11_29FC')
def func_11_29FC():
    Sleep(1800)

    ChrWalkTo(0x00FE, -15000, 0, -27740, 3000, 0x00)
    ChrWalkTo(0x00FE, -10300, 0, -27580, 3000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0012 offset: 0x2A31
@scena.Code('func_12_2A31')
def func_12_2A31():
    Sleep(3000)

    ChrWalkTo(0x00FE, -15000, 0, -27740, 3000, 0x00)
    ChrWalkTo(0x00FE, -12770, 0, -28330, 3000, 0x00)

    Return()

# id: 0x0013 offset: 0x2A5F
@scena.Code('func_13_2A5F')
def func_13_2A5F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 1, 0x311)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 0, 0x310)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2C1D',
    )

    MapClearFlags(0x00000001)
    EventBegin(0x00)
    OP_4A(0x0008, 255)

    @scena.Lambda('lambda_2A7C')
    def lambda_2A7C():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2A7C)

    @scena.Lambda('lambda_2A8A')
    def lambda_2A8A():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_2A8A)

    @scena.Lambda('lambda_2A98')
    def lambda_2A98():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2A98)

    @scena.Lambda('lambda_2AA6')
    def lambda_2AA6():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2AA6)

    OP_69(0x0008, 1000)
    SetScenaFlags(ScenaFlag(0x0062, 1, 0x311))

    ChrTalk(
        0x0008,
        (
            '#2420020824V刚才听见你们的吵架声了，\n',
            '和其它的旅行者发生了争执吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020825V#008F其、其实也不是什么大事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020826V话说回来……\n',
            '我们可以和将军见面了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2420020827V啊，请进去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0008, 0x0004)
    ChrWalkTo(0x0008, 8300, 0, -10500, 3000, 0x00)
    ChrTurnDirection(0x0008, 0x0000, 400)
    ChrClearFlags(0x0008, 0x0004)

    ChrTalk(
        0x0008,
        (
            '#2420020828V将军的办公室在走廊尽头的左边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2420020829V请记住不要\n',
            '随便进入其它无关的场所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 180, 400)
    OP_4B(0x0008, 255)
    OP_71(0x0001, 0x0010)
    EventEnd(0x01)

    def _loc_2C1D(): pass

    label('loc_2C1D')

    Return()

# id: 0x0014 offset: 0x2C1E
@scena.Code('func_14_2C1E')
def func_14_2C1E():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(6980, 0, -10700, 0)
    ChrSetPos(0x0101, 11000, 500, -11970, 0)
    ChrSetPos(0x0103, 11000, 500, -11970, 0)
    ChrSetPos(0x0102, 11000, 500, -11970, 0)
    ChrSetPos(0x000D, 11000, 500, -11970, 0)
    ChrSetPos(0x0008, 11000, 500, -11970, 0)
    ChrSetPos(0x0009, 11000, 500, -11970, 0)
    OP_4A(0x000D, 255)
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0103, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetFlags(0x000D, 0x0040)
    ChrSetChipByIndex(0x0008, 5)
    ChrSetChipByIndex(0x0009, 5)
    Sleep(500)

    OP_70(0x0001, 20)
    OP_73(0x0001)
    Sleep(500)

    CreateThread(0x0101, 0x00, 0x00, func_15_4083)
    CreateThread(0x0103, 0x00, 0x00, func_17_412D)
    CreateThread(0x0102, 0x00, 0x00, func_16_40D8)
    Sleep(1500)

    ChrClearFlags(0x0009, 0x0080)
    CreateThread(0x0009, 0x01, 0x00, func_1B_41E0)
    Sleep(300)

    ChrClearFlags(0x0008, 0x0080)
    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_2D39')
    def lambda_2D39():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_2D39)

    ChrWalkTo(0x0008, 8010, 0, -12180, 4000, 0x00)
    ChrWalkTo(0x0008, 7090, 0, -11100, 4000, 0x00)
    ChrSetDirection(0x0008, 270, 0)

    ChrTalk(
        0x0101,
        (
            '#0010020905V#009F等、等等，干什么呀！\n',
            '像撵狗似的对待我们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000D, 0x0080)
    ChrSetRGBAMask(0x000D, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_2DCA')
    def lambda_2DCA():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000D, 0x0003, lambda_2DCA)

    ChrWalkTo(0x000D, 8010, 0, -12180, 3000, 0x00)

    ChrTalk(
        0x000D,
        (
            '#0600020906V#160F#2P哼，因为你们就只配如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020907V故意隐瞒身份姑且不提，\n',
            '竟然还明目张胆骗取军情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020908V敢做出这种不知廉耻的事，\n',
            '看来游击士的信用也不过如此！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020909V#005F说、说什么骗取！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010020910V要说起来，这都是你的错！\n',
            '谁让你不把消息通告给游击士协会！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600020911V#162F#2P胡闹！这种事件怎么能让\n',
            '充其量只算民间团体的组织负责！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020912V#163F真是的……\n',
            '那个梅贝尔究竟怎么想的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020913V雇佣这种小女孩儿，\n',
            '只会给搜索行动带来麻烦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030020914V#022F……请适可而止吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3019')
    def lambda_3019():
        CameraMove(7800, 0, -10140, 1200)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_3019)

    ChrSetChipByIndex(0x0008, 0)
    ChrSetChipByIndex(0x0009, 0)

    @scena.Lambda('lambda_303B')
    def lambda_303B():
        ChrTurnDirection(0x00FE, 0x0103, 400)
        Yield()

        Jump('lambda_303B')

    DispatchAsync2(0x0008, 0x0002, lambda_303B)

    @scena.Lambda('lambda_304C')
    def lambda_304C():
        ChrTurnDirection(0x00FE, 0x0103, 400)
        Yield()

        Jump('lambda_304C')

    DispatchAsync2(0x0009, 0x0002, lambda_304C)

    ChrWalkTo(0x0103, 6200, 0, -12260, 3000, 0x00)
    TerminateThread(0x0008, 0x02)
    TerminateThread(0x0009, 0x02)
    Sleep(400)

    ChrTalk(
        0x0103,
        (
            '#0030020915V#025F#6P将军有没有想过\n',
            '我们特地从洛连特\n',
            '赶过来这里的原因啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(
        0x0103,
        (
            '#0030020916V#024F#6P#3S不就是因为你们这些当兵的！\n',
            '在关键时刻完全不中用！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600020917V#161F#2P什、什什什什什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010020918V#007F（哇啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020919V#017F（雪拉姐姐，发飙了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020920V#022F#6P最近这几个月，\n',
            '柏斯地区接连发生由空贼引起的盗窃案件。\n',
            '敢问将军知道吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020921V没有经过认真的搜查，\n',
            '就把责任一股脑推给游击士协会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020922V#026F发生了这样的大事，还摆出一幅\n',
            '目中无人的态度和我们划清界限……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020923V而且，先别说人质了，\n',
            '连定期船的行踪到现在都还没有查明。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020924V#027F难道你们不会感到羞耻吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000D,
        (
            '#0600020925V#162F#2P#3S给我闭嘴，小丫头！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600020926V#162F#2P有组织纪律约束的军队\n',
            '岂能像你们那样任意妄为？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020927V不考虑清楚就行动的结果，\n',
            '只会是打草惊蛇让犯人逃掉。\n',
            '你们不懂就不要逞一时意气地胡说！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030020928V#022F#6P说得可真是好听……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0040)
    ChrSetChipByIndex(0x000C, 6)
    ChrSetRGBAMask(0x000C, 255, 255, 255, 0, 0)
    ChrSetPos(0x000C, 0, 0, -5000, 135)
    OP_1F(0x46, 0x00000190)
    Sleep(400)

    PlaySE(190, 0x00, 0x64)
    Sleep(1000)

    NpcTalk(
        0x000C,
        '青年的声音',
        (
            '#0040020929V呼，多么令人悲哀呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1200)

    OP_1F(0x64, 0x00000190)
    OP_4A(0x000C, 255)
    ChrSetChipByIndex(0x000C, 6)
    ChrSetRGBAMask(0x000C, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000C, 255, 255, 255, 255, 100)
    ChrSetPos(0x000C, 0, 0, -7024, 135)

    @scena.Lambda('lambda_357C')
    def lambda_357C():
        CameraMove(3580, 0, -8410, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_357C)

    @scena.Lambda('lambda_3594')
    def lambda_3594():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_3594)

    @scena.Lambda('lambda_35A4')
    def lambda_35A4():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_35A4)

    @scena.Lambda('lambda_35B2')
    def lambda_35B2():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_35B2)

    @scena.Lambda('lambda_35C0')
    def lambda_35C0():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_35C0)

    Sleep(500)

    @scena.Lambda('lambda_35D3')
    def lambda_35D3():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_35D3)

    @scena.Lambda('lambda_35E1')
    def lambda_35E1():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_35E1)

    @scena.Lambda('lambda_35EF')
    def lambda_35EF():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_35EF)

    Sleep(2000)

    ChrTalk(
        0x000C,
        (
            '#0040020930V#035F争吵是不会有结果的……\n',
            '只会使这片干涸的大地更为荒凉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020931V#030F本人谨向在场诸位，献歌一首。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020932V一首能润泽心中的荒野，\n',
            '让美丽的希望之花盛开，\n',
            '温柔而忧伤的歌曲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0103, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x000D, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0009, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0101)
    OP_63(0x0103)
    OP_63(0x0102)
    OP_63(0x000D)
    OP_63(0x0008)
    OP_63(0x0009)
    Sleep(500)

    PlayBGM(0)

    ChrTalk(
        0x000C,
        (
            '#006501v#035F#10A#0W……………………',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(1500)

    OP_4B(0x000C, 255)
    CloseMessageWindow()
    Sleep(6270)

    ChrTalk(
        0x000C,
        (
            '#100A#0W滑过天边　星之轨迹……  ',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(6600)

    ChrTalk(
        0x000C,
        (
            '#100A#0W仿如路标　引导向你……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(6200)

    ChrTalk(
        0x000C,
        (
            '#100A#0W急切的　思念　满溢胸怀……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(5600)

    ChrTalk(
        0x000C,
        (
            '#100A#0W月亮也嘲笑　这份痛苦……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(7000)

    ChrTalk(
        0x000C,
        (
            '#100A#0W若无法实现　这份空想……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(7000)

    ChrTalk(
        0x000C,
        (
            '#100A#0W至少请留下　一道浅伤……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(9500)

    ChrTalk(
        0x000C,
        (
            '#100A#0W最初之吻　最后之吻…… ',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(8500)

    ChrTalk(
        0x000C,
        (
            '#100A#0W你的泪滴  化作琥珀……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(8800)

    ChrTalk(
        0x000C,
        (
            '#100A#0W这份爱意　永远封存……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(10800)

    CloseMessageWindow()
    OP_21()
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(2000)

    OP_4A(0x000C, 255)
    Sleep(1000)

    Fade(250)
    ChrSetFlags(0x000C, 0x0002)
    ChrSetChipByIndex(0x000C, 7)
    ChrSetSubChip(0x000C, 0)
    OP_0D()
    OP_99(0x000C, 0x00, 0x03, 1500)
    Sleep(300)

    OP_99(0x000C, 0x03, 0x0A, 1000)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0040020942V#035F呵呵……\n',
            '看来大家已经明白了我的意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020943V世上最宝贵最重要的东西……\n',
            '是爱与和平。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020944V#030F以时下的话来说，就是Love ＆ Peace。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(137, 0x00, 0x64)
    OP_62(0x000C, 0x0000012C, 1900, 0x36, 0x39, 0x000000FA, 0x00)
    Sleep(1000)

    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0600020945V#163F#2P咳、咳咳……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3AD1')
    def lambda_3AD1():
        CameraMove(6980, 0, -10700, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_3AD1)

    @scena.Lambda('lambda_3AE9')
    def lambda_3AE9():
        OP_6C(45000, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_3AE9)

    Sleep(1500)

    PlayBGM(16)
    ChrClearFlags(0x000C, 0x0002)
    ChrSetChipByIndex(0x000C, 2)
    ChrTurnDirection(0x000D, 0x0009, 400)
    OP_63(0x000C)

    ChrTalk(
        0x000D,
        (
            '#0600020946V#160F#2P各地搜索部队的报告\n',
            '差不多也都传来了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3B55')
    def lambda_3B55():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3B55)

    @scena.Lambda('lambda_3B63')
    def lambda_3B63():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3B63)

    @scena.Lambda('lambda_3B71')
    def lambda_3B71():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3B71)

    @scena.Lambda('lambda_3B7F')
    def lambda_3B7F():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_3B7F)

    @scena.Lambda('lambda_3B8D')
    def lambda_3B8D():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3B8D)

    ChrTalk(
        0x0009,
        (
            '#2440020947V是、是的。\n',
            '正等候将军的批阅！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0600020948V#160F#2P那我回去工作了。\n',
            '记住，不要让那些人再进来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000D, 90, 400)
    ChrWalkTo(0x000D, 9540, 500, -11960, 2000, 0x00)
    Sleep(500)

    ChrTalk(
        0x000D,
        (
            '#0600020949V#163F#6P还有就是……\n',
            '解除钢壁之路的监察站。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600020950V我不想再看到他们呆在这里，\n',
            '简直是太碍眼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2420020951V#5P遵、遵命！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0009, 0x01, 0x00, func_1C_422D)
    CreateThread(0x0008, 0x01, 0x00, func_1D_42A8)

    @scena.Lambda('lambda_3CD2')
    def lambda_3CD2():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x000D, 0x0003, lambda_3CD2)

    ChrWalkTo(0x000D, 11000, 500, -11970, 2000, 0x00)
    ChrSetFlags(0x000D, 0x0080)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010020952V#509F（啊！逃掉了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020020953V#017F（不过心情可以理解呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3D5C')
    def lambda_3D5C():
        CameraMove(4140, 0, -10880, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_3D5C)

    @scena.Lambda('lambda_3D74')
    def lambda_3D74():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_3D74)

    ChrWalkTo(0x000C, 2400, 0, -9920, 2000, 0x00)
    ChrSetDirection(0x000C, 135, 400)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0040020954V#031F呵呵，无论哪个国家，\n',
            '军人都是一样不解风情呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020955V哈·哈·哈。\n',
            '还是在场的你们几位更有眼光啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1200)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010020956V#506F#5P那、那么，\n',
            '我们也该回去了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 45, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020020957V#019F#6P是、是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020020958V虽然惹了些麻烦，\n',
            '不过大致上还是得到了情报……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0102, 400)

    ChrTalk(
        0x0103,
        (
            '#0030020959V#021F我们回到柏斯\n',
            '再制定今后的对策吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0101, 0x00, 0x00, func_18_417D)
    CreateThread(0x0103, 0x00, 0x00, func_1A_41BF)
    CreateThread(0x0102, 0x00, 0x00, func_19_41A3)
    Sleep(1000)

    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrSetDirection(0x000C, 180, 400)

    ChrTalk(
        0x000C,
        (
            '#0040020960V#033F哎呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040020961V等等，你们几位。\n',
            '你们刚才说要去哪里来着？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrMoveToRelative(0x000C, 0, 0, -3000, 4000, 0x00)

    ChrTalk(
        0x000C,
        (
            '#0040020962V#036F#5P等、等一下！\n',
            '不不，无论如何请稍等我一下啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4051')
    def lambda_4051():
        ChrMoveToRelative(0x00FE, 0, 0, -7000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_4051)

    FadeOut(2000, 0, -1)
    OP_0D()
    MapClearFlags(0x00400000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T1410._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0015 offset: 0x4083
@scena.Code('func_15_4083')
def func_15_4083():
    Sleep(600)

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_40B0')
    def lambda_40B0():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_40B0)

    ChrWalkTo(0x00FE, 5220, 0, -11500, 6000, 0x00)
    ChrTurnDirection(0x00FE, 0x000D, 400)

    Return()

# id: 0x0016 offset: 0x40D8
@scena.Code('func_16_40D8')
def func_16_40D8():
    Sleep(300)

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_4105')
    def lambda_4105():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_4105)

    ChrWalkTo(0x00FE, 4700, 0, -12900, 6000, 0x00)
    ChrTurnDirection(0x00FE, 0x000D, 400)

    Return()

# id: 0x0017 offset: 0x412D
@scena.Code('func_17_412D')
def func_17_412D():
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_4155')
    def lambda_4155():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_4155)

    ChrWalkTo(0x00FE, 3810, 0, -12210, 6000, 0x00)
    ChrTurnDirection(0x00FE, 0x000D, 400)

    Return()

# id: 0x0018 offset: 0x417D
@scena.Code('func_18_417D')
def func_18_417D():
    Sleep(500)

    Sleep(500)

    ChrSetDirection(0x00FE, 180, 400)
    ChrMoveToRelative(0x00FE, 0, 0, -10000, 3000, 0x00)

    Return()

# id: 0x0019 offset: 0x41A3
@scena.Code('func_19_41A3')
def func_19_41A3():
    ChrSetDirection(0x00FE, 180, 400)
    ChrMoveToRelative(0x00FE, 0, 0, -10000, 3000, 0x00)

    Return()

# id: 0x001A offset: 0x41BF
@scena.Code('func_1A_41BF')
def func_1A_41BF():
    Sleep(500)

    ChrSetDirection(0x00FE, 180, 400)
    ChrMoveToRelative(0x00FE, 0, 0, -10000, 3000, 0x00)

    Return()

# id: 0x001B offset: 0x41E0
@scena.Code('func_1B_41E0')
def func_1B_41E0():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_41F1')
    def lambda_41F1():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_41F1)

    ChrWalkTo(0x00FE, 8010, 0, -12180, 4000, 0x00)
    ChrWalkTo(0x00FE, 7180, 0, -13360, 4000, 0x00)
    ChrSetDirection(0x00FE, 270, 0)

    Return()

# id: 0x001C offset: 0x422D
@scena.Code('func_1C_422D')
def func_1C_422D():
    Sleep(500)

    ChrWalkTo(0x00FE, 8010, 0, -12180, 4000, 0x00)
    ChrWalkTo(0x00FE, 9290, 500, -12050, 4000, 0x00)

    @scena.Lambda('lambda_4260')
    def lambda_4260():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_4260)

    ChrWalkTo(0x00FE, 11000, 500, -11970, 2000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)
    Sleep(500)

    OP_72(0x0001, 0x0800)
    PlaySE(230, 0x00, 0x64)
    OP_6F(0x0001, 20)
    OP_70(0x0001, 0)
    OP_71(0x0001, 0x0800)

    Return()

# id: 0x001D offset: 0x42A8
@scena.Code('func_1D_42A8')
def func_1D_42A8():
    Sleep(3000)

    ChrWalkTo(0x00FE, 8250, 0, -12000, 3000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x001E offset: 0x42C9
@scena.Code('func_1E_42C9')
def func_1E_42C9():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 6, 0x30E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_440C',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 0, 0x310)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4385',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_42F5',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_42FC')

    def _loc_42F5(): pass

    label('loc_42F5')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_42FC(): pass

    label('loc_42FC')

    @scena.Lambda('lambda_4302')
    def lambda_4302():
        ChrTurnDirection(0x0101, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4302)

    ChrTurnDirection(0x0102, 0x0103, 400)

    ChrTalk(
        0x0103,
        (
            '#0030020747V#020F在将军回来之前，\n',
            '我们还是不要随便乱走了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020748V就在酒馆里一边等一边休息一下吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_43F1')

    def _loc_4385(): pass

    label('loc_4385')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_439B',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_43A2')

    def _loc_439B(): pass

    label('loc_439B')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_43A2(): pass

    label('loc_43A2')

    @scena.Lambda('lambda_43A8')
    def lambda_43A8():
        ChrTurnDirection(0x0101, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_43A8)

    ChrTurnDirection(0x0102, 0x0103, 400)

    ChrTalk(
        0x0103,
        (
            '#0030020749V#020F别到处乱走了。\n',
            '赶快去和将军会面吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_43F1(): pass

    label('loc_43F1')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_440C(): pass

    label('loc_440C')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
