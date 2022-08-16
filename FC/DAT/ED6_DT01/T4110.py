import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4110_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4110   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4110.x'
    header.mapIndex       = 1
    header.bgm            = 14
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
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01490._CH', 'ED6_DT07/CH01490P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT07/CH01183._CH', 'ED6_DT07/CH01183P._CP'),
        ('ED6_DT07/CH01033._CH', 'ED6_DT07/CH01033P._CP'),
    ]

# id: 0x10001 offset: 0x102
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '芭蒂',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000E,
        ),
        ScenaNpcData(
            name                = '拉尔夫',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '比尔爷爷',
            x                   = 26550,
            z                   = 0,
            y                   = -2980,
            direction           = 77,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            name                = '伊鲁妮婆婆',
            x                   = 32860,
            z                   = 100,
            y                   = 1000,
            direction           = 175,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '菲利奥',
            x                   = 51890,
            z                   = 0,
            y                   = 56160,
            direction           = 84,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '拉科舒',
            x                   = 59860,
            z                   = 0,
            y                   = 58240,
            direction           = 9,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '丹克',
            x                   = 90200,
            z                   = 0,
            y                   = -2190,
            direction           = 169,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '西加罗',
            x                   = 7200,
            z                   = 200,
            y                   = 53270,
            direction           = 254,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0155,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '艾德尔',
            x                   = 10450,
            z                   = 0,
            y                   = 53510,
            direction           = 106,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
    )

# id: 0x10002 offset: 0x222
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x222
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x222
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x222
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_27D',
    )

    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000D, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -28640, 0, 1890, 183)
    ChrSetFlags(0x0008, 0x0010)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -32060, 0, -2000, 187)
    CreateThread(0x0009, 0x00, 0x00, func_03_548)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x0010, 0x0080)

    Jump('loc_4E4')

    def _loc_27D(): pass

    label('loc_27D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2C6',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -27680, 0, -3510, 10)
    CreateThread(0x0008, 0x00, 0x00, func_02_532)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -32060, 0, -2000, 187)
    CreateThread(0x0009, 0x00, 0x00, func_03_548)
    ChrSetFlags(0x0010, 0x0080)

    Jump('loc_4E4')

    def _loc_2C6(): pass

    label('loc_2C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_30A',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -27310, 0, -4370, 81)
    CreateThread(0x0008, 0x00, 0x00, func_02_532)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -32060, 0, -2000, 187)
    CreateThread(0x0009, 0x00, 0x00, func_03_548)

    Jump('loc_4E4')

    def _loc_30A(): pass

    label('loc_30A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_364',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -27680, 0, -3510, 10)
    CreateThread(0x0008, 0x00, 0x00, func_02_532)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -31960, 0, -1490, 135)
    CreateThread(0x0009, 0x00, 0x00, func_02_532)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetPos(0x0010, 1950, 0, 56650, 90)

    Jump('loc_4E4')

    def _loc_364(): pass

    label('loc_364')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_373',
    )

    ChrSetFlags(0x0010, 0x0080)

    Jump('loc_4E4')

    def _loc_373(): pass

    label('loc_373')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_3A2',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0008, 10)
    ChrSetPos(0x0008, -28640, 150, 1890, 180)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetFlags(0x0008, 0x0004)

    Jump('loc_4E4')

    def _loc_3A2(): pass

    label('loc_3A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_3D3',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -32060, 0, -2000, 187)
    CreateThread(0x0009, 0x00, 0x00, func_03_548)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)

    Jump('loc_4E4')

    def _loc_3D3(): pass

    label('loc_3D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_424',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0008, 10)
    ChrSetPos(0x0008, -28640, 150, 1890, 180)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetFlags(0x0008, 0x0004)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -30620, 0, -1960, 0)
    ChrSetFlags(0x0009, 0x0010)
    CreateThread(0x0009, 0x00, 0x00, func_02_532)

    Jump('loc_4E4')

    def _loc_424(): pass

    label('loc_424')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_450',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -32060, 0, -2000, 187)
    CreateThread(0x0009, 0x00, 0x00, func_03_548)
    ChrSetFlags(0x0010, 0x0080)

    Jump('loc_4E4')

    def _loc_450(): pass

    label('loc_450')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_4B4',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0008, 10)
    ChrSetPos(0x0008, -28640, 150, 1890, 180)
    ChrSetFlags(0x0008, 0x0010)
    ChrSetFlags(0x0008, 0x0004)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -32060, 0, -2000, 187)
    CreateThread(0x0009, 0x00, 0x00, func_03_548)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetChipByIndex(0x000B, 9)
    ChrSetFlags(0x000B, 0x0010)
    ChrSetFlags(0x000B, 0x0004)
    TerminateThread(0x000B, 0xFF)

    Jump('loc_4E4')

    def _loc_4B4(): pass

    label('loc_4B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_4E4',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, -32369, 0, 790, 0)
    ChrSetChipByIndex(0x000B, 9)
    ChrSetFlags(0x000B, 0x0010)
    ChrSetFlags(0x000B, 0x0004)
    TerminateThread(0x000B, 0xFF)

    def _loc_4E4(): pass

    label('loc_4E4')

    Return()

# id: 0x0001 offset: 0x4E5
@scena.Code('func_01_4E5')
def func_01_4E5():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 1, 0x631)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 3, 0x623)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 3, 0x61B)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 6, 0x616)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_518',
    )

    OP_B1('t4110_y')

    Jump('loc_521')

    def _loc_518(): pass

    label('loc_518')

    OP_B1('t4110_n')

    def _loc_521(): pass

    label('loc_521')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            Expr.Return,
        ),
        'loc_531',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_531(): pass

    label('loc_531')

    Return()

# id: 0x0002 offset: 0x532
@scena.Code('func_02_532')
def func_02_532():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_547',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_532')

    def _loc_547(): pass

    label('loc_547')

    Return()

# id: 0x0003 offset: 0x548
@scena.Code('func_03_548')
def func_03_548():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_56B',
    )

    OP_8D(0x00FE, -33020, -920, -30290, -3790, 4000)

    Jump('func_03_548')

    def _loc_56B(): pass

    label('loc_56B')

    Return()

# id: 0x0004 offset: 0x56C
@scena.Code('func_04_56C')
def func_04_56C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_58F',
    )

    OP_8D(0x00FE, 24820, -4110, 30930, -1350, 1800)

    Jump('func_04_56C')

    def _loc_58F(): pass

    label('loc_58F')

    Return()

# id: 0x0005 offset: 0x590
@scena.Code('func_05_590')
def func_05_590():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5B3',
    )

    OP_8D(0x00FE, 89790, -700, 91780, -4740, 2000)

    Jump('func_05_590')

    def _loc_5B3(): pass

    label('loc_5B3')

    Return()

# id: 0x0006 offset: 0x5B4
@scena.Code('func_06_5B4')
def func_06_5B4():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_60F',
    )

    ChrTalk(
        0x00FE,
        (
            '在大主教的鼓励下，\n',
            '我准备出一本书。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要把在各地巡礼的\n',
            '经验记录下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BA4')

    def _loc_60F(): pass

    label('loc_60F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_663',
    )

    ChrTalk(
        0x00FE,
        (
            '呼……\n',
            '终于把家里打扫完毕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，\n',
            '我差不多该去大圣堂看看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BA4')

    def _loc_663(): pass

    label('loc_663')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_6D2',
    )

    ChrTalk(
        0x00FE,
        (
            '妻子总是早早就出门了，\n',
            '早饭只好我来做了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '午饭各自解决，\n',
            '晚饭的话则是谁到家早\n',
            '就由谁来做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BA4')

    def _loc_6D2(): pass

    label('loc_6D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_6DC',
    )

    Jump('loc_BA4')

    def _loc_6DC(): pass

    label('loc_6DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_736',
    )

    ChrTalk(
        0x00FE,
        (
            '今天是去大圣堂\n',
            '祈祷的日子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要在中午之前\n',
            '把家里收拾得干干净净才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BA4')

    def _loc_736(): pass

    label('loc_736')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_824',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_799',
    )

    ChrTalk(
        0x00FE,
        (
            '有的时候\n',
            '我很羡慕妻子的生活方式呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她的这种洒脱\n',
            '大概就是她的魅力所在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_821')

    def _loc_799(): pass

    label('loc_799')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '悄悄告诉你啊，\n',
            '有时候我很羡慕妻子的生活方式呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '我怎么都不能学会像她那样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她的这种洒脱\n',
            '大概就是她的魅力所在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_821(): pass

    label('loc_821')

    Jump('loc_BA4')

    def _loc_824(): pass

    label('loc_824')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_82E',
    )

    Jump('loc_BA4')

    def _loc_82E(): pass

    label('loc_82E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_91D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_862',
    )

    ChrTalk(
        0x00FE,
        (
            '有个大款妻子\n',
            '还真是辛苦啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_91A')

    def _loc_862(): pass

    label('loc_862')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '作为一个宗教信徒，\n',
            '我希望妻子也能够花钱适度，\n',
            '过有节制的生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，巡礼所花的费用\n',
            '妻子却全部替我掏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且我又\n',
            '是个上门女婿，\n',
            '面子上真有点挂不住啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉唉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_91A(): pass

    label('loc_91A')

    Jump('loc_BA4')

    def _loc_91D(): pass

    label('loc_91D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_995',
    )

    ChrTalk(
        0x00FE,
        (
            '妻子继承她父亲的事业\n',
            '经营百货店，\n',
            '已经赚了很多钱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '旅行结束之后，\n',
            '今天立刻就开始\n',
            '到店里去工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BA4')

    def _loc_995(): pass

    label('loc_995')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_B29',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_A2B',
    )

    ChrTalk(
        0x00FE,
        (
            '分布在王国各地的七耀教会\n',
            '在几百年前就已经存在了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了纪念大崩坏之后\n',
            '引导人们的女神而在王国各地旅行，\n',
            '的确非常的有意义啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B26')

    def _loc_A2B(): pass

    label('loc_A2B')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '分布在王国各地的七耀教会\n',
            '在几百年前就已经存在了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为了纪念大崩坏之后\n',
            '引导人们的女神而在王国各地旅行，\n',
            '的确非常的有意义啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我平日里就和忙碌的妻子\n',
            '一起度过这些时光。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '日子虽然过得很平淡，\n',
            '但是能够买到许多好东西，\n',
            '妻子也很满足了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B26(): pass

    label('loc_B26')

    Jump('loc_BA4')

    def _loc_B29(): pass

    label('loc_B29')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_BA4',
    )

    ChrTalk(
        0x00FE,
        (
            '巡礼过王国所有的七耀教会之后，\n',
            '我终于又回到了自己的家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好久没有去大圣堂看看了，\n',
            '才发现来了一位新的修女。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BA4(): pass

    label('loc_BA4')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xBA8
@scena.Code('func_07_BA8')
def func_07_BA8():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_BB5',
    )

    Jump('loc_FED')

    def _loc_BB5(): pass

    label('loc_BB5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_BBF',
    )

    Jump('loc_FED')

    def _loc_BBF(): pass

    label('loc_BBF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_BEE',
    )

    ChrTalk(
        0x00FE,
        (
            '那～么，\n',
            '差不多该去店里上班了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FED')

    def _loc_BEE(): pass

    label('loc_BEE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_C35',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，\n',
            '老公还没有回来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么今天只好我来做饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FED')

    def _loc_C35(): pass

    label('loc_C35')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_C3F',
    )

    Jump('loc_FED')

    def _loc_C3F(): pass

    label('loc_C3F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_D2D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_CA9',
    )

    ChrTalk(
        0x00FE,
        (
            '丈夫要是能够\n',
            '学会享受人生就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果这也不行，\n',
            '那也不行的话，\n',
            '会很没意思的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D2A')

    def _loc_CA9(): pass

    label('loc_CA9')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '丈夫要是能够\n',
            '学会享受人生就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果这也不行，\n',
            '那也不行的话，\n',
            '会很没意思的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过那股认真劲\n',
            '也是他的优点呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D2A(): pass

    label('loc_D2A')

    Jump('loc_FED')

    def _loc_D2D(): pass

    label('loc_D2D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_D37',
    )

    Jump('loc_FED')

    def _loc_D37(): pass

    label('loc_D37')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_E46',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_DB8',
    )

    ChrTalk(
        0x00FE,
        (
            '因为呢，一回到王都，\n',
            '自己就是经营百货店的店主，\n',
            '所以购物的乐趣也享受不到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉呀，还是想出去旅行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E43')

    def _loc_DB8(): pass

    label('loc_DB8')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '呼～工作得真辛苦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是，一回到王都，\n',
            '自己就是经营百货店的店主，\n',
            '所以购物的乐趣也享受不到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉呀，还是想出去旅行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E43(): pass

    label('loc_E43')

    Jump('loc_FED')

    def _loc_E46(): pass

    label('loc_E46')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_E50',
    )

    Jump('loc_FED')

    def _loc_E50(): pass

    label('loc_E50')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_EA8',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '明天开始要回去工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '武术大会和诞辰庆典\n',
            '是绝好的赚钱机会哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FED')

    def _loc_EA8(): pass

    label('loc_EA8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_FED',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Return,
        ),
        'loc_F33',
    )

    ChrTalk(
        0x00FE,
        (
            '我丈夫很高兴能到各地的教会去礼拜，\n',
            '而我也因为能在各地尽情购物而特别愉快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对夫妻而言，\n',
            '是一次很有意义的旅行呢㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_FED')

    def _loc_F33(): pass

    label('loc_F33')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    ChrTalk(
        0x00FE,
        (
            '哈～太忙了太忙了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在旅行中买的东西\n',
            '整理起来好费力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我丈夫很高兴能到各地的教会去，\n',
            '而我也因为能在各地尽情购物而特别愉快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对夫妻而言，\n',
            '是一次很有意义的旅行呢㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FED(): pass

    label('loc_FED')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0xFF1
@scena.Code('func_08_FF1')
def func_08_FF1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1120',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1077',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀～～～\n',
            '空港被封锁原来是\n',
            '因为政变导致的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典结束之后，\n',
            '又要回去面对\n',
            '像山一样多的工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_111D')

    def _loc_1077(): pass

    label('loc_1077')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀～～～\n',
            '空港被封锁原来是\n',
            '因为政变导致的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是托那些军人的福，\n',
            '给我带来了这么多麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典结束之后，\n',
            '又要回去面对\n',
            '像山一样多的工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_111D(): pass

    label('loc_111D')

    Jump('loc_1995')

    def _loc_1120(): pass

    label('loc_1120')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1210',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_118C',
    )

    ChrTalk(
        0x00FE,
        (
            '那些吓人的黑衣士兵\n',
            '究竟是什么来头！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大白天的\n',
            '还在王都里面巡逻，\n',
            '果然不对劲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_120D')

    def _loc_118C(): pass

    label('loc_118C')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '那些吓人的黑衣士兵\n',
            '究竟是什么来头！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '趾高气扬横行霸道，\n',
            '太讨厌了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大白天的\n',
            '还在王都里面巡逻，\n',
            '果然不对劲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_120D(): pass

    label('loc_120D')

    Jump('loc_1995')

    def _loc_1210(): pass

    label('loc_1210')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1342',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1296',
    )

    ChrTalk(
        0x00FE,
        (
            '很多人好像还不知道\n',
            '女王陛下身体欠佳，\n',
            '为了诞辰庆典纷纷来到了王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果庆典中止的话，\n',
            '他们肯定很不满吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_133F')

    def _loc_1296(): pass

    label('loc_1296')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '武术大会结束以后，\n',
            '诞辰庆典终于就要临近了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很多人好像还不知道\n',
            '女王陛下身体欠佳，\n',
            '为了诞辰庆典纷纷来到了王都。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果庆典中止的话，\n',
            '他们肯定很不满吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_133F(): pass

    label('loc_133F')

    Jump('loc_1995')

    def _loc_1342(): pass

    label('loc_1342')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_13C1',
    )

    ChrTalk(
        0x00FE,
        (
            '公爵邀请了大会优胜者\n',
            '去参加王城中的晚宴，\n',
            '可是女王还在生病，这样好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '公爵做的事\n',
            '总是那么让人觉得不舒服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1995')

    def _loc_13C1(): pass

    label('loc_13C1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_14B7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_13FB',
    )

    ChrTalk(
        0x00FE,
        (
            '希望一切都能\n',
            '回复到正常状态就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14B4')

    def _loc_13FB(): pass

    label('loc_13FB')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '不单是港口，\n',
            '现在连艾尔贝离宫都不能进入了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '就连王城也禁止游客进入参观，\n',
            '这是怎么搞的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在唯一积极的话题\n',
            '就是武术大会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望一切都能\n',
            '回复到正常状态就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14B4(): pass

    label('loc_14B4')

    Jump('loc_1995')

    def _loc_14B7(): pass

    label('loc_14B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_160C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1549',
    )

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典到来的时候估计封锁会解除，\n',
            '但这样仍旧要无所事事一段时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '军队又不会在我\n',
            '无事可做时给我发薪水，\n',
            '真让人烦恼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1609')

    def _loc_1549(): pass

    label('loc_1549')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '军队加强了警戒，\n',
            '这样看来港口的封锁\n',
            '暂时是无法解除了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典到来的时候估计封锁会解除，\n',
            '但这样仍旧要无所事事一段时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '军队又不会在我\n',
            '无事可做时给我发薪水，\n',
            '真让人烦恼啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1609(): pass

    label('loc_1609')

    Jump('loc_1995')

    def _loc_160C(): pass

    label('loc_160C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1736',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_169A',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，港口解除封锁以后，\n',
            '工作马上就会重新开始，\n',
            '我只能在家里等着随时回到工作岗位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '武术大会也去不成，\n',
            '无聊得不行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1733')

    def _loc_169A(): pass

    label('loc_169A')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '呼，港口解除封锁以后，\n',
            '工作马上就会重新开始，\n',
            '我只能在家里等着随时回到工作岗位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '武术大会也去不成，\n',
            '无聊得不行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之，\n',
            '好想放假啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1733(): pass

    label('loc_1733')

    Jump('loc_1995')

    def _loc_1736(): pass

    label('loc_1736')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_184F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_17AC',
    )

    ChrTalk(
        0x00FE,
        (
            '军方口中的恐怖分子\n',
            '就是指亲卫队吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让我说的话，\n',
            '昨天参加比赛的\n',
            '特务部队倒真的有点像坏人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_184C')

    def _loc_17AC(): pass

    label('loc_17AC')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '军方口中的恐怖分子\n',
            '就是指亲卫队吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '亲卫队虽说\n',
            '有些刻板守旧，\n',
            '但我不认为他们是坏人呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让我说的话，\n',
            '昨天参加比赛的\n',
            '特务部队倒真的有点像坏人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_184C(): pass

    label('loc_184C')

    Jump('loc_1995')

    def _loc_184F(): pass

    label('loc_184F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_18B0',
    )

    ChrTalk(
        0x00FE,
        (
            '希望王国军\n',
            '早日从港口撤离。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从卢安来的船只\n',
            '不能进入港口，\n',
            '在湖面上进退两难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1995')

    def _loc_18B0(): pass

    label('loc_18B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1959',
    )

    ChrTalk(
        0x00FE,
        (
            '从卢安运来的货物\n',
            '是要从格兰赛尔的\n',
            '港口卸下来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是，\n',
            '现在王国军为了对付恐怖组织\n',
            '而把港口封锁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这下我们的工作就不得不停滞了，\n',
            '真是困扰啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1995')

    def _loc_1959(): pass

    label('loc_1959')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1995',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，格兰赛尔港口的封锁\n',
            '要到什么时候才结束啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1995(): pass

    label('loc_1995')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x1999
@scena.Code('func_09_1999')
def func_09_1999():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_19A6',
    )

    Jump('loc_1E6E')

    def _loc_19A6(): pass

    label('loc_19A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_19FD',
    )

    ChrTalk(
        0x00FE,
        (
            '港口被封锁了，\n',
            '我现在也没事可做了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '接下来该轮到什么地方遭殃了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E6E')

    def _loc_19FD(): pass

    label('loc_19FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_1AD3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1A58',
    )

    ChrTalk(
        0x00FE,
        (
            '这儿附近有一间\n',
            '在出售的房子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我这个家太小，\n',
            '很想住到那边去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1AD0')

    def _loc_1A58(): pass

    label('loc_1A58')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '这儿附近有一间\n',
            '在出售的房子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我这个家太小，\n',
            '很想住到那边去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '努力工作，再借点钱，\n',
            '应该就可以了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1AD0(): pass

    label('loc_1AD0')

    Jump('loc_1E6E')

    def _loc_1AD3(): pass

    label('loc_1AD3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_1B38',
    )

    ChrTalk(
        0x00FE,
        (
            '呀～\n',
            '决赛真是十分精彩呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明天开始要加油工作。\n',
            '我感觉到活力\n',
            '源源不断地涌上来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E6E')

    def _loc_1B38(): pass

    label('loc_1B38')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1B90',
    )

    ChrTalk(
        0x00FE,
        (
            '今天我要和妻子\n',
            '一起去看总决赛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以这个为起点，\n',
            '从现在开始我要努力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E6E')

    def _loc_1B90(): pass

    label('loc_1B90')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1C80',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_1BFA',
    )

    ChrTalk(
        0x00FE,
        (
            '我和妻子约定，\n',
            '以后少抽烟，赶快去找工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '然后，\n',
            '妻子就允许我\n',
            '去看武术大会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C7D')

    def _loc_1BFA(): pass

    label('loc_1BFA')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '我和妻子约定，\n',
            '以后少抽烟，赶快去找工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '然后，\n',
            '妻子就允许我\n',
            '去看武术大会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然这样，\n',
            '我就要更加努力才行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C7D(): pass

    label('loc_1C7D')

    Jump('loc_1E6E')

    def _loc_1C80(): pass

    label('loc_1C80')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1CD5',
    )

    ChrTalk(
        0x00FE,
        (
            '好，我也是个男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我决定了，\n',
            '要好好努力！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '认真去找工作吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E6E')

    def _loc_1CD5(): pass

    label('loc_1CD5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1D48',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～这样下去的话\n',
            '生活确实也会很辛苦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '本来想着一定\n',
            '要去找工作的，\n',
            '但不知不觉又被耽搁了下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E6E')

    def _loc_1D48(): pass

    label('loc_1D48')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1DA0',
    )

    ChrTalk(
        0x00FE,
        (
            '总算是搬到\n',
            '向往已久的王都来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典期间\n',
            '一定要好好轻松一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E6E')

    def _loc_1DA0(): pass

    label('loc_1DA0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1E04',
    )

    ChrTalk(
        0x00FE,
        (
            '呼～\n',
            '武术大会的门票也太贵了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且一点折扣都不打，\n',
            '杜南公爵果然一点都不精明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E6E')

    def _loc_1E04(): pass

    label('loc_1E04')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1E6E',
    )

    ChrTalk(
        0x00FE,
        (
            '我们家是最近\n',
            '才搬到格兰赛尔来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从孩提时代开始，\n',
            '我就一直向往着能够\n',
            '在华丽的王都生活。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E6E(): pass

    label('loc_1E6E')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1E72
@scena.Code('func_0A_1E72')
def func_0A_1E72():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_1E7F',
    )

    Jump('loc_22A1')

    def _loc_1E7F(): pass

    label('loc_1E7F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_1EB4',
    )

    ChrTalk(
        0x00FE,
        (
            '那些士兵究竟\n',
            '要在街上呆到什么时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22A1')

    def _loc_1EB4(): pass

    label('loc_1EB4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2004',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_1F4F',
    )

    ChrTalk(
        0x00FE,
        (
            '之前还说\n',
            '为了将来出生的孩子\n',
            '要去买布娃娃回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '首先，还不知道宝宝\n',
            '会是男孩还是女孩呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '为什么就不能\n',
            '先考虑一下再行动呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2001')

    def _loc_1F4F(): pass

    label('loc_1F4F')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '刚刚出门没多久，\n',
            '马上就跑回来了，\n',
            '竟然说想买房子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明现在这间房子的\n',
            '房租都没有付清，\n',
            '竟然还去异想天开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在那之前还是\n',
            '快点找好工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，前路漫漫……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2001(): pass

    label('loc_2001')

    Jump('loc_22A1')

    def _loc_2004(): pass

    label('loc_2004')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_2062',
    )

    ChrTalk(
        0x00FE,
        (
            '作为去观看大会的条件，\n',
            '他说会去找工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我担心他是否会\n',
            '好好遵守诺言……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22A1')

    def _loc_2062(): pass

    label('loc_2062')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_209D',
    )

    ChrTalk(
        0x00FE,
        (
            '现在想想的话，\n',
            '我也已经很久没有和他约会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22A1')

    def _loc_209D(): pass

    label('loc_209D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_20F3',
    )

    ChrTalk(
        0x00FE,
        (
            '最后还是我先开口\n',
            '说了关于大会的事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼～\n',
            '我还是心太软了一些。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22A1')

    def _loc_20F3(): pass

    label('loc_20F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_2143',
    )

    ChrTalk(
        0x00FE,
        (
            '好，决定了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须要把我的想法\n',
            '告诉他才行，\n',
            '要好好和他谈谈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22A1')

    def _loc_2143(): pass

    label('loc_2143')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_21A0',
    )

    ChrTalk(
        0x00FE,
        (
            '他这个人\n',
            '确实是个懒鬼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是会变成那样\n',
            '我也有责任，\n',
            '是我太娇惯他了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22A1')

    def _loc_21A0(): pass

    label('loc_21A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_220B',
    )

    ChrTalk(
        0x00FE,
        (
            '他完全没有打算\n',
            '要去找点事情做，\n',
            '哪怕『一点点』都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '对这样的人是没什么指望了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22A1')

    def _loc_220B(): pass

    label('loc_220B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_224C',
    )

    ChrTalk(
        0x00FE,
        (
            '真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '家里哪有那么多钱\n',
            '去看武术大会啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22A1')

    def _loc_224C(): pass

    label('loc_224C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_22A1',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '虽说能搬到憧憬已久的王都是很不错，\n',
            '但我丈夫现在变得就知道游手好闲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22A1(): pass

    label('loc_22A1')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x22A5
@scena.Code('func_0B_22A5')
def func_0B_22A5():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_22B2',
    )

    Jump('loc_26AE')

    def _loc_22B2(): pass

    label('loc_22B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_22EF',
    )

    ChrTalk(
        0x00FE,
        (
            '今天的士兵\n',
            '比平日多了不少……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好可怕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26AE')

    def _loc_22EF(): pass

    label('loc_22EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2352',
    )

    ChrTalk(
        0x00FE,
        (
            '女王陛下不但是国家的支柱，\n',
            '而且也是格兰赛尔市民的骄傲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望她能够早日康复。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26AE')

    def _loc_2352(): pass

    label('loc_2352')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_23B2',
    )

    ChrTalk(
        0x00FE,
        (
            '我啊～\n',
            '太过专注于比赛了，\n',
            '不由自主地就站了起来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵呵，真是不好意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26AE')

    def _loc_23B2(): pass

    label('loc_23B2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_23E8',
    )

    ChrTalk(
        0x00FE,
        (
            '呵呵呵，老头子啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再等一下嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26AE')

    def _loc_23E8(): pass

    label('loc_23E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2441',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '今天的晚饭做什么好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '油炸土豆和\n',
            '爆炒野生菌，\n',
            '做哪一个呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26AE')

    def _loc_2441(): pass

    label('loc_2441')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_254A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_24B6',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，那些人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像在昨天的\n',
            '比赛中出场了嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '记得好像还输给了\n',
            '共和国的那个选手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2547')

    def _loc_24B6(): pass

    label('loc_24B6')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '今天一早就和老头子\n',
            '去百货店采购了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没想到东西很沉，\n',
            '正在发愁……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这时，\n',
            '路过的一群围红头巾的小伙子\n',
            '帮我们把东西全部抬回家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2547(): pass

    label('loc_2547')

    Jump('loc_26AE')

    def _loc_254A(): pass

    label('loc_254A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_25BF',
    )

    ChrTalk(
        0x00FE,
        (
            '我们老俩口已经\n',
            '从王城里得到了门票，\n',
            '去看了比赛的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵呵，老头子他\n',
            '就像小孩子一样欢呼雀跃……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26AE')

    def _loc_25BF(): pass

    label('loc_25BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_25F8',
    )

    ChrTalk(
        0x00FE,
        (
            '对了，午后还要出门，\n',
            '得早点打扫完房间呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26AE')

    def _loc_25F8(): pass

    label('loc_25F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2660',
    )

    ChrTalk(
        0x00FE,
        (
            '武术大会开始了，\n',
            '人们的心情也一下子活跃起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '保持愉快的生活态度\n',
            '才能够更加长寿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_26AE')

    def _loc_2660(): pass

    label('loc_2660')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_26AE',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，外面好热闹啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说岁月不饶人，\n',
            '但也会跟着兴奋起来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_26AE(): pass

    label('loc_26AE')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x26B2
@scena.Code('func_0C_26B2')
def func_0C_26B2():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_26BF',
    )

    Jump('loc_2A6C')

    def _loc_26BF(): pass

    label('loc_26BF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_26EA',
    )

    ChrTalk(
        0x00FE,
        (
            '总感觉\n',
            '外面有些不大对劲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A6C')

    def _loc_26EA(): pass

    label('loc_26EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_275B',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '真是挂念女王陛下的病情啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说我也很担心恐怖事件，\n',
            '但更加希望陛下可以\n',
            '健康长寿啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A6C')

    def _loc_275B(): pass

    label('loc_275B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_27C8',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀哎呀～\n',
            '比赛真的是很精彩呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我虽然不太懂武术，\n',
            '看不明白那些招式，\n',
            '不过也能乐在其中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A6C')

    def _loc_27C8(): pass

    label('loc_27C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2803',
    )

    ChrTalk(
        0x00FE,
        (
            '老婆子，不快点的话，\n',
            '就占不到好的位子了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A6C')

    def _loc_2803(): pass

    label('loc_2803')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2846',
    )

    ChrTalk(
        0x00FE,
        (
            '老婆子做的饭我虽然吃了几十年，\n',
            '但仍旧觉得是极品啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A6C')

    def _loc_2846(): pass

    label('loc_2846')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_28BB',
    )

    ChrTalk(
        0x00FE,
        (
            '我们上了年纪的人总爱对\n',
            '年轻人的行为说三道四……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但回想一下，\n',
            '我们年轻的时候，\n',
            '也是经常被教训啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A6C')

    def _loc_28BB(): pass

    label('loc_28BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_2925',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，愉快愉快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们的孙子和其他孩子们\n',
            '能够在这样一个和平的时代生活，\n',
            '实在是幸福啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A6C')

    def _loc_2925(): pass

    label('loc_2925')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2958',
    )

    ChrTalk(
        0x00FE,
        (
            '早上好，\n',
            '今天又是一个清爽的早晨呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A6C')

    def _loc_2958(): pass

    label('loc_2958')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2A6C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_29C4',
    )

    ChrTalk(
        0x00FE,
        (
            '我们这些老人\n',
            '都是从呱呱坠地到现在\n',
            '一直在格兰赛尔居住的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这条街道\n',
            '还是没有变啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2A6C')

    def _loc_29C4(): pass

    label('loc_29C4')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '听说女王陛下身体欠佳时，\n',
            '大家的心情都很沉重，\n',
            '到现在才稍微好一些了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们这些老人\n',
            '都是从呱呱坠地到现在\n',
            '一直在格兰赛尔居住的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这条街道\n',
            '还是没有变啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2A6C(): pass

    label('loc_2A6C')

    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x2A70
@scena.Code('func_0D_2A70')
def func_0D_2A70():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2AC7',
    )

    ChrTalk(
        0x00FE,
        (
            '这起政变竟然是\n',
            '理查德上校策划的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们一直都被\n',
            '上校给欺骗了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EEA')

    def _loc_2AC7(): pass

    label('loc_2AC7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2B1E',
    )

    ChrTalk(
        0x00FE,
        (
            '一群黑衣士兵在外面警备着，\n',
            '气氛似乎很不妙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最好还是不要出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EEA')

    def _loc_2B1E(): pass

    label('loc_2B1E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_2B90',
    )

    ChrTalk(
        0x00FE,
        (
            '我简直难以相信恐怖事件\n',
            '是亲卫队一手策划的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过既然是那位理查德上校说的，\n',
            '那应该就是真的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EEA')

    def _loc_2B90(): pass

    label('loc_2B90')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_2C74',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2BF7',
    )

    ChrTalk(
        0x00FE,
        (
            '比起我得不断地提醒她，\n',
            '最好还是让她能\n',
            '自觉去做家务……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '夫妻间的协调很难呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2C71')

    def _loc_2BF7(): pass

    label('loc_2BF7')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '今天我妻子把\n',
            '家务都做好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比起我得不断地提醒她，\n',
            '最好还是让她能\n',
            '自觉去做家务……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '夫妻间的协调很难呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2C71(): pass

    label('loc_2C71')

    Jump('loc_2EEA')

    def _loc_2C74(): pass

    label('loc_2C74')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_2C7E',
    )

    Jump('loc_2EEA')

    def _loc_2C7E(): pass

    label('loc_2C7E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_2C88',
    )

    Jump('loc_2EEA')

    def _loc_2C88(): pass

    label('loc_2C88')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_2D01',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2CC0',
    )

    ChrTalk(
        0x00FE,
        (
            '为了以后不再吵架\n',
            '也要好好做家务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CFE')

    def _loc_2CC0(): pass

    label('loc_2CC0')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '嗯，我下定决心了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明天一定要\n',
            '把心里话告诉妻子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2CFE(): pass

    label('loc_2CFE')

    Jump('loc_2EEA')

    def _loc_2D01(): pass

    label('loc_2D01')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_2D32',
    )

    ChrTalk(
        0x00FE,
        (
            '请、请问，\n',
            '晚饭准备得怎么样了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EEA')

    def _loc_2D32(): pass

    label('loc_2D32')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_2DDA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2D61',
    )

    ChrTalk(
        0x00FE,
        (
            '我还是先做完扫除再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DD7')

    def _loc_2D61(): pass

    label('loc_2D61')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '今天我醒来时，\n',
            '妻子就不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像是大清早就\n',
            '跑到竞技场去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，都结婚五年了……\n',
            '还为这种事情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2DD7(): pass

    label('loc_2DD7')

    Jump('loc_2EEA')

    def _loc_2DDA(): pass

    label('loc_2DDA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_2EB2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_2E37',
    )

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '去看武术大会虽然没什么不好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过至少也要\n',
            '分担一些家务啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EAF')

    def _loc_2E37(): pass

    label('loc_2E37')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '去看武术大会虽然没什么不好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过至少也要\n',
            '分担一些家务啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉唉……\n',
            '和结婚前的约定截然不同啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EAF(): pass

    label('loc_2EAF')

    Jump('loc_2EEA')

    def _loc_2EB2(): pass

    label('loc_2EB2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_2EEA',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，妻子外出了，\n',
            '可以好好地收拾一下房间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EEA(): pass

    label('loc_2EEA')

    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x2EEE
@scena.Code('func_0E_2EEE')
def func_0E_2EEE():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2F79',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然好久没见面了，\n',
            '但科洛蒂娅公主的确\n',
            '是成长了许多呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '她是比杜南公爵要合适\n',
            '１００００００００００倍的\n',
            '王位继承者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3341')

    def _loc_2F79(): pass

    label('loc_2F79')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_2FCE',
    )

    ChrTalk(
        0x00FE,
        (
            '无论哪里，到处都是士兵，\n',
            '就像是在监视我们一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '感觉不太舒服啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3341')

    def _loc_2FCE(): pass

    label('loc_2FCE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_302F',
    )

    ChrTalk(
        0x00FE,
        (
            '一般武术大会结束以后，\n',
            '马上就要开始诞辰庆典的准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，今年会怎么样呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3341')

    def _loc_302F(): pass

    label('loc_302F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_3118',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_3067',
    )

    ChrTalk(
        0x00FE,
        (
            '哈～\n',
            '决赛真是眼花缭乱的攻防战呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3115')

    def _loc_3067(): pass

    label('loc_3067')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '哈～\n',
            '决赛真是眼花缭乱的攻防战呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们是在非常好的\n',
            '坐席看比赛的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x00FE,
        (
            '而且我也更加明白\n',
            '丈夫对我的爱了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天是最美的一天啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3115(): pass

    label('loc_3115')

    Jump('loc_3341')

    def _loc_3118(): pass

    label('loc_3118')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_3122',
    )

    Jump('loc_3341')

    def _loc_3122(): pass

    label('loc_3122')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_324A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_318F',
    )

    ChrTalk(
        0x00FE,
        (
            '因为上次没能占到好位子，\n',
            '今天本打算熬夜排队的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '丈夫说很危险，\n',
            '就去替我排队了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3247')

    def _loc_318F(): pass

    label('loc_318F')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '因为上次没能占到好位子，\n',
            '今天本打算熬夜排队的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '丈夫说很危险，\n',
            '就去替我排队了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……啊、啊呀，作为男人，\n',
            '同时作为丈夫，那样也是应该的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3247(): pass

    label('loc_3247')

    Jump('loc_3341')

    def _loc_324A(): pass

    label('loc_324A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_3254',
    )

    Jump('loc_3341')

    def _loc_3254(): pass

    label('loc_3254')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_32C5',
    )

    ChrTalk(
        0x00FE,
        (
            '果然在那个时机\n',
            '应该用射程远的导力枪牵制敌人，\n',
            '然后对其进行斩击。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '攻守的转换\n',
            '还是不够协调啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3341')

    def _loc_32C5(): pass

    label('loc_32C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_32CF',
    )

    Jump('loc_3341')

    def _loc_32CF(): pass

    label('loc_32CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_333A',
    )

    ChrTalk(
        0x00FE,
        (
            '虽说是预选赛，\n',
            '不过今天的比赛\n',
            '每一场都很精彩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然就是要从预选赛开始\n',
            '一场不漏地看啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3341')

    def _loc_333A(): pass

    label('loc_333A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_3341',
    )

    def _loc_3341(): pass

    label('loc_3341')

    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
