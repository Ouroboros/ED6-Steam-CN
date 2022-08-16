import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4205_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4205   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4205.x'
    header.mapIndex       = 1
    header.bgm            = 17
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
        ('ED6_DT07/CH02010._CH', 'ED6_DT07/CH02010P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
        ('ED6_DT07/CH00010._CH', 'ED6_DT07/CH00010P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH00260._CH', 'ED6_DT07/CH00260P._CP'),
        ('ED6_DT07/CH00262._CH', 'ED6_DT07/CH00262P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00141._CH', 'ED6_DT07/CH00141P._CP'),
        ('ED6_DT07/CH02200._CH', 'ED6_DT07/CH02200P._CP'),
        ('ED6_DT07/CH00264._CH', 'ED6_DT07/CH00264P._CP'),
        ('ED6_DT07/CH00104._CH', 'ED6_DT07/CH00104P._CP'),
        ('ED6_DT07/CH00124._CH', 'ED6_DT07/CH00124P._CP'),
        ('ED6_DT07/CH00144._CH', 'ED6_DT07/CH00144P._CP'),
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
    ]

# id: 0x10001 offset: 0x152
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '艾莉茜雅女王',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '尤莉亚中尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '约修亚',
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
        ScenaNpcData(
            name                = '奥利维尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '金',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '洛伦斯少尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '洛伦斯残像',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '洛伦斯残像',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '洛伦斯残像',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '洛伦斯残像',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x292
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x292
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x292
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x292
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_29E'),
        (-1, 'loc_2B4'),
    )

    def _loc_29E(): pass

    label('loc_29E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 6, 0x666)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 5, 0x665)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2B1',
    )

    SetScenaFlags(ScenaFlag(0x00CC, 6, 0x666))
    Event(0, func_04_599)

    def _loc_2B1(): pass

    label('loc_2B1')

    Jump('loc_2B4')

    def _loc_2B4(): pass

    label('loc_2B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2DE',
    )

    ChrSetChipByIndex(0x0000, 18)
    ChrSetChipByIndex(0x0001, 19)
    ChrSetChipByIndex(0x0138, 20)
    ChrSetFlags(0x0000, 0x1000)
    ChrSetFlags(0x0001, 0x1000)
    ChrSetFlags(0x0138, 0x1000)

    def _loc_2DE(): pass

    label('loc_2DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_300',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 2170, 12000, 62700, 0)

    def _loc_300(): pass

    label('loc_300')

    Return()

# id: 0x0001 offset: 0x301
@scena.Code('func_01_301')
def func_01_301():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CE, 0, 0x670)),
            Expr.Return,
        ),
        'loc_31D',
    )

    MapSetFlags(0x02000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_06_2DE9)

    Jump('loc_32D')

    def _loc_31D(): pass

    label('loc_31D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 4, 0x644)),
            Expr.Return,
        ),
        'loc_32D',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_32D(): pass

    label('loc_32D')

    Return()

# id: 0x0002 offset: 0x32E
@scena.Code('func_02_32E')
def func_02_32E():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_343',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_32E')

    def _loc_343(): pass

    label('loc_343')

    Return()

# id: 0x0003 offset: 0x344
@scena.Code('func_03_344')
def func_03_344():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DF, 0, 0x6F8)),
            Expr.Return,
        ),
        'loc_3DF',
    )

    ChrTurnDirection(0x0008, 0x0102, 0)

    ChrTalk(
        0x0008,
        (
            '#0630121329V#090F艾丝蒂尔、约修亚，\n',
            '我好久没有像今天这样开心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121330V可以的话，以后一定要再来\n',
            '和我一起喝喝茶、谈谈心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_595')

    def _loc_3DF(): pass

    label('loc_3DF')

    SetScenaFlags(ScenaFlag(0x00DF, 0, 0x6F8))
    ChrTurnDirection(0x0008, 0x0138, 0)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0630121322V#097F咦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121323V#090F约修亚刚才竟然也能来到这里，\n',
            '我原本觉得很不可思议……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121324V不过现在看来，我算是明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121325V#091F呵呵，特务兵们\n',
            '会被骗过去也是很正常的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121326V#090F……艾丝蒂尔、约修亚，\n',
            '我好久没有像今天这样开心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121327V可以的话，以后一定要再来\n',
            '和我一起喝喝茶、谈谈心哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630121328V下次也把科洛蒂娅和卡西乌斯上校\n',
            '他们一起叫来聊聊天吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_595(): pass

    label('loc_595')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x599
@scena.Code('func_04_599')
def func_04_599():
    EventBegin(0x00)
    OP_28(0x004E, 0x01, 0x0008)
    CameraMove(2240, 12000, 50930, 0)
    OP_67(0, 11000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(135000, 0)
    OP_6E(255, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x0008, 2170, 12000, 62700, 0)
    ChrSetPos(0x000D, 4080, 12000, 64099, 180)
    ChrSetPos(0x0101, 1870, 12000, 45230, 0)
    ChrSetPos(0x0105, 1870, 12000, 45230, 0)
    ChrSetPos(0x0103, 1870, 12000, 45230, 0)
    ChrSetChipByIndex(0x0101, 7)
    ChrSetChipByIndex(0x0103, 9)
    ChrSetChipByIndex(0x0105, 11)
    ChrSetRGBAMask(0x0105, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0103, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_0673')
    def lambda_0673():
        CameraMove(1570, 12000, 55660, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0673)

    @scena.Lambda('lambda_068B')
    def lambda_068B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_068B)

    @scena.Lambda('lambda_069D')
    def lambda_069D():
        ChrWalkTo(0x00FE, 1840, 12000, 54630, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_069D)

    Sleep(500)

    @scena.Lambda('lambda_06BD')
    def lambda_06BD():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_06BD)

    @scena.Lambda('lambda_06CF')
    def lambda_06CF():
        ChrWalkTo(0x00FE, 3020, 12000, 53420, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_06CF)

    Sleep(500)

    @scena.Lambda('lambda_06EF')
    def lambda_06EF():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0103, 0x0002, lambda_06EF)

    @scena.Lambda('lambda_0701')
    def lambda_0701():
        ChrWalkTo(0x00FE, 620, 12000, 53660, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0701)

    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0105,
        (
            '#040F祖母大人，您没事吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F我们来救您了，女王陛下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0105, 400)

    ChrTalk(
        0x0008,
        (
            '#090F科洛蒂娅……\n',
            '还有艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '总算来了……\n',
            '我已经等得有些不耐烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_07BD')
    def lambda_07BD():
        ChrWalkTo(0x000D, 2770, 12000, 62440, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_07BD)

    @scena.Lambda('lambda_07D8')
    def lambda_07D8():
        ChrTurnDirection(0x000D, 0x0105, 0)
        Yield()

        Jump('lambda_07D8')

    DispatchAsync2(0x000D, 0x0001, lambda_07D8)

    @scena.Lambda('lambda_07E9')
    def lambda_07E9():
        CameraMove(2180, 13000, 59350, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_07E9)

    @scena.Lambda('lambda_0801')
    def lambda_0801():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0801)

    @scena.Lambda('lambda_0811')
    def lambda_0811():
        OP_6E(321, 3000)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_0811)

    @scena.Lambda('lambda_0821')
    def lambda_0821():
        OP_67(0, 6360, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0105, 0x0003, lambda_0821)

    Sleep(800)

    @scena.Lambda('lambda_083E')
    def lambda_083E():
        ChrMoveTo(0x00FE, 2190, 12000, 63300, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_083E)

    Sleep(200)

    @scena.Lambda('lambda_085E')
    def lambda_085E():
        ChrWalkTo(0x00FE, 2110, 12000, 56770, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_085E)

    Sleep(110)

    @scena.Lambda('lambda_087E')
    def lambda_087E():
        ChrWalkTo(0x00FE, 3360, 12000, 57270, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_087E)

    Sleep(100)

    @scena.Lambda('lambda_089E')
    def lambda_089E():
        ChrWalkTo(0x00FE, 640, 12000, 57460, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_089E)

    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#000F洛、洛伦斯少尉！\n',
            '你怎么会在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000D, 0xFF)

    ChrTalk(
        0x000D,
        (
            '#0141070005V#280F呵呵……\n',
            '我的任务是保护女王陛下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131289V出现在这里也没什么不可思议的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F别开玩笑了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131291V不管你的实力有多强，\n',
            '我们这边可是有三个人的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F怎么会，这家伙……\n',
            '好强的压迫感。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131173V到底是谁？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F他是情报部——特务部队队长，\n',
            '洛伦斯·博格少尉！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131295V过去是猎兵出身，\n',
            '后来被上校招入麾下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#280F哦，竟然调查到这样的程度了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131297V不愧是Ｓ级游击士\n',
            '卡西乌斯·布莱特的女儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F居然连从未向外界公布过的\n',
            '老师的级别也知道……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131300V这家伙，不是个等闲之辈啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#280F呵呵……\n',
            '你的事情我也很清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '级别Ｃ、外号『银闪』的\n',
            '雪拉扎德·哈维。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131303V近日似乎就要升成级别Ｂ了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F对、对不起……\n',
            '请把祖母交还给我好吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060131306V如果你只是被\n',
            '上校所雇佣的话，\n',
            '现在已经没有必要再战斗了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0141070006V#280F呵呵，驱动着这个世界的，\n',
            '并非只有眼睛能够看得到的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131308V就像只看结晶回路盘是无法\n',
            '知晓齿轮的运动一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#280F注意听好了，科洛蒂娅公主。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131311V所谓国家，与巨大而复杂\n',
            '的导力器是相似的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131312V将人的力量像结晶回路一样充分调动起来的，\n',
            '就是所谓组织、制度这样的齿轮……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131313V而将其包裹着的就是国土这样的框架。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0141070007V对于这些知识，如果不能掌握，\n',
            '那你就没有作为女王的资格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F非常有趣的比喻啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '而且……\n',
            '的确有可能如你所说的那般。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131318V真没有想到在这样的地方\n',
            '竟然能听到国家论……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0008, 400)

    ChrTalk(
        0x000D,
        (
            '#280F呵呵……刚才失礼了。\n',
            '这些说法对于陛下您来说是没有必要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F虽然不太明白是怎么回事儿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过看起来，你好像\n',
            '没有释放女王陛下的打算了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0101, 400)

    ChrTalk(
        0x000D,
        (
            '#280F就算如此……你们想要怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F那还用说……\n',
            '拼尽全力也要救回女王陛下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F是啊……\n',
            '既然已经到了这里，就没有理由后退了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060940011V#040F……虽然从你身上\n',
            '感觉不到什么敌意……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '但是为了将祖母大人救回来，\n',
            '我会向你挥起手中的剑的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#280F哼哼，不错啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0008, 400)
    ChrWalkTo(0x000D, 2530, 12000, 62690, 2000, 0x00)

    @scena.Lambda('lambda_1066')
    def lambda_1066():
        ChrMoveToRelative(0x00FE, 0, 0, 2000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1066)

    @scena.Lambda('lambda_1081')
    def lambda_1081():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 2000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1081)

    @scena.Lambda('lambda_109C')
    def lambda_109C():
        OP_67(0, 5500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_109C)

    @scena.Lambda('lambda_10B4')
    def lambda_10B4():
        OP_6E(295, 3000)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_10B4)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetFlags(0x000D, 0x0020)

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0xB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000D, 6)
    ChrTurnDirection(0x000D, 0x0105, 400)

    @scena.Lambda('lambda_10E5')
    def lambda_10E5():
        OP_99(0x00FE, 0x00, 0x0B, 3000)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_10E5)

    ChrJumpTo(0x000D, 2220, 12000, 61180, 400, 7000)
    WaitForThreadExit(0x000D, 0x0001)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x000D,
        (
            '#0141070008V#280F来……我当你们的对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Battle(0x0000039A, 0x00000000, 0x00, 0x0000, 0xFF)
    EventBegin(0x00)
    ChrSetPos(0x0101, 3360, 12000, 57270, 0)
    ChrSetPos(0x0105, 2110, 12000, 56770, 0)
    ChrSetPos(0x0103, 640, 12000, 57460, 0)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_1194'),
        (0x00000001, 'loc_15B8'),
        (-1, 'loc_16EA'),
    )

    def _loc_1194(): pass

    label('loc_1194')

    OP_28(0x004E, 0x01, 0x0010)

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000D, 14)
    ChrSetPos(0x000D, 2220, 12000, 61180, 180)
    OP_2B(0x004D, 0x0003)

    ChrTalk(
        0x000D,
        (
            '#0141070009V#280F……真令人吃惊啊……\n',
            '没想到你们可以达到这种程度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F呼呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你、你这家伙！\n',
            '当初决赛的时候没有尽全力吧！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131342V和那时相比强悍得判若两人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F竟、竟然可以\n',
            '打败这样的怪物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F的、的确难以置信啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#280F艾丝蒂尔·布莱特……\n',
            '刚才对你太过轻视，在下深表歉意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131346V你如果能继续这么走下去……\n',
            '达到你父亲那种境界也未尝不可。　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#280F不过……现在还有一定差距。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1386')
    def lambda_1386():
        CameraMove(2400, 12000, 57540, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1386)

    OP_99(0x000D, 0x03, 0x00, 2000)

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0xB),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000D, 6)
    ChrSetRGBAMask(0x000E, 255, 255, 255, 200, 0)
    ChrSetRGBAMask(0x000F, 255, 255, 255, 150, 0)
    ChrSetRGBAMask(0x0010, 255, 255, 255, 100, 0)
    ChrSetRGBAMask(0x0011, 255, 255, 255, 50, 0)
    ChrSetPos(0x000E, 2220, 12000, 61180, 180)
    ChrSetPos(0x000F, 2220, 12000, 61180, 180)
    ChrSetPos(0x0010, 2220, 12000, 61180, 180)
    ChrSetPos(0x0011, 2220, 12000, 61180, 180)
    CreateThread(0x000D, 0x01, 0x00, func_05_2D47)
    Sleep(70)

    CreateThread(0x000E, 0x01, 0x00, func_05_2D47)
    Sleep(70)

    CreateThread(0x000F, 0x01, 0x00, func_05_2D47)
    Sleep(70)

    CreateThread(0x0010, 0x01, 0x00, func_05_2D47)
    Sleep(70)

    CreateThread(0x0011, 0x01, 0x00, func_05_2D47)
    OP_A6(0x0000)

    @scena.Lambda('lambda_1461')
    def lambda_1461():
        OP_6C(24000, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_1461)

    OP_A6(0x0000)

    @scena.Lambda('lambda_1474')
    def lambda_1474():
        OP_67(0, 6730, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1474)

    OP_A6(0x0002)
    PlayEffect(0x08, 0xFF, 0x00FF, 2360, 14000, 57260, 0, 0, 0, 2400, 2400, 2400, 0x00FF, 0, 0, 0, 0)

    ExecExpressionWithValue(
        0x0105,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0105, 17)
    ChrTurnDirection(0x0105, 0x000D, 0)

    @scena.Lambda('lambda_14DB')
    def lambda_14DB():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_14DB)

    @scena.Lambda('lambda_14F1')
    def lambda_14F1():
        OP_99(0x00FE, 0x00, 0x03, 2000)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_14F1)

    ExecExpressionWithValue(
        0x0103,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0103, 16)
    ChrTurnDirection(0x0103, 0x000D, 0)

    @scena.Lambda('lambda_1518')
    def lambda_1518():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0002, lambda_1518)

    @scena.Lambda('lambda_152E')
    def lambda_152E():
        OP_99(0x00FE, 0x00, 0x03, 2000)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_152E)

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0101, 15)
    ChrTurnDirection(0x0101, 0x000D, 0)

    @scena.Lambda('lambda_1555')
    def lambda_1555():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000003E8, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1555)

    @scena.Lambda('lambda_156B')
    def lambda_156B():
        OP_99(0x00FE, 0x00, 0x03, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_156B)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#000F啊啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F呜……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F呀啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16EA')

    def _loc_15B8(): pass

    label('loc_15B8')

    OP_28(0x004E, 0x01, 0x0020)
    ChrSetChipByIndex(0x0105, 17)
    ChrSetChipByIndex(0x0103, 16)
    ChrSetChipByIndex(0x0101, 15)

    ChrTalk(
        0x000D,
        (
            '#280F……真让人失望。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131353V原本还以为\n',
            '可以让我有些起劲呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F为、为什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131355V和当初的决赛时完全不同……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F……可能那时他\n',
            '还没有尽全力吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131357V这样强大的力量……\n',
            '或许已经可以和老师匹敌了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F祖母大人……\n',
            '……对不起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16EA')

    def _loc_16EA(): pass

    label('loc_16EA')

    ChrTalk(
        0x0008,
        (
            '#090F科洛蒂娅！\n',
            '艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1710')
    def lambda_1710():
        ChrWalkTo(0x00FE, 1780, 12000, 61930, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1710)

    Sleep(200)

    ChrSetFlags(0x000E, 0x0080)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)
    ChrSetFlags(0x0011, 0x0080)
    ChrTurnDirection(0x000D, 0x0008, 400)

    @scena.Lambda('lambda_174B')
    def lambda_174B():
        CameraMove(2260, 12000, 60490, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_174B)

    @scena.Lambda('lambda_1763')
    def lambda_1763():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1763')

    DispatchAsync2(0x000D, 0x0001, lambda_1763)

    ChrJumpTo(0x000D, 2830, 12000, 61950, 1000, 4000)
    ChrTurnDirection(0x000D, 0x0008, 400)

    ChrTalk(
        0x000D,
        (
            '#280F陛下，她们只是\n',
            '暂时不能动了而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131361V并没有生命危险。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0141070010V#280F哼哼，不错啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000D, 0x0020)

    ExecExpressionWithValue(
        0x000D,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x000D, 13)
    TerminateThread(0x000D, 0xFF)
    ChrTurnDirection(0x000D, 0x0105, 400)

    ChrTalk(
        0x000D,
        (
            '#0141070011V#280F那么……\n',
            '就让我好好活动一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0141070012V恕我失礼……\n',
            '让我摘下这东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x000D, 400)
    ChrTurnDirection(0x0105, 0x000D, 0)
    OP_99(0x0105, 0x03, 0x00, 1000)
    ChrSetChipByIndex(0x0105, 11)
    ChrTurnDirection(0x0101, 0x000D, 0)
    OP_99(0x0101, 0x03, 0x00, 1000)
    ChrSetChipByIndex(0x0101, 7)
    ChrTurnDirection(0x0103, 0x000D, 0)
    OP_99(0x0103, 0x03, 0x00, 1000)
    ChrSetChipByIndex(0x0103, 9)

    ChrTalk(
        0x0101,
        (
            '#000F银、银发……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F不……\n',
            '是苍金色的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131333V这家伙……\n',
            '看起来似乎是出生在北方的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0141070013V#280F呵呵……\n',
            '的确是北方没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131335V不过离这里\n',
            '也不算很遥远。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060940012V#040F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F那双眼眸……\n',
            '为何会有那么深邃的颜色呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131364V明明还这么年轻……\n',
            '可是却好像经历了巨大的苦难啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0008, 400)

    ChrTalk(
        0x000D,
        (
            '#280F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '女王啊，您是没有\n',
            '怜悯我的资格的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131367V对于知道『哈梅尔』\n',
            '这个名字的您来说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0631160001V#090F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0105, 400)

    ChrTalk(
        0x000D,
        (
            '#280F好了，差不多是时候了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131370V如你们所愿，\n',
            '我将女王予以归还。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#280F如果想要阻止上校，\n',
            '就赶快前去地下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131373V虽然可能已经来不及了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131374V不过还可以抑制住\n',
            '不必要的伤亡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F地下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131376V难道是说从那个地方\n',
            '降到地下的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0008, 400)

    ChrTalk(
        0x000D,
        (
            '#0141070014V#280F哼哼……现在的您对其中的含义，\n',
            '应该清楚的不能再清楚了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140131378V为他们指引前进的道路吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……那么，再会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1CB3')
    def lambda_1CB3():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_1CB3')

    DispatchAsync2(0x0008, 0x0001, lambda_1CB3)

    @scena.Lambda('lambda_1CC4')
    def lambda_1CC4():
        CameraMove(1670, 12000, 63950, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1CC4)

    @scena.Lambda('lambda_1CDC')
    def lambda_1CDC():
        OP_6E(347, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1CDC)

    @scena.Lambda('lambda_1CEC')
    def lambda_1CEC():
        OP_67(0, 6160, -10000, 2000)

        ExitThread()

    DispatchAsync(0x000D, 0x0003, lambda_1CEC)

    ChrWalkTo(0x000D, 3070, 12000, 64550, 7000, 0x00)
    ChrWalkTo(0x000D, 2310, 12000, 66890, 7000, 0x00)
    ChrJumpTo(0x000D, 1510, 12600, 67780, 800, 7000)
    ChrJumpTo(0x000D, 1310, -12000, 73830, 1000, 7000)
    WaitForThreadExit(0x000D, 0x0002)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(200)

    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(200)

    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(200)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#000F怎么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0101,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0101, 65535)

    @scena.Lambda('lambda_1DF2')
    def lambda_1DF2():
        ChrWalkTo(0x00FE, 3820, 12000, 67150, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1DF2)

    ChrTalk(
        0x0103,
        (
            '#020F来、来真的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1E26')
    def lambda_1E26():
        CameraMove(2270, 12000, 66180, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1E26)

    @scena.Lambda('lambda_1E3E')
    def lambda_1E3E():
        OP_6C(129000, 2000)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_1E3E)

    Sleep(200)

    ExecExpressionWithValue(
        0x0103,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0103, 65535)

    @scena.Lambda('lambda_1E63')
    def lambda_1E63():
        ChrWalkTo(0x00FE, 750, 12000, 67290, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_1E63)

    Sleep(500)

    ExecExpressionWithValue(
        0x0105,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0105, 65535)

    @scena.Lambda('lambda_1E93')
    def lambda_1E93():
        ChrWalkTo(0x00FE, 1770, 12000, 60750, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_1E93)

    WaitForThreadExit(0x0105, 0x0001)

    @scena.Lambda('lambda_1EB3')
    def lambda_1EB3():
        ChrTurnDirection(0x00FE, 0x0105, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1EB3)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#000F不、不见了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '落到湖里去了……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0103, 0x0001)

    ChrTalk(
        0x0103,
        (
            '#020F这么说来……\n',
            '可是湖面并没有波痕……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131385V那个男的，究竟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F祖母大人……\n',
            '您没有受伤吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F没有呢，科洛蒂娅。\n',
            '他并没有伤害我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '话说回来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x000B, 0x0040)
    ChrSetFlags(0x000A, 0x0040)
    ChrSetFlags(0x000C, 0x0040)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetPos(0x000B, 1870, 12000, 45230, 0)
    ChrSetPos(0x000A, 1870, 12000, 45230, 0)
    ChrSetPos(0x000C, 1870, 12000, 45230, 0)
    ChrSetPos(0x0009, 1870, 12000, 45230, 0)
    ChrSetRGBAMask(0x000A, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000C, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2052')
    def lambda_2052():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2052)

    @scena.Lambda('lambda_2060')
    def lambda_2060():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_2060)

    @scena.Lambda('lambda_206E')
    def lambda_206E():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_206E)

    @scena.Lambda('lambda_207C')
    def lambda_207C():
        CameraMove(2540, 12000, 61390, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_207C)

    @scena.Lambda('lambda_2094')
    def lambda_2094():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_2094)

    @scena.Lambda('lambda_20A6')
    def lambda_20A6():
        ChrWalkTo(0x00FE, 3370, 12000, 58260, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_20A6)

    Sleep(500)

    @scena.Lambda('lambda_20C6')
    def lambda_20C6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_20C6)

    @scena.Lambda('lambda_20D8')
    def lambda_20D8():
        ChrWalkTo(0x00FE, 2000, 12000, 59510, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_20D8)

    Sleep(500)

    @scena.Lambda('lambda_20F8')
    def lambda_20F8():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_20F8')

    DispatchAsync2(0x000B, 0x0001, lambda_20F8)

    @scena.Lambda('lambda_2109')
    def lambda_2109():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_2109)

    @scena.Lambda('lambda_211B')
    def lambda_211B():
        ChrWalkTo(0x00FE, 2070, 12000, 57860, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_211B)

    Sleep(500)

    @scena.Lambda('lambda_213B')
    def lambda_213B():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_213B')

    DispatchAsync2(0x000C, 0x0001, lambda_213B)

    @scena.Lambda('lambda_214C')
    def lambda_214C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_214C)

    @scena.Lambda('lambda_215E')
    def lambda_215E():
        ChrWalkTo(0x00FE, 710, 12000, 58440, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_215E)

    @scena.Lambda('lambda_2179')
    def lambda_2179():
        ChrWalkTo(0x00FE, 3570, 12000, 59430, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2179)

    Sleep(500)

    @scena.Lambda('lambda_2199')
    def lambda_2199():
        ChrWalkTo(0x00FE, 150, 12000, 60340, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_2199)

    @scena.Lambda('lambda_21B4')
    def lambda_21B4():
        CameraMove(2140, 12000, 59300, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_21B4)

    @scena.Lambda('lambda_21CC')
    def lambda_21CC():
        OP_6E(307, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_21CC)

    ChrSetFlags(0x0105, 0x0040)
    ChrWalkTo(0x0105, 2850, 12000, 61440, 2000, 0x00)
    ChrTurnDirection(0x0105, 0x0009, 400)
    WaitForThreadExit(0x0103, 0x0001)

    @scena.Lambda('lambda_2201')
    def lambda_2201():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_2201)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#000F约修亚！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '太好了，你平安无事！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#010F艾丝蒂尔你那边才是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131393V因为理查德上校和洛伦斯少尉\n',
            '都没有在城内，我很是有些担心呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F那个戴红色头盔的，\n',
            '倒是刚才还在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#010F咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030840012V#020F他撞破窗户\n',
            '一跃而下，逃走了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真是一个超越常理的怪物啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#010F哦，原来是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '真是太好了……\n',
            '你能够平安无事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F约、约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0009, 1840, 12000, 60370, 2000, 0x00)

    ChrTalk(
        0x0009,
        (
            '#170F陛下……幸好您没事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F尤莉亚中尉……\n',
            '能再见到你我真的很愉快呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '而且，大家……\n',
            '我对你们的感激也是一言难尽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2435')
    def lambda_2435():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2435)

    @scena.Lambda('lambda_2443')
    def lambda_2443():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_2443)

    @scena.Lambda('lambda_2451')
    def lambda_2451():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_2451)

    @scena.Lambda('lambda_245F')
    def lambda_245F():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_245F)

    @scena.Lambda('lambda_246D')
    def lambda_246D():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_246D)

    @scena.Lambda('lambda_247B')
    def lambda_247B():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_247B)

    ChrTalk(
        0x000B,
        (
            '#030F呵呵，女王陛下。\n',
            '您过奖了，我感到非常荣幸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#070F能够为您服务，我已深感荣幸了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过现在还\n',
            '没有到结束的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#170F虽然已镇压住了城内的特务兵，\n',
            '但又传来了不利的消息。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100131408V各地的正规军部队\n',
            '正朝着王都方向攻来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100131409V很可能是被\n',
            '情报部给操控了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F是这样的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#170F虽然很抱歉，不过已经没时间了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100131412V务必请您乘坐\n',
            '飞行艇从这儿离开吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F不行……我办不到。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '话说回来……\n',
            '可怕的事情就要发生了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131415V无论如何也要\n',
            '阻止理查德上校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#170F怎、怎么回事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F昨夜，我和上校谈话之后，　　\n',
            '总算明白了其真正的目的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0631160002V他企图将『辉之环』\n',
            '据为己有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F『辉之环』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131420V好、好像在哪里\n',
            '好像在哪儿听到过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#010F……女神赐予古代人的\n',
            '『七至宝』之一……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '可以支配世间一切的\n',
            '传说中的古代遗迹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哦，是亚鲁瓦教授说过的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131424V可是那只是教会\n',
            '流传下来的故事啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#030F嗯，应该存在吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040131428V在这个利贝尔王国的某处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F古老的王家传承如下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0631160003V『辉之环，总有一天会带来灾难，\n',
            '将人类之子的灵魂与炼狱相接。』',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0631160004V『我等，为了作为人而存在，\n',
            '在昏暗的狭间将其封印……』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0081040014V#070F『将人类之子的灵魂与炼狱相接』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '实在是……令人感到可怕的说法啊。　　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F这些箴言，作为戒律\n',
            '从一代代的国王那里相传至今。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131435V也许那个被称作『辉之环』的\n',
            '东西具备这样的危险性，因此\n',
            '王家的祖先才将其封印起来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131436V而且，在王都的地下\n',
            '还检测出了巨大的导力反应……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131437V如果把这两者结合起来考虑的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#010F王都的地下\n',
            '封印着『辉之环』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131439V这么想是理所当然的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F是啊……\n',
            '上校肯定也是这么推断的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131441V『辉之环』究竟是什么样的东西，\n',
            '这一点并没有被传承下来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131442V一旦其被人唤醒，\n',
            '说不定会发生十分可怕的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0631160005V甚至有可能和过去所发生的，\n',
            '传说中的『大崩坏』匹敌……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F怎么……怎么会这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F没有想到，竟然会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F女王陛下！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131447V洛伦斯少尉曾说过\n',
            '『到地下去吧』这样的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010131448V那是代表什么意思呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#090F在这个格兰赛尔城里\n',
            '有一间奇怪的屋子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131450V是一个什么东西也不保管，\n',
            '而且从很久以前就禁止入内的地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#040F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#170F是宝物库吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x004E, 0x01, 0x0040)
    OP_28(0x004E, 0x01, 0x0080)
    OP_28(0x004E, 0x01, 0x0100)
    OP_28(0x004E, 0x01, 0x0200)
    OP_28(0x004E, 0x01, 0x0400)
    OP_28(0x004F, 0x04, 0x02)
    OP_28(0x004F, 0x04, 0x04)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4240._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x2D47
@scena.Code('func_05_2D47')
def func_05_2D47():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetFlags(0x00FE, 0x0020)
    ChrSetFlags(0x00FE, 0x0004)
    ChrClearFlags(0x00FE, 0x0080)
    ChrJumpTo(0x00FE, 2110, 12000, 60200, 400, 6000)
    ChrSetChipByIndex(0x00FE, 6)

    @scena.Lambda('lambda_2D7D')
    def lambda_2D7D():
        OP_99(0x00FE, 0x00, 0x01, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2D7D)

    ChrJumpTo(0x00FE, 1950, 15000, 59050, 3000, 8000)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    Sleep(300)

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    @scena.Lambda('lambda_2DAF')
    def lambda_2DAF():
        OP_99(0x00FE, 0x02, 0x05, 2000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2DAF)

    ChrJumpTo(0x00FE, 1860, 12000, 57860, 0, 15000)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    Sleep(1000)

    @scena.Lambda('lambda_2DDE')
    def lambda_2DDE():
        OP_99(0x00FE, 0x03, 0x0B, 4000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_2DDE)

    Return()

# id: 0x0006 offset: 0x2DE9
@scena.Code('func_06_2DE9')
def func_06_2DE9():
    OP_1F(0x50, 0x000000C8)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
