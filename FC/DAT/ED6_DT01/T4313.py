import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4313_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4313   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4313.x'
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
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP'),
        ('ED6_DT07/CH01570._CH', 'ED6_DT07/CH01570P._CP'),
        ('ED6_DT07/CH01330._CH', 'ED6_DT07/CH01330P._CP'),
        ('ED6_DT07/CH02340._CH', 'ED6_DT07/CH02340P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
    ]

# id: 0x10001 offset: 0x112
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '管家费特',
            x                   = -11780,
            z                   = 0,
            y                   = 20150,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0002,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '特务兵',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '科洛丝',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '奥利维尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '雪拉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
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
            name                = '尤莉亚中尉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '基库',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x272
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x272
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x272
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 25980,
            triggerZ            = 0,
            triggerY            = 50580,
            triggerRange        = 800,
            actorX              = 25690,
            actorZ              = 1000,
            actorY              = 51500,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 22140,
            triggerZ            = 0,
            triggerY            = 50600,
            triggerRange        = 800,
            actorX              = 21830,
            actorZ              = 890,
            actorY              = 51760,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2BA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_2C8',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_06_1346)

    def _loc_2C8(): pass

    label('loc_2C8')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000066, 'loc_2D4'),
        (-1, 'loc_2EA'),
    )

    def _loc_2D4(): pass

    label('loc_2D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 6, 0x656)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 3, 0x653)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2E7',
    )

    SetScenaFlags(ScenaFlag(0x00CA, 6, 0x656))
    Event(0, func_03_5F5)

    def _loc_2E7(): pass

    label('loc_2E7')

    Jump('loc_2EA')

    def _loc_2EA(): pass

    label('loc_2EA')

    Return()

# id: 0x0001 offset: 0x2EB
@scena.Code('func_01_2EB')
def func_01_2EB():
    Return()

# id: 0x0002 offset: 0x2EC
@scena.Code('func_02_2EC')
def func_02_2EC():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 5, 0x655)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 1, 0x679)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_510',
    )

    SetScenaFlags(ScenaFlag(0x00CF, 1, 0x679))
    OP_28(0x004C, 0x01, 0x0010)
    EventBegin(0x00)
    OP_69(0x0008, 1000)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '说明了最深处的豪华大门\n',
            '被锁上了的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#2330130671V是啊，那里\n',
            '是被锁上了的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那个钥匙是由情报部的队长\n',
            '保管着的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130673V因为出现了恐怖分子，\n',
            '中队长好像出动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F也就是说，是到尤莉亚中尉\n',
            '他们埋伏的地方去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F嗯，这可就麻烦了。\n',
            '没时间回去了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130677V等等……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130678V还有一个备用钥匙\n',
            '是保管在某个地方的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130679V我想应该是藏匿\n',
            '在展示室里面的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F展示室！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F立刻去调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_5F1')

    def _loc_510(): pass

    label('loc_510')

    ChrTalk(
        0x00FE,
        (
            '啊，他们集中在这个建筑\n',
            '最深处的『纹章之间』里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '用来签署条约的，\n',
            '具有光辉历史的大厅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F最深处的『纹章之间』吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还有一个备用钥匙\n',
            '是保管在某个地方的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2330130679V我想应该是藏匿\n',
            '在展示室里面的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5F1(): pass

    label('loc_5F1')

    TalkEnd(0x0008)

    Return()

# id: 0x0003 offset: 0x5F5
@scena.Code('func_03_5F5')
def func_03_5F5():
    EventBegin(0x00)
    CameraMove(-14960, 0, 17380, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x0008, -11780, 0, 20150, 225)
    ChrSetChipByIndex(0x0101, 0)
    ChrSetChipByIndex(0x0102, 2)
    ChrSetChipByIndex(0x0108, 4)
    ChrSetPos(0x0101, -16850, 0, 13660, 45)
    ChrSetPos(0x0108, -18160, 0, 13760, 45)
    ChrSetPos(0x0102, -16690, 0, 12820, 45)
    ChrSetPos(0x0009, -10960, 0, 18200, 352)
    ChrSetPos(0x000A, -12000, 0, 18190, 61)
    ChrSetPos(0x000B, -15540, 0, 19130, 135)
    ChrSetPos(0x000C, -14400, 0, 18870, 285)
    ChrSetPos(0x000D, -18830, 0, 18070, 82)

    ChrTalk(
        0x0008,
        (
            '#2330130620V你、你们几个是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哇哇……\n',
            '聚集了不少人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_071C')
    def lambda_071C():
        ChrTurnDirection(0x00FE, 0x0101, 150)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_071C)

    ChrTurnDirection(0x000B, 0x0101, 200)

    ChrTalk(
        0x000B,
        (
            '嗯～……\n',
            '什么，你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '唔～……\n',
            '是不认识的人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F晚上好。\n',
            '我们是游击士协会的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0799')
    def lambda_0799():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0799)

    @scena.Lambda('lambda_07A7')
    def lambda_07A7():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_07A7)

    ChrJumpTo(0x000D, -17920, 0, 18010, 300, 3000)
    ChrTurnDirection(0x000D, 0x0101, 200)

    ChrTalk(
        0x000D,
        (
            '啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130626V#070F你们就在这儿\n',
            '好好睡一觉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0811')
    def lambda_0811():
        ChrWalkTo(0x00FE, -14420, 0, 29200, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0811)

    @scena.Lambda('lambda_082C')
    def lambda_082C():
        ChrWalkTo(0x00FE, -15420, 0, 18460, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_082C)

    @scena.Lambda('lambda_0847')
    def lambda_0847():
        ChrWalkTo(0x00FE, 1360, 0, 34370, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0847)

    CameraMove(-14540, 0, 19000, 500)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0102, 0xFF)
    Battle(0x000003AF, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_892'),
        (-1, 'loc_895'),
    )

    def _loc_892(): pass

    label('loc_892')

    OP_B4(0x00)

    Return()

    def _loc_895(): pass

    label('loc_895')

    EventBegin(0x00)
    CameraMove(-14300, 0, 17270, 0)
    ChrSetPos(0x0009, -10570, 0, 16410, 121)
    ChrSetPos(0x000A, -11440, 0, 14650, 198)
    ChrSetPos(0x000B, -11940, 0, 15850, 225)
    ChrSetPos(0x000C, -18230, 0, 18530, 225)
    ChrSetPos(0x000D, -19110, 0, 14890, 135)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)
    ChrSetPos(0x0101, -14770, 0, 16800, 45)
    ChrSetPos(0x0108, -17220, 0, 15660, 350)
    ChrSetPos(0x0102, -15540, 0, 15160, 45)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, -12550, -10, 19850, 225)

    ChrTalk(
        0x0101,
        (
            '#000F呼，解决掉一批。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F几下就打晕了，\n',
            '真是没有挑战性。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F这里和城里面一样，\n',
            '也是个有酒卖的谈话室呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130630V留、留我一条小命……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_09FC')
    def lambda_09FC():
        ChrMoveTo(0x00FE, -12050, 0, 20370, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_09FC)

    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0108, 65535)

    @scena.Lambda('lambda_0A26')
    def lambda_0A26():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0A26)

    @scena.Lambda('lambda_0A34')
    def lambda_0A34():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A34)

    @scena.Lambda('lambda_0A42')
    def lambda_0A42():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0A42)

    CameraMove(-12590, 0, 19790, 2000)

    @scena.Lambda('lambda_0A61')
    def lambda_0A61():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0A61')

    DispatchAsync2(0x0108, 0x0001, lambda_0A61)

    @scena.Lambda('lambda_0A72')
    def lambda_0A72():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0A72')

    DispatchAsync2(0x0101, 0x0001, lambda_0A72)

    @scena.Lambda('lambda_0A83')
    def lambda_0A83():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0A83')

    DispatchAsync2(0x0102, 0x0001, lambda_0A83)

    ChrTalk(
        0x0008,
        (
            '#2330130631V我、我、我\n',
            '不是他们的同伙！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F我们知道了，\n',
            '你是离宫的工作人员对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130633V#010F我们是接受女王陛下的委托\n',
            '来解救被拘捕的人们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130634V咦……真、真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130635V真的是来\n',
            '救我们的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，因此你可以放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0BA5')
    def lambda_0BA5():
        CameraMove(-15830, 0, 17600, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0BA5)

    ChrWalkTo(0x0008, -12930, 0, 21390, 3000, 0x00)
    ChrWalkTo(0x0008, -15830, 0, 20970, 3000, 0x00)
    ChrWalkTo(0x0008, -16300, 0, 18110, 3000, 0x00)

    ChrTalk(
        0x0008,
        (
            '哈……太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '记者朋友被捕后，\n',
            '我认为我已经活不成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '他应该没事吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F记者朋友……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '啊，奈尔的朋友\n',
            '莫非就是你吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔说明了\n',
            '奈尔失踪事件的经过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '是啊，那时联络\n',
            '奈尔的确实是我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '他想对保护在这里的公主\n',
            '进行一次采访……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '看到他那么热心，我不忍心拒绝，\n',
            '于是我就把他悄悄带了进来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130646V#070F结果事情暴露而被捕了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是啊，说来惭愧，\n',
            '那时我还没有觉察到真相。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '只是听说公主被恐怖分子列为目标，\n',
            '那伙人给囚禁了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '公主要来的事情让我们很高兴，\n',
            '所以根本就没有注意到实情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F算了算了，\n',
            '不要灰心丧气嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F您知道被捕的人们\n',
            '关在哪里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '啊，他们集中在这个建筑\n',
            '最深处的『纹章之间』里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '用来签署条约的，\n',
            '具有光辉历史的大厅。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x004C, 0x01, 0x0002)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 5, 0x655)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F44',
    )

    ChrTalk(
        0x0101,
        (
            '#000F最深处的『纹章之间』吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130657V#070F好，赶快去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x004C, 0x01, 0x0004)

    Jump('loc_1175')

    def _loc_F44(): pass

    label('loc_F44')

    SetScenaFlags(ScenaFlag(0x00CF, 1, 0x679))
    OP_28(0x004C, 0x01, 0x0010)

    ChrTalk(
        0x0101,
        (
            '#000F最深处的大厅……\n',
            '不就是在刚才那边吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0081040031V#070F啊，是里面那扇\n',
            '上了锁的豪华的大门吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130671V是啊，那里\n',
            '是被锁上了的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那个钥匙是由情报部的队长\n',
            '保管着的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130673V因为出现了恐怖分子，\n',
            '中队长好像出动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F也就是说，是到尤莉亚中尉\n',
            '他们埋伏的地方去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F嗯，这可就麻烦了。\n',
            '没时间回去了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130677V等等……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130678V还有一个备用钥匙\n',
            '是保管在某个地方的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2330130679V我想应该是藏匿\n',
            '在展示室里面的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F展示室！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F立刻去调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1175(): pass

    label('loc_1175')

    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x1178
@scena.Code('func_04_1178')
def func_04_1178():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 7, 0x657)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 1, 0x679)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1285',
    )

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00CA, 7, 0x657))
    OP_28(0x004C, 0x01, 0x0020)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有个豪华的深红色花瓶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们调查了一下，\n',
            '经过调查，\n',
            '发现其底部粘有什么东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '备用钥匙',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x036F, 1)

    ChrTalk(
        0x0101,
        (
            '#000F啊，就是它！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130690V#010F这样就可以打开\n',
            '里面那扇门了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_12AB')

    def _loc_1285(): pass

    label('loc_1285')

    ChrTalk(
        0x0101,
        (
            '#000F…干得好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '（假定）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FF)

    def _loc_12AB(): pass

    label('loc_12AB')

    Return()

# id: 0x0005 offset: 0x12AC
@scena.Code('func_05_12AC')
def func_05_12AC():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 7, 0x657)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 1, 0x679)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_131F',
    )

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有○○○○○○○。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们调查了一下，\n',
            '没有找到什么特别的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    Jump('loc_1342')

    def _loc_131F(): pass

    label('loc_131F')

    ChrTalk(
        0x0101,
        (
            '#000F…干得好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '（假定）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1342(): pass

    label('loc_1342')

    TalkEnd(0x00FF)

    Return()

# id: 0x0006 offset: 0x1346
@scena.Code('func_06_1346')
def func_06_1346():
    EventBegin(0x00)
    CameraMove(11600, 0, -11080, 0)
    ChrSetFlags(0x0012, 0x0080)
    ChrSetPos(0x000E, 11330, 0, -10500, 135)
    ChrSetPos(0x0011, 12980, 0, -9840, 233)
    ChrSetPos(0x0012, 9810, 700, -10140, 315)
    ChrSetPos(0x0101, 10700, 0, -11900, 66)
    ChrSetPos(0x0102, 11920, 0, -12750, 353)
    ChrSetPos(0x0108, 11030, 0, -13350, 31)
    ChrSetPos(0x0010, 13240, 0, -12800, 311)
    ChrSetPos(0x000F, 14330, 0, -11910, 252)
    ChrTurnDirection(0x000E, 0x0011, 0)
    ChrTurnDirection(0x0012, 0x0011, 0)
    ChrTurnDirection(0x0101, 0x0011, 0)
    ChrTurnDirection(0x0102, 0x0011, 0)
    ChrTurnDirection(0x0108, 0x0011, 0)
    ChrTurnDirection(0x0010, 0x0011, 0)
    ChrTurnDirection(0x000F, 0x0011, 0)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x0011, 0x0080)
    ChrClearFlags(0x0012, 0x0080)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0102, 0x0080)
    ChrClearFlags(0x0108, 0x0080)
    ChrClearFlags(0x0010, 0x0080)
    ChrClearFlags(0x000F, 0x0080)

    ChrTalk(
        0x0011,
        (
            '#170F我真的……\n',
            '真是不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130859V由于我的不中用，\n',
            '而让大家这么的辛苦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130860V如果没能完成任务，办事不周的我将会\n',
            '用自己的双手将身体撕裂，以谢此罪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '请不要这么说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '能够这样和大家再次相会，\n',
            '我已经觉得非常开心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0060130863V你们能够来救我……\n',
            '真是太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#170F殿下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0012, 400)

    ChrTalk(
        0x0101,
        (
            '#000F哎呀，在这样的场所感动，\n',
            '总感觉有些不太合适呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '为何基库也在这里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_15DB')
    def lambda_15DB():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_15DB)

    @scena.Lambda('lambda_15E9')
    def lambda_15E9():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_15E9)

    @scena.Lambda('lambda_15F7')
    def lambda_15F7():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_15F7)

    @scena.Lambda('lambda_1605')
    def lambda_1605():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1605)

    @scena.Lambda('lambda_1613')
    def lambda_1613():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1613)

    @scena.Lambda('lambda_1621')
    def lambda_1621():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1621)

    ChrTurnDirection(0x0012, 0x0101, 400)

    ChrTalk(
        0x0012,
        (
            '啾？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0011, 0x0101, 400)

    ChrTalk(
        0x0011,
        (
            '#0100130868V#170F呵呵，基库在作为\n',
            '殿下的护卫的同时，\n',
            '也是亲卫队的传令员哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130869V你们忘了在旅馆收到的\n',
            '那封信了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_16C7')
    def lambda_16C7():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_16C7)

    @scena.Lambda('lambda_16D5')
    def lambda_16D5():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_16D5)

    @scena.Lambda('lambda_16E3')
    def lambda_16E3():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_16E3)

    @scena.Lambda('lambda_16F1')
    def lambda_16F1():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_16F1)

    @scena.Lambda('lambda_16FF')
    def lambda_16FF():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_16FF)

    @scena.Lambda('lambda_170D')
    def lambda_170D():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_170D)

    ChrTalk(
        0x0101,
        (
            '#000F啊……是那天晚上！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F果然是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130872V这么说来，让尤莉亚中尉\n',
            '得知女王陛下委托的也是它了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#170F嗯，是女王陛下直接\n',
            '通过基库告知我的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0101060023V不过殿下所在的这个大房间\n',
            '没有基库可以进入的窗户。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130875V不能及时取得联系真让我很担心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000E, 0x0101, 400)

    ChrTalk(
        0x000E,
        (
            '#0060940025V呵呵，说得没错呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0012, 400)

    ChrTalk(
        0x0101,
        (
            '#000F还真是的……\n',
            '我完全没有想到呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '喂，基库。\n',
            '悄悄的把信放下后就离开了，\n',
            '是不是有些薄情了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '啾～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#040F嘻嘻……\n',
            '它说『对不起』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0011, 400)

    ChrTalk(
        0x0101,
        (
            '#000F哎呀，没关系的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对了，那些特务兵已经\n',
            '全部解决了吗?',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1941')
    def lambda_1941():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1941)

    ChrTalk(
        0x0011,
        (
            '#170F在离宫这里值勤的部队\n',
            '基本上都被我们控制了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130883V但是在格兰赛尔城内\n',
            '应该还有相当一部分的残党。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_19C0')
    def lambda_19C0():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_19C0)

    ChrTalk(
        0x0010,
        (
            '#020F各地的王国军，至今还\n',
            '处于情报部的掌控之下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '最糟糕的是，他们有可能会以镇压\n',
            '叛军的名义对这里展开进攻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊……\n',
            '我还没有想到这一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '至少让科洛丝\n',
            '先去别的地方避难吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0040130890V#030F如果可能的话，去寻求\n',
            '帝国或共和国大使馆的保护如何？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在大使馆里有治外法权保护……\n',
            '敌人是不会轻举妄动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0081040032V#070F可以用刚才作战所缴获的\n',
            '特务艇作为逃跑的办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130893V虽然不能从根本上解决问题，\n',
            '但可以拖延一些时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0101060024V#170F说得是啊……\n',
            '也只有选择逃亡了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '大家……听我说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1C23')
    def lambda_1C23():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1C23)

    @scena.Lambda('lambda_1C31')
    def lambda_1C31():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1C31)

    @scena.Lambda('lambda_1C3F')
    def lambda_1C3F():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1C3F)

    @scena.Lambda('lambda_1C4D')
    def lambda_1C4D():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1C4D)

    @scena.Lambda('lambda_1C5B')
    def lambda_1C5B():
        ChrTurnDirection(0x00FE, 0x000E, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1C5B)

    ChrSetDirection(0x000E, 135, 400)

    ChrTalk(
        0x000E,
        (
            '#0060940026V在这种状况下，我还可以\n',
            '委托任务给作为游击士的大家吗？',
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
        0x0102,
        (
            '#010F人质救出任务已经\n',
            '完成了。所以应该没有问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130900V当然，要视委托的内容而定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '如果可以……\n',
            '请接受我无理的请求。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0060940027V能够帮助我\n',
            '解放王城并救出陛下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#170F殿、殿下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F对啊……还有女王陛下呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130905V我们一定要把她也救出来啊！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F说实话，我就知道\n',
            '有可能会变成这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，公主殿下……\n',
            '这个委托相当棘手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#020F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030130909V以我们现在的战斗力，就算全员齐聚，\n',
            '也不可能从正面攻入王城的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F如果利用那艘特务艇的话，\n',
            '也不是没有可能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130911V然而，非常充足的\n',
            '准备是行动的必要条件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '……这些我已经考虑过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '各位，你们看这个可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F这个是……哪儿的地图？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '这是记载着王都地下水路\n',
            '内部结构的古代文献。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0060130916V这上面标记出了通往\n',
            '王城地下的隐藏水路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    AddItem(0x0357, 1)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4220._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
