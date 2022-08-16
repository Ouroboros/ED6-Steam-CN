import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2110_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2110   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2110.x'
    header.mapIndex       = 1
    header.bgm            = 12
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH01230._CH', 'ED6_DT07/CH01230P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01540._CH', 'ED6_DT07/CH01540P._CP'),
        ('ED6_DT07/CH01170._CH', 'ED6_DT07/CH01170P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01470._CH', 'ED6_DT07/CH01470P._CP'),
    ]

# id: 0x10001 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '布丽奇特',
            x                   = 24980,
            z                   = 0,
            y                   = 62760,
            direction           = 90,
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
            name                = '贝尔夫',
            x                   = -28000,
            z                   = 0,
            y                   = 61400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            name                = '希艾尔',
            x                   = 1950,
            z                   = 0,
            y                   = 5470,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '爱蕾塔',
            x                   = -470,
            z                   = 0,
            y                   = 1090,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '连茨',
            x                   = 23690,
            z                   = 0,
            y                   = 4490,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '丽泽',
            x                   = 27150,
            z                   = 0,
            y                   = -1550,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '托尼奥',
            x                   = 26000,
            z                   = 4000,
            y                   = -510,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '诺莉雅',
            x                   = -5740,
            z                   = 0,
            y                   = 35100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '路易',
            x                   = 5430,
            z                   = 0,
            y                   = 64750,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
    )

# id: 0x10002 offset: 0x212
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x212
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x212
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x212
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_232',
    )

    ChrSetFlags(0x0009, 0x0080)
    ChrSetPos(0x000D, 27250, 0, -1740, 87)

    Jump('loc_2A8')

    def _loc_232(): pass

    label('loc_232')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_24B',
    )

    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)

    Jump('loc_2A8')

    def _loc_24B(): pass

    label('loc_24B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_27F',
    )

    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetPos(0x000A, 1700, 0, 2029, 90)

    Jump('loc_2A8')

    def _loc_27F(): pass

    label('loc_27F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_28E',
    )

    ChrSetFlags(0x000C, 0x0080)

    Jump('loc_2A8')

    def _loc_28E(): pass

    label('loc_28E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_29C',
    )

    Jump('loc_2A8')

    def _loc_29C(): pass

    label('loc_29C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_2A8',
    )

    ChrSetFlags(0x000C, 0x0080)

    def _loc_2A8(): pass

    label('loc_2A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 0, 0x1210)),
            Expr.Return,
        ),
        'loc_2B7',
    )

    ChrClearFlags(0x0009, 0x0010)

    Jump('loc_2DE')

    def _loc_2B7(): pass

    label('loc_2B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0241, 7, 0x120F)),
            Expr.Return,
        ),
        'loc_2D2',
    )

    ChrSetPos(0x0008, -230, 0, 63820, 270)

    Jump('loc_2DE')

    def _loc_2D2(): pass

    label('loc_2D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_2DE',
    )

    ChrSetFlags(0x0009, 0x0010)

    def _loc_2DE(): pass

    label('loc_2DE')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x0000006B, 'loc_2EA'),
        (-1, 'loc_302'),
    )

    def _loc_2EA(): pass

    label('loc_2EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0241, 6, 0x120E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0241, 7, 0x120F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2FF',
    )

    MapSetFlags(0x10000000)
    Event(0, func_0E_24A0)

    def _loc_2FF(): pass

    label('loc_2FF')

    Jump('loc_302')

    def _loc_302(): pass

    label('loc_302')

    Return()

# id: 0x0001 offset: 0x303
@scena.Code('func_01_303')
def func_01_303():
    Return()

# id: 0x0002 offset: 0x304
@scena.Code('func_02_304')
def func_02_304():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_319',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_304')

    def _loc_319(): pass

    label('loc_319')

    Return()

# id: 0x0003 offset: 0x31A
@scena.Code('func_03_31A')
def func_03_31A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_33D',
    )

    OP_8D(0x00FE, -6630, 65280, -3270, 67330, 1000)

    Jump('func_03_31A')

    def _loc_33D(): pass

    label('loc_33D')

    Return()

# id: 0x0004 offset: 0x33E
@scena.Code('func_04_33E')
def func_04_33E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_361',
    )

    OP_8D(0x00FE, -2620, 970, 1167, -2110, 3000)

    Jump('func_04_33E')

    def _loc_361(): pass

    label('loc_361')

    Return()

# id: 0x0005 offset: 0x362
@scena.Code('func_05_362')
def func_05_362():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_40D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3CD',
    )

    ChrTalk(
        0x00FE,
        (
            '哥哥他说要帮\n',
            '爸爸的忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哥哥也在努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也要努力帮妈妈的忙哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))

    Jump('loc_40A')

    def _loc_3CD(): pass

    label('loc_3CD')

    ChrTalk(
        0x00FE,
        (
            '哥哥他说要帮\n',
            '爸爸的忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也要努力帮妈妈的忙哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_40A(): pass

    label('loc_40A')

    Jump('loc_529')

    def _loc_40D(): pass

    label('loc_40D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_471',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器停止了\n',
            '爸爸的工作也很受影响呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，我爸爸很厉害。\n',
            '一定会马上修好的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_529')

    def _loc_471(): pass

    label('loc_471')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_4B3',
    )

    ChrTalk(
        0x00FE,
        (
            '我哥哥\n',
            '已经开始工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像在帮\n',
            '爸爸的忙呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_529')

    def _loc_4B3(): pass

    label('loc_4B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_4BD',
    )

    Jump('loc_529')

    def _loc_4BD(): pass

    label('loc_4BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_4F0',
    )

    ChrTalk(
        0x00FE,
        (
            '爸爸这次\n',
            '因为选举一直不在家呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_529')

    def _loc_4F0(): pass

    label('loc_4F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_529',
    )

    ChrTalk(
        0x00FE,
        (
            '哥哥，\n',
            '都不跟我玩～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好难得\n',
            '才回家一次～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_529(): pass

    label('loc_529')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x52D
@scena.Code('func_06_52D')
def func_06_52D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_65A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5F5',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然是传言，\n',
            '听说学院出了事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，我儿子罗基克\n',
            '应该没事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那家伙意外的谨慎，\n',
            '应该早早的就逃出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比起勇敢的孩子，胆小的孩子\n',
            '反而更能让父母安心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_657')

    def _loc_5F5(): pass

    label('loc_5F5')

    ChrTalk(
        0x00FE,
        (
            '虽说学院好像出了事，\n',
            '我儿子罗基克应该没事的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那家伙意外的谨慎，\n',
            '应该早早的就逃出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_657(): pass

    label('loc_657')

    Jump('loc_A10')

    def _loc_65A(): pass

    label('loc_65A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_770',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_719',
    )

    ChrTalk(
        0x00FE,
        (
            '因为导力器停止了，\n',
            '港湾区那边一片混乱啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我先生被市长一大清早\n',
            '叫出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '即使在选举中输了，\n',
            '为了那家伙还是尽心尽力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我先生\n',
            '真是个没心机的老好人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_76D')

    def _loc_719(): pass

    label('loc_719')

    ChrTalk(
        0x00FE,
        (
            '因为导力器停止了，\n',
            '港湾区那边一片混乱啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我先生被市长一大清早\n',
            '叫出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_76D(): pass

    label('loc_76D')

    Jump('loc_A10')

    def _loc_770(): pass

    label('loc_770')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_7D6',
    )

    ChrTalk(
        0x00FE,
        (
            '过几天我去先生\n',
            '工作的地方看望他一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不去鞭策他一下\n',
            '马上就会说出没出息的话了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A10')

    def _loc_7D6(): pass

    label('loc_7D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_835',
    )

    ChrTalk(
        0x00FE,
        (
            '好像是支持者之间\n',
            '发生了争执呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '既然是我先生，\n',
            '肯定是打算阻止\n',
            '又没成功吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A10')

    def _loc_835(): pass

    label('loc_835')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_90B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_89A',
    )

    ChrTalk(
        0x00FE,
        (
            '我儿子罗基克\n',
            '什么事情都喜欢讲道理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '什么事都是一堆理论，\n',
            '真让我头疼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_908')

    def _loc_89A(): pass

    label('loc_89A')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '说起来，王立学院\n',
            '马上就要放长假了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那儿子一整天\n',
            '都要待在家里了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，想想\n',
            '都觉得头疼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_908(): pass

    label('loc_908')

    Jump('loc_A10')

    def _loc_90B(): pass

    label('loc_90B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_A10',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Return,
        ),
        'loc_982',
    )

    ChrTalk(
        0x00FE,
        (
            '我先生就算当了市长候选人\n',
            '还是那么没出息啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想知道他什么样子，\n',
            '就出去看看外面的墙壁就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A10')

    def _loc_982(): pass

    label('loc_982')

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '我先生就算当了市长候选人\n',
            '还是那么没出息啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '换句话说就是『胆量不够』。\n',
            '事到如今说话还打颤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '支持者们都看着，\n',
            '不能振作点吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A10(): pass

    label('loc_A10')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xA14
@scena.Code('func_07_A14')
def func_07_A14():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_AD4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A96',
    )

    ChrTalk(
        0x00FE,
        (
            '这次是学院事件吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利贝尔王国到底\n',
            '怎么回事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '入学考试能不能照预定\n',
            '进行，心里很不安啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_AD1')

    def _loc_A96(): pass

    label('loc_A96')

    ChrTalk(
        0x00FE,
        (
            '这次是学院事件吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '利贝尔王国到底\n',
            '怎么回事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AD1(): pass

    label('loc_AD1')

    Jump('loc_EC8')

    def _loc_AD4(): pass

    label('loc_AD4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_BDE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B7B',
    )

    ChrTalk(
        0x00FE,
        (
            '学院放假时，让基诺奇奥\n',
            '辅导我应考复习了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因此对于入学考试\n',
            '总算有点自信了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '导力器停了，\n',
            '怪异的东西又浮在天上，\n',
            '实在无心学习啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    Jump('loc_BDB')

    def _loc_B7B(): pass

    label('loc_B7B')

    ChrTalk(
        0x00FE,
        (
            '多亏基诺奇奥的指导，\n',
            '算是能应付入学考试了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看着世间发生的事情，\n',
            '实在没心思学习啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BDB(): pass

    label('loc_BDB')

    Jump('loc_EC8')

    def _loc_BDE(): pass

    label('loc_BDE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_C9C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_C33',
    )

    ChrTalk(
        0x00FE,
        (
            '基诺奇奥给我当\n',
            '家庭教师了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好，再坚持坚持～\n',
            '努力学习吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C99')

    def _loc_C33(): pass

    label('loc_C33')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '学院放假时\n',
            '基诺奇奥给我当\n',
            '家庭教师了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '能找到有入学考试经验的人\n',
            '来帮忙真的是事半功倍啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C99(): pass

    label('loc_C99')

    Jump('loc_EC8')

    def _loc_C9C(): pass

    label('loc_C9C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_CA6',
    )

    Jump('loc_EC8')

    def _loc_CA6(): pass

    label('loc_CA6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_CE8',
    )

    ChrTalk(
        0x00FE,
        (
            '爸爸好像慌慌张张的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……外边出什么事了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EC8')

    def _loc_CE8(): pass

    label('loc_CE8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_DF5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_D64',
    )

    ChrTalk(
        0x00FE,
        (
            '基诺奇奥\n',
            '要是能来辅导复习\n',
            '对我来说是再好不过的了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是我妈妈，却对邻居\n',
            '有奇怪的抵触意识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DF2')

    def _loc_D64(): pass

    label('loc_D64')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '隔壁的基诺奇奥\n',
            '已经是王立学院的学生了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果能请他来辅导我应试复习\n',
            '我就安心多了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是我妈妈，却对邻居\n',
            '有奇怪的抵触意识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DF2(): pass

    label('loc_DF2')

    Jump('loc_EC8')

    def _loc_DF5(): pass

    label('loc_DF5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_EC8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_E64',
    )

    ChrTalk(
        0x00FE,
        (
            '但是，王立学院的入学考试\n',
            '好像相当难的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我也很努力，\n',
            '说实话还是很没自信啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EC8')

    def _loc_E64(): pass

    label('loc_E64')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '我的梦想是当飞船\n',
            '上的乘员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到王立学院\n',
            '学习自然科课程的话，\n',
            '应该就能进一步接近梦想吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EC8(): pass

    label('loc_EC8')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0xECC
@scena.Code('func_08_ECC')
def func_08_ECC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_F8C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F38',
    )

    ChrTalk(
        0x00FE,
        (
            '小道消息，\n',
            '学院好像出事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '据说已经平安解决了，\n',
            '现在王国军在学院警备哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_F89')

    def _loc_F38(): pass

    label('loc_F38')

    ChrTalk(
        0x00FE,
        (
            '学院好像出事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，据说已经平安解决了，\n',
            '现在似乎是王国军在警备哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F89(): pass

    label('loc_F89')

    Jump('loc_1341')

    def _loc_F8C(): pass

    label('loc_F8C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1059',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1014',
    )

    ChrTalk(
        0x00FE,
        (
            '唔唔，灯油\n',
            '放在哪里了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '儿子的应试复习\n',
            '也到了关键时刻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论如何要保证桌子上\n',
            '的灯一直亮着才行啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_1056')

    def _loc_1014(): pass

    label('loc_1014')

    ChrTalk(
        0x00FE,
        (
            '唔唔，灯油\n',
            '放在哪里了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，干脆让先生\n',
            '去买好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1056(): pass

    label('loc_1056')

    Jump('loc_1341')

    def _loc_1059(): pass

    label('loc_1059')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1139',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_10C0',
    )

    ChrTalk(
        0x00FE,
        (
            '家庭教师也请了，\n',
            '这样应付考试就万全了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，还有学费\n',
            '得想办法准备好才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1136')

    def _loc_10C0(): pass

    label('loc_10C0')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '因为王立学院放假了，\n',
            '就拜托基诺奇奥\n',
            '来辅导儿子的学习了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然拜托邻居很不甘心，\n',
            '为了儿子就含泪忍下来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1136(): pass

    label('loc_1136')

    Jump('loc_1341')

    def _loc_1139(): pass

    label('loc_1139')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_1187',
    )

    ChrTalk(
        0x00FE,
        (
            '儿子也相当\n',
            '有干劲呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '上主日学校的时候\n',
            '他自己就很用功呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1341')

    def _loc_1187(): pass

    label('loc_1187')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_11B6',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，什么事……\n',
            '大街上好吵呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1341')

    def _loc_11B6(): pass

    label('loc_11B6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1282',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_120F',
    )

    ChrTalk(
        0x00FE,
        (
            '家庭教师只能\n',
            '拜托基诺奇奥吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '拜托邻居\n',
            '真是有点懊恼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_127F')

    def _loc_120F(): pass

    label('loc_120F')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '不过儿子说了\n',
            '一切以考试为重。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '基诺奇奥的话\n',
            '正适合当家庭教师呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，拜托邻居\n',
            '实在有点懊恼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_127F(): pass

    label('loc_127F')

    Jump('loc_1341')

    def _loc_1282(): pass

    label('loc_1282')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_1341',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_12EE',
    )

    ChrTalk(
        0x00FE,
        (
            '不过无论如何\n',
            '也希望儿子托尼奥\n',
            '能考上王立学院啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望别有什么事\n',
            '妨碍到他学习哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1341')

    def _loc_12EE(): pass

    label('loc_12EE')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '真讨厌，\n',
            '选举运动的声音这么吵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样儿子学习\n',
            '不是无法集中精神了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1341(): pass

    label('loc_1341')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x1345
@scena.Code('func_09_1345')
def func_09_1345():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_1397',
    )

    ChrTalk(
        0x00FE,
        (
            '真的出了事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，这也说那也说，\n',
            '传言完全不能相信啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_160C')

    def _loc_1397(): pass

    label('loc_1397')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_147C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1427',
    )

    ChrTalk(
        0x00FE,
        (
            '我预定要乘的船\n',
            '也在海上抛锚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '推进器的导力输出装置\n',
            '好象完全没反应了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '没办法，我们\n',
            '也只好在自己家待命了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_1479')

    def _loc_1427(): pass

    label('loc_1427')

    ChrTalk(
        0x00FE,
        (
            '我预定要乘的船\n',
            '也在海上抛锚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '推进器的导力输出装置\n',
            '好象完全没反应了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1479(): pass

    label('loc_1479')

    Jump('loc_160C')

    def _loc_147C(): pass

    label('loc_147C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1548',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_14D3',
    )

    ChrTalk(
        0x00FE,
        (
            '儿子好像想当\n',
            '飞船的船员呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，果然\n',
            '是船员的儿子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1545')

    def _loc_14D3(): pass

    label('loc_14D3')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '儿子好像想当\n',
            '飞船的船员呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然是在天上飞的，\n',
            '那和船也没多大区别。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，果然\n',
            '是船员的儿子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1545(): pass

    label('loc_1545')

    Jump('loc_160C')

    def _loc_1548(): pass

    label('loc_1548')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_160C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_158A',
    )

    ChrTalk(
        0x00FE,
        (
            '诺曼先生是很出色的人，\n',
            '但就是对公约不重视。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_160C')

    def _loc_158A(): pass

    label('loc_158A')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '诺曼先生是很出色的人，\n',
            '但就是对公约不重视。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '卢安就不是旅游城市，\n',
            '原本就是船员和渔夫的城市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这点最好\n',
            '别搞错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_160C(): pass

    label('loc_160C')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1610
@scena.Code('func_0A_1610')
def func_0A_1610():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_165B',
    )

    ChrTalk(
        0x00FE,
        (
            '基诺奇奥哥哥\n',
            '才不会输给考试呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为哥哥\n',
            '很厉害的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1802')

    def _loc_165B(): pass

    label('loc_165B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_16A6',
    )

    ChrTalk(
        0x00FE,
        (
            '放假结束，\n',
            '基诺奇奥哥哥也要回学校了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '学校没事了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1802')

    def _loc_16A6(): pass

    label('loc_16A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_16E7',
    )

    ChrTalk(
        0x00FE,
        (
            '选举的声音没有了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '叔叔们是不是\n',
            '回家了呢～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1802')

    def _loc_16E7(): pass

    label('loc_16E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_171F',
    )

    ChrTalk(
        0x00FE,
        (
            '今天有主日学校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啦，真期待啊⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1802')

    def _loc_171F(): pass

    label('loc_171F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_1802',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1782',
    )

    ChrTalk(
        0x00FE,
        (
            '基诺奇奥哥哥的学校\n',
            '据说也很快就要放假了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，等他回来\n',
            '要尽情玩耍啊⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1802')

    def _loc_1782(): pass

    label('loc_1782')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，妈妈可是很久没有\n',
            '一直待在家里了⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很快基诺奇奥哥哥的\n',
            '学校也要放假了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然就是要\n',
            '大家都在家才开心啊⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1802(): pass

    label('loc_1802')

    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x1806
@scena.Code('func_0B_1806')
def func_0B_1806():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_18CF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1888',
    )

    ChrTalk(
        0x00FE,
        (
            '学院好像出事了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '待会儿得去\n',
            '隔壁问问详情才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎样现在没有消息，\n',
            '只能靠人传言了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_18CC')

    def _loc_1888(): pass

    label('loc_1888')

    ChrTalk(
        0x00FE,
        (
            '学院出事什么的\n',
            '是真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '待会儿得去\n',
            '隔壁问问详情才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18CC(): pass

    label('loc_18CC')

    Jump('loc_1D5D')

    def _loc_18CF(): pass

    label('loc_18CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_19A4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1951',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器停了，\n',
            '日常生活也不顺心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '新市长诺曼\n',
            '快点想想办法啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '至少桥的问题\n',
            '得解决了才行啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_19A1')

    def _loc_1951(): pass

    label('loc_1951')

    ChrTalk(
        0x00FE,
        (
            '导力器不能使用，\n',
            '日常生活也不顺心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '至少桥的问题\n',
            '得解决了才行啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19A1(): pass

    label('loc_19A1')

    Jump('loc_1D5D')

    def _loc_19A4(): pass

    label('loc_19A4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_1A6E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1A03',
    )

    ChrTalk(
        0x00FE,
        (
            '儿子要当隔壁托尼奥\n',
            '的家庭教师了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '托尼奥好像也想\n',
            '考进王立学院的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A6B')

    def _loc_1A03(): pass

    label('loc_1A03')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '我儿子基诺奇奥\n',
            '要当隔壁托尼奥\n',
            '的家庭教师了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然只是放假期间，\n',
            '但应该是不错的社会经验吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A6B(): pass

    label('loc_1A6B')

    Jump('loc_1D5D')

    def _loc_1A6E(): pass

    label('loc_1A6E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_1B44',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1ACB',
    )

    ChrTalk(
        0x00FE,
        (
            '一有自由的时间\n',
            '就会考虑要做什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '忙起来明明有那么多\n',
            '想做的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B41')

    def _loc_1ACB(): pass

    label('loc_1ACB')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '扫除和洗衣服都做完了，\n',
            '女儿也去上主日学校了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，难得能休息了，\n',
            '一有自由的时间\n',
            '真不知道该做些什么了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B41(): pass

    label('loc_1B41')

    Jump('loc_1D5D')

    def _loc_1B44(): pass

    label('loc_1B44')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_1B8D',
    )

    ChrTalk(
        0x00FE,
        (
            '外面还很吵闹……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '咦，不过今天\n',
            '不是有演讲会什么的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D5D')

    def _loc_1B8D(): pass

    label('loc_1B8D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1C4C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1BE3',
    )

    ChrTalk(
        0x00FE,
        (
            '女儿爱蕾塔最近\n',
            '好像有新朋友了哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这也多亏了主日学校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C49')

    def _loc_1BE3(): pass

    label('loc_1BE3')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '女儿爱蕾塔最近\n',
            '好像有新朋友了哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总是让那孩子看家\n',
            '她一定很寂寞，\n',
            '交了新朋友真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C49(): pass

    label('loc_1C49')

    Jump('loc_1D5D')

    def _loc_1C4C(): pass

    label('loc_1C4C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_1D5D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1CC9',
    )

    ChrTalk(
        0x00FE,
        (
            '选举中游客不多，\n',
            '向导的工作暂时停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '丈夫为了支援选举看起来很忙的样子，\n',
            '不过我在家倒是很悠闲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D5D')

    def _loc_1CC9(): pass

    label('loc_1CC9')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '我和丈夫一起\n',
            '做旅游向导……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '选举中游客不多，\n',
            '不过总算是暂时可以休息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '丈夫为了支援选举看起来很忙的样子，\n',
            '不过我在家倒是很悠闲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D5D(): pass

    label('loc_1D5D')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x1D61
@scena.Code('func_0C_1D61')
def func_0C_1D61():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_1E80',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E25',
    )

    ChrTalk(
        0x00FE,
        (
            '儿子贝尔夫也在市长官邸\n',
            '很努力的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望以这个为契机，\n',
            '好好考虑一下将来吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，还是不要着急\n',
            '慢慢来比较重要的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在应该好好称赞他\n',
            '肯工作才是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_1E7D')

    def _loc_1E25(): pass

    label('loc_1E25')

    ChrTalk(
        0x00FE,
        (
            '儿子贝尔夫也在市长官邸\n',
            '很努力的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次我们做父母的\n',
            '可得认可那孩子才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E7D(): pass

    label('loc_1E7D')

    Jump('loc_223E')

    def _loc_1E80(): pass

    label('loc_1E80')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1F80',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1F1A',
    )

    ChrTalk(
        0x00FE,
        (
            '我先生诺曼\n',
            '已经好几天没从\n',
            '市长官邸回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '身为新任市长要急迫处理事态\n',
            '的紧张心情也能够理解……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只是不要太拼命了就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    Jump('loc_1F7D')

    def _loc_1F1A(): pass

    label('loc_1F1A')

    ChrTalk(
        0x00FE,
        (
            '我先生诺曼\n',
            '已经好几天没从\n',
            '市长官邸回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，先生刚当上市长\n',
            '为什么就接二连三的出事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F7D(): pass

    label('loc_1F7D')

    Jump('loc_223E')

    def _loc_1F80(): pass

    label('loc_1F80')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_2055',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_1FF7',
    )

    ChrTalk(
        0x00FE,
        (
            '儿子贝尔夫好像去\n',
            '老公的事务所帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然不知道能持续到什么时候，\n',
            '现在也只能先观望观望了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2052')

    def _loc_1FF7(): pass

    label('loc_1FF7')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '儿子贝尔夫好像去\n',
            '老公的事务所帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明那么不愿意的……\n',
            '为什么又去做了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2052(): pass

    label('loc_2052')

    Jump('loc_223E')

    def _loc_2055(): pass

    label('loc_2055')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_209F',
    )

    ChrTalk(
        0x00FE,
        (
            '贝尔夫又\n',
            '去哪里了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像没回仓库，\n',
            '到底去哪儿了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_223E')

    def _loc_209F(): pass

    label('loc_209F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_2169',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Return,
        ),
        'loc_2109',
    )

    ChrTalk(
        0x00FE,
        (
            '无论如何，那孩子\n',
            '能回家真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然可能是暂时的,\n',
            '但待在家里就足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2166')

    def _loc_2109(): pass

    label('loc_2109')

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x00FE,
        (
            '无论如何，那孩子\n',
            '能回家真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '将来的事不必着急，\n',
            '花点时间慢慢考虑就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2166(): pass

    label('loc_2166')

    Jump('loc_223E')

    def _loc_2169(): pass

    label('loc_2169')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_223E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 0, 0x1210)),
            Expr.Return,
        ),
        'loc_21D0',
    )

    ChrTalk(
        0x00FE,
        (
            '老公要是能和那孩子\n',
            '谈谈心就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是现在选举活动那么忙\n',
            '连家也不能回啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_223E')

    def _loc_21D0(): pass

    label('loc_21D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0241, 7, 0x120F)),
            Expr.Return,
        ),
        'loc_21F9',
    )

    ChrTalk(
        0x00FE,
        (
            '贝尔夫在２楼。\n',
            '请上去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_223E')

    def _loc_21F9(): pass

    label('loc_21F9')

    ChrTalk(
        0x00FE,
        (
            '真是的……那孩子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '打算把自己关在房间里\n',
            '到什么时候啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_223E(): pass

    label('loc_223E')

    TalkEnd(0x0008)

    Return()

# id: 0x000D offset: 0x2242
@scena.Code('func_0D_2242')
def func_0D_2242():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 0, 0x1210)),
            Expr.Return,
        ),
        'loc_246D',
    )

    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_2308',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_22A9',
    )

    ChrTalk(
        0x00FE,
        (
            '这种时候，不得已也得\n',
            '去打工了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只是，在父亲的事务所\n',
            '工作啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2305')

    def _loc_22A9(): pass

    label('loc_22A9')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '去北街区\n',
            '找过工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过世间还真是残酷啊。\n',
            '工作只有选举运动\n',
            '的兼职什么的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2305(): pass

    label('loc_2305')

    Jump('loc_2467')

    def _loc_2308(): pass

    label('loc_2308')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_23F8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_237B',
    )

    ChrTalk(
        0x00FE,
        (
            '看来只好\n',
            '再去找找工作了吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，又在意伙伴们的目光，\n',
            '港口那边的工作还是避开吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23F5')

    def _loc_237B(): pass

    label('loc_237B')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '就这样关在家里\n',
            '也不是办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过伙伴们的仓库…\n',
            '事到如今也是回不去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，看来只好\n',
            '去找找工作了吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23F5(): pass

    label('loc_23F5')

    Jump('loc_2467')

    def _loc_23F8(): pass

    label('loc_23F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_2467',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_242D',
    )

    ChrTalk(
        0x00FE,
        (
            '………………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2467')

    def _loc_242D(): pass

    label('loc_242D')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '一直躲着\n',
            '父亲也不是办法啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我也明白……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2467(): pass

    label('loc_2467')

    TalkEnd(0x0009)

    Jump('loc_249F')

    def _loc_246D(): pass

    label('loc_246D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0241, 7, 0x120F)),
            Expr.Return,
        ),
        'loc_247B',
    )

    Call(0, 0x0011)

    Jump('loc_249F')

    def _loc_247B(): pass

    label('loc_247B')

    TalkBegin(0x0009)

    ChrTalk(
        0x00FE,
        (
            '嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……唉………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0009)

    def _loc_249F(): pass

    label('loc_249F')

    Return()

# id: 0x000E offset: 0x24A0
@scena.Code('func_0E_24A0')
def func_0E_24A0():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_24B1',
    )

    Call(0, 0x0012)

    def _loc_24B1(): pass

    label('loc_24B1')

    FadeOut(0, 0, -1)
    EventBegin(0x00)
    OP_4A(0x0008, 255)
    ChrSetPos(0x0101, -4580, 0, 62980, 360)
    ChrSetPos(0x00F7, -5200, 0, 62110, 360)
    ChrSetPos(0x0008, 2720, 0, 67920, 167)
    MapClearFlags(0x00000001)
    CameraMove(-5070, 0, 64220, 0)
    OP_67(0, 8900, -10000, 0)
    CameraSetDistance(2590, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010201201V#1015F#6P嗯……\n',
            '这里是贝尔夫的家吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_25B4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050201202V#051F市长官邸右侧旁\n',
            '就是这里了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25EC')

    def _loc_25B4(): pass

    label('loc_25B4')

    ChrTalk(
        0x0103,
        (
            '#0030201203V#020F说是市长官邸的右边，\n',
            '应该是了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25EC(): pass

    label('loc_25EC')

    @scena.Lambda('lambda_25F2')
    def lambda_25F2():
        CameraMove(210, 0, 64230, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_25F2)

    @scena.Lambda('lambda_260A')
    def lambda_260A():
        OP_67(0, 8900, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_260A)

    Sleep(1000)

    ChrClearFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0004)
    ChrWalkTo(0x0008, 3000, 0, 65200, 2000, 0x00)
    ChrClearFlags(0x0008, 0x0004)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0008, 256, 500)

    ChrTalk(
        0x0008,
        (
            '#2800201204V哎呀，欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0008, 500)
    ChrTurnDirection(0x00F7, 0x0008, 500)

    @scena.Lambda('lambda_26A3')
    def lambda_26A3():
        ChrWalkTo(0x00FE, -230, 0, 63820, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_26A3)

    Sleep(300)

    @scena.Lambda('lambda_26C3')
    def lambda_26C3():
        CameraMove(-1590, 0, 64160, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_26C3)

    @scena.Lambda('lambda_26DB')
    def lambda_26DB():
        OP_67(0, 8900, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_26DB)

    CreateThread(0x0101, 0x01, 0x00, func_0F_2DDD)
    Sleep(300)

    CreateThread(0x00F7, 0x01, 0x00, func_10_2E21)
    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x00F7, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0008,
        (
            '#2800201205V很不巧，我先生现在\n',
            '去酒店那边了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2800201206V能去那边找他吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201207V#1004F#5P咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_27EC',
    )

    ChrTalk(
        0x0106,
        (
            '#0050201208V#053F不，我们要找的\n',
            '不是您先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201209V#050F而是令郎贝尔夫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2842')

    def _loc_27EC(): pass

    label('loc_27EC')

    ChrTalk(
        0x0103,
        (
            '#0030201210V#026F不，我们要找的\n',
            '不是您先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201211V#020F而是令郎\n',
            '贝尔夫。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2842(): pass

    label('loc_2842')

    ChrTalk(
        0x0008,
        (
            '#2800201212V哎呀哎呀，是找贝尔夫啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2800201213V抱歉哦。\n',
            '我还以为一定是\n',
            '为选举的事来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201214V#1015F#5P选举……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201215V#1004F啊，难不成\n',
            '您先生是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2800201216V是的，我先生诺曼\n',
            '参加了市长选举。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2800201217V因此，把酒店最上层\n',
            '作为应对选举的总部使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2800201218V各位支持者好像就是\n',
            '在那里进行选举宣传活动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201219V#1011F#5P是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201220V那个，我们是\n',
            '游击士协会的人…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201221V有些事，想问问\n',
            '令郎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2800201222V游击士协会？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0008,
        (
            '#2800201223V那、那个，我家贝尔夫\n',
            '做了什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2B1B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050201224V#050F不，不是那样的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201225V听说令郎\n',
            '看到了奇怪的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201226V我们是来打听目击情报的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2B9E')

    def _loc_2B1B(): pass

    label('loc_2B1B')

    ChrTalk(
        0x0103,
        (
            '#0030201227V#020F不，请不必担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201228V其实听说贝尔夫\n',
            '看到了奇怪的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201229V我们只是来打听\n',
            '这个目击情报的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2B9E(): pass

    label('loc_2B9E')

    ChrTalk(
        0x0008,
        (
            '#2800201230V奇怪的东西……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201231V#1015F#5P您\n',
            '什么也没听说吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2800201232V是，不好意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2800201233V儿子好不容易\n',
            '回家来了，\n',
            '却不怎么说话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2800201234V先生又为了选举拼尽全力，\n',
            '也没和儿子好好谈谈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201235V#1025F#5P是、是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2D21',
    )

    ChrTalk(
        0x0106,
        (
            '#0050201236V#050F总之能让我们\n',
            '和贝尔夫谈谈吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201237V如果有烦恼\n',
            '或许能开导开导他呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2D82')

    def _loc_2D21(): pass

    label('loc_2D21')

    ChrTalk(
        0x0103,
        (
            '#0030201238V#020F总之，能让我们\n',
            '和令郎谈谈吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201239V如果有烦恼\n',
            '或许能开导开导他呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D82(): pass

    label('loc_2D82')

    ChrTalk(
        0x0008,
        (
            '#2800201240V这样啊……\n',
            '请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2800201241V贝尔夫在2楼。\n',
            '请上去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0241, 7, 0x120F))
    OP_4B(0x0008, 255)
    EventEnd(0x00)

    Return()

# id: 0x000F offset: 0x2DDD
@scena.Code('func_0F_2DDD')
def func_0F_2DDD():
    ChrWalkTo(0x0101, -4440, 0, 65280, 3000, 0x00)
    ChrWalkTo(0x0101, -2110, 0, 65430, 3000, 0x00)
    ChrWalkTo(0x0101, -1910, 0, 63470, 3000, 0x00)
    ChrTurnDirection(0x0101, 0x0008, 500)

    Return()

# id: 0x0010 offset: 0x2E21
@scena.Code('func_10_2E21')
def func_10_2E21():
    ChrWalkTo(0x00F7, -4440, 0, 65280, 3000, 0x00)
    ChrWalkTo(0x00F7, -2110, 0, 65430, 3000, 0x00)
    ChrWalkTo(0x00F7, -1770, 0, 64290, 3000, 0x00)
    ChrTurnDirection(0x00F7, 0x0008, 500)

    Return()

# id: 0x0011 offset: 0x2E65
@scena.Code('func_11_2E65')
def func_11_2E65():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2E76',
    )

    Call(0, 0x0012)

    def _loc_2E76(): pass

    label('loc_2E76')

    FadeIn(0, 0)
    EventBegin(0x00)
    OP_4A(0x0009, 255)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_2F69',
    )

    Fade(1000)
    ChrSetPos(0x0101, -29130, 0, 62760, 135)
    ChrSetPos(0x0106, -27990, 0, 62950, 180)

    ExecExpressionWithVar(
        0x65,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x9, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x66,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x9, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x67,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x9, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x66,
        (
            (Expr.PushLong, 0x1F4),
            Expr.Add2,
            Expr.Return,
        ),
    )

    OP_0D()

    NpcTalk(
        0x0009,
        '年轻人',
        (
            '#2810201242V嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0009,
        '年轻人',
        (
            '#2810201243V……唉………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201244V#1015F请问～打扰一下好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3046')

    def _loc_2F69(): pass

    label('loc_2F69')

    Fade(1000)
    ChrSetPos(0x0101, -27990, 0, 62950, 180)
    ChrSetPos(0x0103, -29130, 0, 62760, 135)

    ExecExpressionWithVar(
        0x65,
        (
            (Expr.GetChrWork, 0x103, 0x1),
            (Expr.GetChrWork, 0x9, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x66,
        (
            (Expr.GetChrWork, 0x103, 0x2),
            (Expr.GetChrWork, 0x9, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x67,
        (
            (Expr.GetChrWork, 0x103, 0x3),
            (Expr.GetChrWork, 0x9, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x66,
        (
            (Expr.PushLong, 0x1F4),
            Expr.Add2,
            Expr.Return,
        ),
    )

    OP_0D()

    NpcTalk(
        0x0009,
        '年轻人',
        (
            '#2810201242V嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0009,
        '年轻人',
        (
            '#2810201243V……唉………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201244V#1015F#2P请问～打扰一下好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3046(): pass

    label('loc_3046')

    NpcTalk(
        0x0009,
        '年轻人',
        (
            '#2810201248V我到底在干什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0009,
        '年轻人',
        (
            '#2810201249V因为老爸不在家\n',
            '才安心回来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0009,
        '年轻人',
        (
            '#2810201250V……真丢脸……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3F2F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050201251V#551F#2P说你呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201252V我们在跟你说话呢，\n',
            '你也回个头啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0009,
        '年轻人',
        (
            '#2810201253V啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0106, 400)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_3182')
    def lambda_3182():
        ChrMoveToRelativeAsync(0x0009, 0, 0, -500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3182)

    WaitForThreadExit(0x0009, 0x0001)

    NpcTalk(
        0x0009,
        '年轻人',
        (
            '#2810201254V呜哇哇哇！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0009,
        '年轻人',
        (
            '#2810201255V#6P你、你们是谁！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050201256V#050F#2P你是贝尔夫吧。\n',
            '忘了我的脸了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201257V#6P……咦…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0009,
        (
            '#2810201258V#6P啊啊，阿加特先生！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201259V#6P为、为什么会在我家！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050201260V#051F#2P有点事想问你。\n',
            '你母亲就让我们上来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201261V现在有时间吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201262V#6P有、有……\n',
            '倒是没什么事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_335A')
    def lambda_335A():
        ChrMoveToRelativeAsync(0x0009, 0, 0, 350, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_335A)

    WaitForThreadExit(0x0009, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#2810201263V……那个，要问什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201264V#1011F其实是，听说你看见\n',
            '『白影』了对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201265V能不能详细\n',
            '说说呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#2810201266V这、这件事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201267V说实话，我不太\n',
            '想说啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201268V一说就会想起来的，\n',
            '然后又被吓到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0106,
        (
            '#0050201269V#057F#2P你说什么!',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#2810201270V我，我说！\n',
            '说就是了嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010201271V#1019F我说阿加特。\n',
            '别威胁他嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050201272V#053F#2P痛快点说出来不是更好吗～？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201273V#050F喂，还不快说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0009,
        (
            '#2810201274V呼……真受不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201275V一周前我一直\n',
            '都待在组织的大本营，\n',
            '也就是那个仓库里生活的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201276V这个家，只是为了\n',
            '吃饭才偶尔回来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201277V其他时间和伙伴们一起\n',
            '在那里暂住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201278V#1007F真、真难理解啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201279V难得这么舒服的家，\n',
            '为什么不愿意回来呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010201280V#1006F阿加特以前也\n',
            '过着一样的生活吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050201281V#552F#2P……啰嗦。\n',
            '别转移话题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201282V#050F然后呢，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0009,
        (
            '#2810201283V一周前的夜晚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201284V我和平时一样，和伙伴们\n',
            '喝醉了睡在仓库时，\n',
            '偶然醒来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201285V打算吹吹夜风来到了仓库外\n',
            '……就看见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201286V#1020F看见……\n',
            '是，是那个『白影』？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201287V啊啊…\n',
            '浮在天上的『白影』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201288V裹着斗篷一样的\n',
            '古老服装……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201289V像跳舞一样在空中飞舞着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010201290V#1016F啊、啊哈哈……\n',
            '相当具体啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050201291V#050F#2P既然喝醉了，\n',
            '那喝多了眼花的可能性呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201292V不，不会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201293V我一下子就清醒了，\n',
            '想叫喊但是喊不出声……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201294V幽灵向东北方飞走之后，\n',
            '我才返回仓库大声把其他人\n',
            '叫醒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201295V因此还被洛克\n',
            '打了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050201296V#053F#2P哼，原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201297V#050F说是晚上，\n',
            '知道大致是几点钟吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201298V这个啊……\n',
            '半夜两点左右吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201299V……啊啊真是的。\n',
            '完全想起来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201300V明明特地跑回家\n',
            '就是不想想起来的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201301V#1007F这、这就是\n',
            '回家的理由啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201302V#1019F确实如此，不想住在看到过幽灵的地方\n',
            '是可以理解的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050201303V#552F#2P哼，还当什么不良少年。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201304V离开渡鸦帮，\n',
            '就这样待在家里对你比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#2810201305V呜呜……\n',
            '我知道啊，我不适合当不良少年。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201306V但是我无论如何\n',
            '都不想见到父亲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201307V现在父亲因为选举活动\n',
            '在宾馆暂住，\n',
            '我才能回家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201308V如果选举结束了，\n',
            '就又要再看到他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201309V如果当了市长，\n',
            '那就会更加严格了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201310V#1015F嗯～说到底，\n',
            '就是逃避自己不喜欢的事而已啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201311V呜呜呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050201312V#050F#2P哼，看来\n',
            '对自己还有所有认识的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201313V#053F那就不要依靠任何人\n',
            '自己找到答案吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050201314V我们会这样\n',
            '对你母亲说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201315V阿、阿加特先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050201316V#053F#2P这里的事办完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)
    Sleep(500)

    ChrTalk(
        0x0106,
        (
            '#0050201317V#051F#2P艾丝蒂尔，去下一站吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 82, 400)

    ChrTalk(
        0x0101,
        (
            '#0010201318V#1006F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#0010201319V#1001F贝尔夫。\n',
            '谢谢你提供情报哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201320V……啊啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4FD7')

    def _loc_3F2F(): pass

    label('loc_3F2F')

    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010201321V#1019F#2P真是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201322V人跟你说话呢，\n',
            '也朝这边看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0009,
        '年轻人',
        (
            '#2810201253V啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_3FF5')
    def lambda_3FF5():
        ChrMoveToRelativeAsync(0x0009, 0, 0, -500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3FF5)

    WaitForThreadExit(0x0009, 0x0001)

    NpcTalk(
        0x0009,
        '年轻人',
        (
            '#2810201254V#6P呜哇哇哇！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0009,
        '年轻人',
        (
            '#2810201255V#6P你、你们是谁！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201326V#1011F#2P终于有反应了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201327V嗯，你就是贝尔夫？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201328V#6P啊啊……是我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#2810201329V#6P对了，你。\n',
            '是参加过武术大会的游击士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201330V#1006F#2P艾丝蒂尔·布莱特啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201331V这位是我的前辈，\n',
            '雪拉扎德·哈维。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030201332V#021F呵呵，请多关照。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201333V#6P是、是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_41CA')
    def lambda_41CA():
        ChrMoveToRelativeAsync(0x0009, 0, 0, 350, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_41CA)

    WaitForThreadExit(0x0009, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#2810201334V那到底有什么事啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201264V#1011F#2P其实是，听说你看见\n',
            '『白影』了对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201265V能不能详细\n',
            '说说呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#2810201266V这、这件事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201267V说实话，我不太\n',
            '想说啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201268V一说就会想起来的，\n',
            '然后又被吓到……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010201340V#1020F#2P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201341V那、那么恐怖的事啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030201342V#021F好了好了。\n',
            '别这么说啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201343V难道不能告诉\n',
            '姐姐吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0103, 400)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#2810201344V咦，但是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030201345V#027F呵呵，只要你告诉我们\n',
            '说不定可以给你一些好处哟㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#2810201346V唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010201347V#1019F#2P我说雪拉姐……\n',
            '不要诱惑他啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0103, 82, 400)

    ChrTalk(
        0x0103,
        (
            '#0030201348V#021F别这么死板嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0009, 400)

    ChrTalk(
        0x0103,
        (
            '#0030201349V#027F那么……\n',
            '你打算说了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)
    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0009,
        (
            '#2810201274V呼……真受不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201351V一周前我一直\n',
            '都待在组织的大本营里，\n',
            '也就是说在那个仓库里生活着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201276V这个家，只是为了\n',
            '吃饭才偶尔回来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201353V其他时间和伙伴们一起\n',
            '在那里暂住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201278V#1007F#2P真、真难理解啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201279V难得这么舒服的家，\n',
            '为什么不愿意回来呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030201356V#021F呵呵。\n',
            '年轻人就是这样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201357V#027F那么，之后呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201283V一周前的夜晚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201284V我和平时一样，和伙伴们\n',
            '喝醉了在仓库里睡觉时，\n',
            '偶然醒来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201360V打算到仓库外吹吹夜风的，\n',
            '……就看见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201286V#1020F#2P看见……\n',
            '是，是那个『白影』？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201287V啊啊…\n',
            '浮在天上的『白影』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201288V裹着斗篷一样的\n',
            '古老服装……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201289V像跳舞一样在空中飞舞着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010201290V#1016F#2P啊，啊哈哈……\n',
            '相当具体啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030201366V#020F既然喝醉了，\n',
            '那喝多了眼花的可能性呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201367V不，不会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201368V我一下子就清醒了，\n',
            '想叫喊但是喊不出声……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201369V幽灵向东北方飞走之后，\n',
            '我才返回仓库大声把其他人\n',
            '叫醒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201370V因此还被洛克\n',
            '打了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030201371V#026F唔，原来如此啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201372V#020F说是晚上，\n',
            '知道具体是几点钟吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201373V是啊……\n',
            '半夜两点左右吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201299V……啊啊真是的。\n',
            '完全想起来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201300V明明特地跑回家\n',
            '就是不想想起来的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201301V#1007F#2P这、这就是\n',
            '回家的理由啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010201302V#1019F确实如此，不想住在看到过幽灵的地方，\n',
            '这是可以理解的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030201378V#027F呵呵，这不是深切地\n',
            '感受到家的温暖了嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201379V以此为机会，别再当什么\n',
            '不良少年不就好了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#2810201380V呜呜……\n',
            '我知道啊，我不适合当不良少年。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201306V但是我无论如何\n',
            '都不想见到父亲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201382V现在父亲因为选举活动\n',
            '在酒店暂住\n',
            '我才能回家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201308V如果选举结束了，\n',
            '就又要再看到他……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201309V如果当了市长\n',
            '那就会更加严格了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201310V#1015F#2P嗯～说到底，\n',
            '就是逃避自己不喜欢的事而已啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201311V呜呜呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030201387V#021F好了好了，打起精神来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0103, 0x0040)
    ChrMoveTo(0x0103, -28420, 0, 61690, 1000, 0x00)
    Sleep(500)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '雪拉扎德\n',
            '在贝尔夫脸颊上吻了一下。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#2810201388V呜哇啊！',
            TxtCtl.Enter,
        ),
    )

    ChrJumpTo(0x0009, -27900, 0, 61110, 500, 5000)
    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrMoveTo(0x0103, -28880, 0, 62510, 1200, 0x00)
    ChrClearFlags(0x0103, 0x0040)
    ChrTurnDirection(0x0009, 0x0103, 800)
    ChrTurnDirection(0x0101, 0x0103, 500)

    ChrTalk(
        0x0101,
        (
            '#0010201389V#1013F#2P我、我说雪拉姐！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030201390V#021F呵呵，这是提供情报的\n',
            '感谢兼鼓励哟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201391V#027F之后你自己思考\n',
            '找出答案就好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030201392V你的事只有你自己\n',
            '才能找到答案。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2810201393V姐，姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030201394V#026F那么……\n',
            '这里就这样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0103, 82, 400)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030201395V#020F艾丝蒂尔，去下一站吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010201396V#1007F#2P唉……真服了雪拉姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010201397V#1008F#2P贝尔夫。\n',
            '谢谢你提供情报哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#2810201398V噢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4FD7(): pass

    label('loc_4FD7')

    SetScenaFlags(ScenaFlag(0x0242, 0, 0x1210))
    OP_28(0x0082, 0x02, 0x0020)
    OP_28(0x0082, 0x01, 0x0040)
    OP_4B(0x0009, 255)
    ChrClearFlags(0x0009, 0x0010)
    EventEnd(0x00)

    Return()

# id: 0x0012 offset: 0x4FF2
@scena.Code('func_12_4FF2')
def func_12_4FF2():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
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
        (0x00000000, 'loc_506C'),
        (0x00000001, 'loc_5072'),
        (-1, 'loc_5078'),
    )

    def _loc_506C(): pass

    label('loc_506C')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_5078')

    def _loc_5072(): pass

    label('loc_5072')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_5078')

    def _loc_5078(): pass

    label('loc_5078')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_5086',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_508A')

    def _loc_5086(): pass

    label('loc_5086')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_508A(): pass

    label('loc_508A')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
