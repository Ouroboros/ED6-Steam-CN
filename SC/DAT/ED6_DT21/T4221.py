import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4221_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4221   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4221.x'
    header.mapIndex       = 1
    header.bgm            = 17
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
        ('ED6_DT26/CH20260._CH', 'ED6_DT26/CH20260P._CP'),
        ('ED6_DT26/CH20234._CH', 'ED6_DT26/CH20234P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT26/CH20261._CH', 'ED6_DT26/CH20261P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
    ]

# id: 0x10001 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '雷沃尔',
            x                   = 143260,
            z                   = 0,
            y                   = 3310,
            direction           = 356,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            name                = '雪拉扎德',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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

# id: 0x10002 offset: 0x112
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x112
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x112
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x112
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 2, 0x1002)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_11E',
    )

    Event(0, func_03_358)

    def _loc_11E(): pass

    label('loc_11E')

    Return()

# id: 0x0001 offset: 0x11F
@scena.Code('func_01_11F')
def func_01_11F():
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
        'loc_13B',
    )

    OP_B1('t4221_y')

    Jump('loc_144')

    def _loc_13B(): pass

    label('loc_13B')

    OP_B1('t4221_n')

    def _loc_144(): pass

    label('loc_144')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 2, 0x1002)),
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 4, 0x1004)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_159',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_159(): pass

    label('loc_159')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_181',
    )

    PlaySE(135, 0x01, 0x1E)
    PlaySE(174, 0x01, 0x1E)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x2E),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x02000000)
    OP_77(0xFF, 0xBF, 0xB7, 0x00, 0x00000000)

    def _loc_181(): pass

    label('loc_181')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 6, 0x203E)),
            Expr.Return,
        ),
        'loc_19C',
    )

    OP_1B(0x01, 0x00, 0x0004)
    OP_1B(0x02, 0x00, 0x0004)
    OP_1B(0x03, 0x00, 0x0005)
    OP_1B(0x04, 0x00, 0x0005)

    def _loc_19C(): pass

    label('loc_19C')

    Return()

# id: 0x0002 offset: 0x19D
@scena.Code('func_02_19D')
def func_02_19D():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_1F3',
    )

    ChrTalk(
        0x00FE,
        (
            '好、好像从门外传来了\n',
            '悲鸣和愤怒的声音……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到、到底发生了什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_354')

    def _loc_1F3(): pass

    label('loc_1F3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_260',
    )

    ChrTalk(
        0x00FE,
        (
            '科洛蒂娅殿下看来\n',
            '要在城堡里逗留一阵子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有她在的话\n',
            '城堡里的气氛就会很活跃，\n',
            '真令人高兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_354')

    def _loc_260(): pass

    label('loc_260')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_301',
    )

    ChrTalk(
        0x00FE,
        (
            '凯诺娜小姐被捕了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样一来情报部的余党\n',
            '就被一网打尽了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也能稍稍减轻尤莉亚\n',
            '小姐肩上的负担吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最后果然还是\n',
            '正义取得了胜利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_354')

    def _loc_301(): pass

    label('loc_301')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_354',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，科洛蒂娅殿下，\n',
            '您回来啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '有何吩咐？\n',
            '要不要我来准备一些饮品？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_354(): pass

    label('loc_354')

    TalkEnd(0x00FE)

    Return()

# id: 0x0003 offset: 0x358
@scena.Code('func_03_358')
def func_03_358():
    AddCraft(ChrTable['艾丝蒂尔'], 0x0000)
    OP_BB(0x00, 0x06, 0x000000E7)
    ChrSetStatus(ChrTable['艾丝蒂尔'], 0xFE, 0)
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetSubChip(0x0101, 0)
    ChrSetFlags(0x0101, 0x0004)
    ChrClearFlags(0x0101, 0x0001)
    CameraMove(79650, 350, 55020, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 85060, 500, 60710, 180)
    OP_72(0x0005, 0x0004)
    OP_72(0x0005, 0x0020)
    OP_72(0x0005, 0x0008)
    OP_6F(0x0005, 5)
    OP_71(0x0006, 0x0004)
    OP_71(0x0007, 0x0004)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_040F')
    def lambda_040F():
        CameraMove(85310, 350, 60680, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_040F)

    @scena.Lambda('lambda_0427')
    def lambda_0427():
        OP_67(0, 8000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0427)

    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    NpcTalk(
        0x0101,
        '艾丝蒂尔',
        (
            '#0010190001V#007F……唔～……好刺眼…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 16)
    Sleep(200)

    ChrSetSubChip(0x0101, 0)
    Sleep(200)

    ChrSetSubChip(0x0101, 16)
    Sleep(200)

    ChrSetSubChip(0x0101, 0)
    Sleep(1000)

    @scena.Lambda('lambda_04B1')
    def lambda_04B1():
        OP_99(0x0101, 0x00, 0x08, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_04B1)

    Sleep(300)

    OP_71(0x0005, 0x0008)
    OP_6F(0x0005, 5)
    OP_B0(0x0005, 0x28)
    OP_70(0x0005, 59)
    Sleep(1500)

    @scena.Lambda('lambda_04E2')
    def lambda_04E2():
        OP_99(0x00FE, 0x08, 0x0C, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_04E2)

    ChrTalk(
        0x0101,
        (
            '#0010190002V#504F嘿～～～～～……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0101, 15, 0, 2000, 4000)

    @scena.Lambda('lambda_052C')
    def lambda_052C():
        OP_99(0x00FE, 0x0C, 0x0E, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_052C)

    Sleep(1000)

    ChrSetSubChip(0x0101, 14)
    Sleep(200)

    ChrSetSubChip(0x0101, 17)
    Sleep(200)

    ChrSetSubChip(0x0101, 18)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010190003V#501F嗯～～睡得真香呢～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0101, 0x12, 0x15, 1000)
    Sleep(500)

    OP_99(0x0101, 0x15, 0x12, 1000)
    ChrSetSubChip(0x0101, 23)
    Sleep(1000)

    ChrSetSubChip(0x0101, 18)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010190004V#004F咦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190005V……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190006V#505F对了，我们\n',
            '昨天留宿在王都里面了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190007V和约修亚一起逛了庆典……\n',
            '回来途中吃了冰淇淋……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190008V晚上和老爸一起参加晚餐会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190009V……然后………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    OP_AD('ED6_DT24/C_VIS160._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1500)

    OP_AE(0x000001F4)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010190010V#580F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190011V……不………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrClearFlags(0x0101, 0x0002)
    ChrSetSubChip(0x0101, 0)
    Sleep(100)

    PlaySE(571, 0x00, 0x3C)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetDirection(0x0101, 270, 0)

    @scena.Lambda('lambda_0760')
    def lambda_0760():
        ChrJumpTo(0x00FE, 83500, 0, 60660, 600, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0760)

    WaitForThreadExit(0x0101, 0x0001)
    ChrClearFlags(0x0101, 0x0004)
    ChrSetFlags(0x0101, 0x0001)

    @scena.Lambda('lambda_078D')
    def lambda_078D():
        CameraMove(83470, 0, 60260, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_078D)

    @scena.Lambda('lambda_07A5')
    def lambda_07A5():
        OP_67(0, 8000, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_07A5)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    ChrSetDirection(0x0101, 180, 1000)
    Sleep(1000)

    ChrSetDirection(0x0101, 90, 1000)
    Sleep(1000)

    ChrSetDirection(0x0101, 270, 1000)
    Sleep(1000)

    ChrSetDirection(0x0101, 180, 1000)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010190012V#587F这是……\n',
            '约修亚和老爸的房间……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190013V我应该……\n',
            '是和雪拉姐睡一个房间的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190014V那个……\n',
            '……我是什么时候开始睡着的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Sleep(100)

    Fade(500)
    ChrSetFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 1)
    ChrSetSubChip(0x0101, 5)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010190015V#580F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190016V………………………………\n',
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010190017V#005F#4S约修亚！！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    Fade(500)
    ChrClearFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    OP_0D()

    @scena.Lambda('lambda_097D')
    def lambda_097D():
        ChrWalkTo(0x0101, 79790, 0, 48550, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_097D)

    Sleep(100)

    @scena.Lambda('lambda_099D')
    def lambda_099D():
        CameraMove(80350, 0, 51510, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_099D)

    @scena.Lambda('lambda_09B5')
    def lambda_09B5():
        OP_67(0, 8000, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_09B5)

    Sleep(1500)

    @scena.Lambda('lambda_09D2')
    def lambda_09D2():
        ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 250)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_09D2)

    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    MapClearFlags(0x00000001)
    Fade(1000)
    CameraMove(79000, 0, 7200, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 255, 0)
    ChrSetPos(0x0101, 79210, 0, 9810, 180)
    ChrSetPos(0x0009, 67190, 0, 9780, 180)
    ChrClearFlags(0x0009, 0x0080)

    @scena.Lambda('lambda_0A71')
    def lambda_0A71():
        ChrWalkTo(0x0101, 78930, 0, 2080, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0A71)

    OP_72(0x0001, 0x0010)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 60)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    ChrSetDirection(0x0101, 90, 1000)
    Sleep(1000)

    ChrSetDirection(0x0101, 270, 1000)
    Sleep(1000)

    ChrSetDirection(0x0101, 90, 1000)
    OP_69(0x0009, 2000)

    @scena.Lambda('lambda_0ACB')
    def lambda_0ACB():
        OP_69(0x0009, 0)
        Yield()

        Jump('lambda_0ACB')

    DispatchAsync2(0x0009, 0x0003, lambda_0ACB)

    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 60)
    OP_73(0x0000)
    ChrWalkTo(0x0009, 66490, 0, 1780, 2000, 0x00)
    OP_62(0x0009, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(500)

    ChrTurnDirection(0x0009, 0x0101, 500)
    Sleep(500)

    TerminateThread(0x0009, 0x03)

    @scena.Lambda('lambda_0B2D')
    def lambda_0B2D():
        CameraMove(76750, 0, 2160, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0B2D)

    @scena.Lambda('lambda_0B45')
    def lambda_0B45():
        OP_67(0, 8000, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B45)

    @scena.Lambda('lambda_0B5D')
    def lambda_0B5D():
        CameraSetDistance(2800, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0B5D)

    @scena.Lambda('lambda_0B6D')
    def lambda_0B6D():
        OP_6E(262, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0B6D)

    ChrWalkTo(0x0009, 74790, 0, 2100, 2000, 0x00)

    ChrTalk(
        0x0009,
        (
            '#0030190018V#6P#020F哎呀，艾丝蒂尔。\n',
            '这么晚才睡醒呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0009, 500)

    ChrTalk(
        0x0101,
        (
            '#0010190019V#587F#2P雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030190020V#6P#021F真是的，昨天那么晚还不回来，\n',
            '叫人担心死了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030190021V不过看起来，你应该是\n',
            '和约修亚聊了很多──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0101, 0x0009, 2000, 5000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010190022V#005F#2P雪拉姐，约修亚在哪儿！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030190023V#6P#023F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190024V#005F#2P我在找约修亚！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190025V雪拉姐，你见过他吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030190026V#6P#023F今天早上没见到过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030190027V话说回来，你不是昨天太累了\n',
            '就睡在那边的房间了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030190028V醒来的时候他不在？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190029V#580F#2P咦……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190030V我太累，就睡了……\n',
            '你是听谁说的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030190031V#6P#023F老师说的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190032V#580F#2P老、老爸！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190033V#005F那么！\n',
            '你有没有看见老爸！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0030190034V#6P#022F老师他刚才走上楼梯\n',
            '去了空中庭园……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010190035V#002F#2P！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 800)

    @scena.Lambda('lambda_0EDF')
    def lambda_0EDF():
        CameraMove(78660, 0, 2110, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_0EDF)

    @scena.Lambda('lambda_0EF7')
    def lambda_0EF7():
        ChrWalkTo(0x00FE, 91410, 0, 2360, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0EF7)

    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0030190036V#023F啊，等等，艾丝蒂尔！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    OP_69(0x0009, 1500)

    ChrTalk(
        0x0009,
        (
            '#0030190037V#022F……怎么回事……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    @scena.Lambda('lambda_0F83')
    def lambda_0F83():
        OP_6E(240, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_0F83)

    Fade(1000)
    ChrSetChipByIndex(0x0009, 3)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0030190038V#022F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030190039V#522F逆位的『恋人』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0200, 2, 0x1002))
    FadeOut(1500, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T4201._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x100C
@scena.Code('func_04_100C')
def func_04_100C():
    EventBegin(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_102E'),
        (0x00000001, 'loc_106E'),
        (0x00000002, 'loc_10AC'),
        (0x00000005, 'loc_10E5'),
        (0x00000007, 'loc_111E'),
        (0x00000006, 'loc_115B'),
        (-1, 'loc_119A'),
    )

    def _loc_102E(): pass

    label('loc_102E')

    ChrTalk(
        0x0101,
        (
            '#0010380301V#1002F不，不是这边。\n',
            '……得抓紧前往女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_119A')

    def _loc_106E(): pass

    label('loc_106E')

    ChrTalk(
        0x0102,
        (
            '#0020380302V#1042F不对，不是这边。\n',
            '……赶紧去女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_119A')

    def _loc_10AC(): pass

    label('loc_10AC')

    ChrTalk(
        0x0103,
        (
            '#0030380303V#022F这边不对。\n',
            '……赶紧去女王宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_119A')

    def _loc_10E5(): pass

    label('loc_10E5')

    ChrTalk(
        0x0106,
        (
            '#0050380304V#057F没时间磨蹭了，\n',
            '赶快去女王宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_119A')

    def _loc_111E(): pass

    label('loc_111E')

    ChrTalk(
        0x0108,
        (
            '#0080380305V#072F没空去别处了。\n',
            '……抓紧去女王宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_119A')

    def _loc_115B(): pass

    label('loc_115B')

    ChrTalk(
        0x0107,
        (
            '#0070380306V#062F不、不是这边。\n',
            '……得抓紧前往女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_119A')

    def _loc_119A(): pass

    label('loc_119A')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0005 offset: 0x11BB
@scena.Code('func_05_11BB')
def func_05_11BB():
    EventBegin(0x01)

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_11DD'),
        (0x00000001, 'loc_121D'),
        (0x00000002, 'loc_125B'),
        (0x00000005, 'loc_1294'),
        (0x00000007, 'loc_12CD'),
        (0x00000006, 'loc_130A'),
        (-1, 'loc_1349'),
    )

    def _loc_11DD(): pass

    label('loc_11DD')

    ChrTalk(
        0x0101,
        (
            '#0010380301V#1002F不，不是这边。\n',
            '……得抓紧前往女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1349')

    def _loc_121D(): pass

    label('loc_121D')

    ChrTalk(
        0x0102,
        (
            '#0020380302V#1042F不对，不是这边。\n',
            '……赶紧去女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1349')

    def _loc_125B(): pass

    label('loc_125B')

    ChrTalk(
        0x0103,
        (
            '#0030380303V#022F这边不对。\n',
            '……赶紧去女王宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1349')

    def _loc_1294(): pass

    label('loc_1294')

    ChrTalk(
        0x0106,
        (
            '#0050380304V#057F没时间磨蹭了，\n',
            '赶快去女王宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1349')

    def _loc_12CD(): pass

    label('loc_12CD')

    ChrTalk(
        0x0108,
        (
            '#0080380305V#072F没空去别处了。\n',
            '……抓紧去女王宫吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1349')

    def _loc_130A(): pass

    label('loc_130A')

    ChrTalk(
        0x0107,
        (
            '#0070380306V#062F不、不是这边。\n',
            '……得抓紧前往女王宫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1349')

    def _loc_1349(): pass

    label('loc_1349')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    MapSetFlags(0x02000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
