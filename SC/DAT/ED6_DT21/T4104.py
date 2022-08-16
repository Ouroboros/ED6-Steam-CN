import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4104_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4104   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4104.x'
    header.mapIndex       = 1
    header.bgm            = 81
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
        ('ED6_DT09/CH10840._CH', 'ED6_DT09/CH10840P._CP'),
        ('ED6_DT09/CH10841._CH', 'ED6_DT09/CH10841P._CP'),
        ('ED6_DT29/CH12460._CH', 'ED6_DT29/CH12460P._CP'),
        ('ED6_DT29/CH12461._CH', 'ED6_DT29/CH12461P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
    ]

# id: 0x10001 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '寒冰至尊',
            x                   = 960,
            z                   = 0,
            y                   = 10300,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '寒冰碎片',
            x                   = 1960,
            z                   = 0,
            y                   = 8260,
            direction           = 180,
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
            name                = '寒冰碎片',
            x                   = -600,
            z                   = 0,
            y                   = 8260,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x14A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x14A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x14A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x14A
@scena.Code('Init')
def Init():
    Event(0, func_03_2F7)

    Return()

# id: 0x0001 offset: 0x14F
@scena.Code('func_01_14F')
def func_01_14F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_16B',
    )

    OP_B1('t4104_y')

    Jump('loc_174')

    def _loc_16B(): pass

    label('loc_16B')

    OP_B1('t4104_n')

    def _loc_174(): pass

    label('loc_174')

    OP_71(0x0007, 0x0004)

    Return()

# id: 0x0002 offset: 0x17A
@scena.Code('func_02_17A')
def func_02_17A():
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
        'loc_19F',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_2E1')

    def _loc_19F(): pass

    label('loc_19F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B8',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_2E1')

    def _loc_1B8(): pass

    label('loc_1B8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D1',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_2E1')

    def _loc_1D1(): pass

    label('loc_1D1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1EA',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_2E1')

    def _loc_1EA(): pass

    label('loc_1EA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_203',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_2E1')

    def _loc_203(): pass

    label('loc_203')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_21C',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_2E1')

    def _loc_21C(): pass

    label('loc_21C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_235',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_2E1')

    def _loc_235(): pass

    label('loc_235')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24E',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_2E1')

    def _loc_24E(): pass

    label('loc_24E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_267',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_2E1')

    def _loc_267(): pass

    label('loc_267')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_280',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_2E1')

    def _loc_280(): pass

    label('loc_280')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_299',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_2E1')

    def _loc_299(): pass

    label('loc_299')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B2',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_2E1')

    def _loc_2B2(): pass

    label('loc_2B2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2CB',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_2E1')

    def _loc_2CB(): pass

    label('loc_2CB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E1',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_2E1(): pass

    label('loc_2E1')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2F6',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_2E1')

    def _loc_2F6(): pass

    label('loc_2F6')

    Return()

# id: 0x0003 offset: 0x2F7
@scena.Code('func_03_2F7')
def func_03_2F7():
    EventBegin(0x00)
    CameraMove(1520, 0, 1520, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(4400, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    OP_6F(0x0000, 0)
    OP_72(0x0000, 0x0010)
    OP_6F(0x0001, 0)
    OP_72(0x0001, 0x0010)
    ChrSetPos(0x0101, 440, 0, -25960, 0)
    ChrSetPos(0x0105, 2060, 0, -26560, 0)
    ChrSetPos(0x0104, -520, 0, -27220, 0)
    ChrSetPos(0x0108, 1280, 0, -27820, 0)

    @scena.Lambda('lambda_0398')
    def lambda_0398():
        CameraMove(1520, 0, -18920, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0398)

    Sleep(500)

    OP_70(0x0000, 100)
    CreateThread(0x0101, 0x01, 0x00, func_04_BBE)
    Sleep(100)

    CreateThread(0x0105, 0x01, 0x00, func_05_BF7)
    Sleep(100)

    CreateThread(0x0104, 0x01, 0x00, func_06_C30)
    Sleep(100)

    CreateThread(0x0108, 0x01, 0x00, func_07_C5D)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(1000)

    Fade(500)
    CameraMove(1280, 0, -12260, 0)
    OP_67(0, 6900, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    WaitForThreadExit(0x0108, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010460372V#1000F格兰竞技场……\n',
            '感觉好怀念。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080460373V#070F啊，明明没过多久，\n',
            '真不可思议。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040460374V#035F呼，只要站在这里，\n',
            '就好像还能听见那时的欢呼声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_04E7')
    def lambda_04E7():
        ChrSetDirection(0x0101, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_04E7)

    Sleep(50)

    @scena.Lambda('lambda_04FA')
    def lambda_04FA():
        ChrSetDirection(0x0105, 270, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_04FA)

    Sleep(50)

    @scena.Lambda('lambda_050D')
    def lambda_050D():
        ChrSetDirection(0x0104, 45, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_050D)

    Sleep(50)

    @scena.Lambda('lambda_0520')
    def lambda_0520():
        ChrSetDirection(0x0108, 0, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0520)

    WaitForThreadExit(0x0108, 0x0001)

    ChrTalk(
        0x0105,
        (
            '#0060460375V#040F我记得艾丝蒂尔你们\n',
            '在获得武术大会冠军后\n',
            '被邀请进入城堡了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060460376V#041F呵呵，我也很想观战啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460377V#1016F哈哈，现在想想\n',
            '我那时还很不成熟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460378V#1006F不过等这回的骚乱平息之后，\n',
            '我想再次参加明年的武术大会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460379V这也是为了测试自己的实力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080460380V#071F哈哈，这才是大人的女儿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080460381V#070F是啊……\n',
            '到时候让我也参战吧',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460382V#1016F金、金先生做我对手的话\n',
            '我实在没取胜的信心……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040460383V#031F呵呵，那我就在观众席\n',
            '唱歌来\n',
            '支持艾丝蒂尔吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040460384V#030F用我充满爱意和力量的歌声…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460385V#1019F……你的好意\n',
            '我就心领了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060460386V#041F呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_70(0x0001, 100)
    Sleep(200)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0108, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(200)

    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrSetChipByIndex(0x0008, 1)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0009, 3)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x000A, 3)
    ChrSetSubChip(0x000A, 0)

    @scena.Lambda('lambda_0866')
    def lambda_0866():
        ChrMoveTo(0x00FE, 960, 0, -1160, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0866)

    @scena.Lambda('lambda_0881')
    def lambda_0881():
        ChrMoveTo(0x00FE, 1960, 0, -3120, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0881)

    @scena.Lambda('lambda_089C')
    def lambda_089C():
        ChrMoveTo(0x00FE, -600, 0, -3120, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_089C)

    @scena.Lambda('lambda_08B7')
    def lambda_08B7():
        CameraMove(1880, 0, 5500, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_08B7)

    @scena.Lambda('lambda_08CF')
    def lambda_08CF():
        OP_67(0, 5420, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_08CF)

    @scena.Lambda('lambda_08E7')
    def lambda_08E7():
        CameraSetDistance(3200, 2000)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_08E7)

    @scena.Lambda('lambda_08F7')
    def lambda_08F7():
        OP_6C(45000, 2000)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_08F7)

    @scena.Lambda('lambda_0907')
    def lambda_0907():
        ChrSetDirection(0x0101, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0907)

    Sleep(50)

    @scena.Lambda('lambda_091A')
    def lambda_091A():
        ChrSetDirection(0x0105, 0, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_091A)

    Sleep(50)

    @scena.Lambda('lambda_092D')
    def lambda_092D():
        ChrSetDirection(0x0104, 0, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_092D)

    WaitForThreadExit(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 4)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0104, 5)
    ChrSetSubChip(0x0104, 0)
    ChrSetChipByIndex(0x0105, 6)
    ChrSetSubChip(0x0105, 0)
    ChrSetChipByIndex(0x0108, 7)
    ChrSetSubChip(0x0108, 0)
    ChrSetPos(0x0101, 320, 0, -8590, 0)
    ChrSetPos(0x0105, 1670, 0, -9190, 0)
    ChrSetPos(0x0104, -430, 0, -10240, 0)
    ChrSetPos(0x0108, 920, 0, -10990, 0)

    @scena.Lambda('lambda_09AC')
    def lambda_09AC():
        CameraMove(1620, 0, -5360, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_09AC)

    @scena.Lambda('lambda_09C4')
    def lambda_09C4():
        CameraSetDistance(3400, 4000)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_09C4)

    WaitForThreadExit(0x0101, 0x0002)
    Fade(250)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0009, 2)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x000A, 2)
    ChrSetSubChip(0x000A, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010460387V#1004F魔、魔兽！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080460388V#072F好像是要模仿古代\n',
            '竞技场呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040460389V#035F呵呵，这舞台令人满意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040460390V#030F不过没有观战的客人，\n',
            '真是有点遗憾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060460391V#046F……敌人来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0008, 1)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0009, 3)
    ChrSetSubChip(0x0009, 0)
    ChrSetChipByIndex(0x000A, 3)
    ChrSetSubChip(0x000A, 0)
    CreateThread(0x0008, 0x00, 0x00, func_08_C96)

    @scena.Lambda('lambda_0B04')
    def lambda_0B04():
        ChrMoveTo(0x00FE, 960, 0, -11160, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0B04)

    @scena.Lambda('lambda_0B1F')
    def lambda_0B1F():
        ChrMoveTo(0x00FE, 1960, 0, -13120, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0B1F)

    @scena.Lambda('lambda_0B3A')
    def lambda_0B3A():
        ChrMoveTo(0x00FE, -600, 0, -13120, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0B3A)

    @scena.Lambda('lambda_0B55')
    def lambda_0B55():
        CameraSetDistance(2600, 500)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_0B55)

    Sleep(400)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0104, 0xFF)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B94',
    )

    Battle(0x00000CEA, 0x00000000, 0x00, 0x0000, 0xFF)

    Jump('loc_BA1')

    def _loc_B94(): pass

    label('loc_B94')

    Battle(0x00000CE9, 0x00000000, 0x00, 0x0000, 0xFF)

    def _loc_BA1(): pass

    label('loc_BA1')

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_BB1'),
        (0x00000000, 'loc_BB6'),
        (-1, 'loc_BBD'),
    )

    def _loc_BB1(): pass

    label('loc_BB1')

    OP_B4(0x00)

    Jump('loc_BBD')

    def _loc_BB6(): pass

    label('loc_BB6')

    Call(0, 0x0009)

    Jump('loc_BBD')

    def _loc_BBD(): pass

    label('loc_BBD')

    Return()

# id: 0x0004 offset: 0xBBE
@scena.Code('func_04_BBE')
def func_04_BBE():
    ChrWalkTo(0x0101, 440, 0, -10960, 2000, 0x00)
    Sleep(200)

    ChrSetDirection(0x00FE, 270, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 360, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 315, 400)

    Return()

# id: 0x0005 offset: 0xBF7
@scena.Code('func_05_BF7')
def func_05_BF7():
    ChrWalkTo(0x0105, 2060, 0, -11560, 2000, 0x00)
    Sleep(200)

    ChrSetDirection(0x00FE, 45, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 135, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0006 offset: 0xC30
@scena.Code('func_06_C30')
def func_06_C30():
    ChrWalkTo(0x0104, -520, 0, -12220, 2000, 0x00)
    Sleep(200)

    ChrSetDirection(0x00FE, 225, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0007 offset: 0xC5D
@scena.Code('func_07_C5D')
def func_07_C5D():
    ChrWalkTo(0x0108, 1280, 0, -12820, 2000, 0x00)
    Sleep(200)

    ChrSetDirection(0x00FE, 45, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 90, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 45, 400)

    Return()

# id: 0x0008 offset: 0xC96
@scena.Code('func_08_C96')
def func_08_C96():
    ChrSetDirection(0x00FE, 90, 1000)
    ChrSetDirection(0x00FE, 0, 1000)
    ChrSetDirection(0x00FE, 270, 1000)
    ChrSetDirection(0x00FE, 180, 1000)
    ChrSetDirection(0x00FE, 90, 1000)
    ChrSetDirection(0x00FE, 0, 1000)
    ChrSetDirection(0x00FE, 270, 1000)
    ChrSetDirection(0x00FE, 180, 1000)
    ChrSetDirection(0x00FE, 90, 1000)
    ChrSetDirection(0x00FE, 0, 1000)
    ChrSetDirection(0x00FE, 270, 1000)
    ChrSetDirection(0x00FE, 180, 1000)
    ChrSetDirection(0x00FE, 90, 1000)
    ChrSetDirection(0x00FE, 0, 1000)
    ChrSetDirection(0x00FE, 270, 1000)
    ChrSetDirection(0x00FE, 180, 1000)

    Return()

# id: 0x0009 offset: 0xD07
@scena.Code('func_09_D07')
def func_09_D07():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    LoadEffect(0x00, 'craft\\\\cr162_02.eff')
    CameraMove(1620, 0, -5360, 0)
    OP_67(0, 5420, -10000, 0)
    CameraSetDistance(3400, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetChipByIndex(0x0101, 4)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0104, 5)
    ChrSetSubChip(0x0104, 0)
    ChrSetChipByIndex(0x0105, 6)
    ChrSetSubChip(0x0105, 0)
    ChrSetChipByIndex(0x0108, 7)
    ChrSetSubChip(0x0108, 0)
    ChrSetPos(0x0101, 320, 0, -8590, 0)
    ChrSetPos(0x0105, 1670, 0, -9190, 0)
    ChrSetPos(0x0104, -430, 0, -10240, 0)
    ChrSetPos(0x0108, 920, 0, -10990, 0)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    PlayEffect(0x00, 0x01, 0x00FF, 720, 0, -3320, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_72(0x0007, 0x0004)

    ChrTalk(
        0x0101,
        (
            '#0010460392V#1004F哇哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0105, 65535)
    ChrSetChipByIndex(0x0104, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010460393V#1019F什、什么啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060460394V#044F看上去像是魔术……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040460395V#030F呵呵，水平\n',
            '不是还不错吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040460396V#035F确实有实力当我的\n',
            '候补对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080460397V#075F唉，比我想象的\n',
            '要有性格……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080460398V#070F好了，赶快看一下\n',
            '里面的内容吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010250129V#1000F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0FA2')
    def lambda_0FA2():
        CameraSetDistance(2700, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0FA2)

    @scena.Lambda('lambda_0FB2')
    def lambda_0FB2():
        ChrWalkTo(0x00FE, 520, 0, -4340, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0FB2)

    Sleep(400)

    @scena.Lambda('lambda_0FD2')
    def lambda_0FD2():
        ChrMoveToRelative(0x00FE, -200, 0, 2500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_0FD2)

    Sleep(50)

    @scena.Lambda('lambda_0FF2')
    def lambda_0FF2():
        ChrMoveToRelative(0x00FE, -200, 0, 2500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_0FF2)

    Sleep(50)

    @scena.Lambda('lambda_1012')
    def lambda_1012():
        ChrMoveToRelative(0x00FE, -200, 0, 2500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1012)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(400)

    OP_70(0x0007, 60)
    PlaySE(43, 0x00, 0x64)
    OP_73(0x0007)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#16I埃尔赛尤的照片',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '箱子底部\n',
            '贴着一张卡片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_59()
    OP_AD('ED6_DT24/C_VIS124._CH', 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 300, -1, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0170460400V　　　　我的公主和劲敌，\n',
            '　　还有勇敢的诸位游击士啊。　　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170460401V　　对我精心装备的招待\n',
            '　　　 你们可满意否？ 　　　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170460402V　　我不想伤害主角的心情，\n',
            '所以就让我这个配角退席吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170460403V敬请期待来日的重逢。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010460404V#1009F真是的，什么来日的重逢啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460405V真希望他能够适可而止。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060460406V#042F不过他写的东西\n',
            '挺令人在意的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060460407V主角和配角什么的\n',
            '究竟是指？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460408V#1015F被你这么一说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460409V#1000F好了，总之先把这张照片\n',
            '送回资料馆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T4135._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
