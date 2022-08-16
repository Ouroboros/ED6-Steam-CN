import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4240_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4240   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4240.x'
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
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
        ('ED6_DT07/CH02010._CH', 'ED6_DT07/CH02010P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
        ('ED6_DT07/CH00010._CH', 'ED6_DT07/CH00010P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT07/CH01330._CH', 'ED6_DT07/CH01330P._CP'),
    ]

# id: 0x10001 offset: 0xF2
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
            dword_10            = 3,
            chipIndex           = 3,
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
            dword_10            = 4,
            chipIndex           = 4,
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
            dword_10            = 5,
            chipIndex           = 5,
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
            dword_10            = 6,
            chipIndex           = 6,
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
            x                   = 11510,
            z                   = 0,
            y                   = -154850,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x1B2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1B2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 11510,
            y           = -1000,
            z           = -154850,
            range       = 4000,
            dword_10    = 0x000005DC,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000004,
        ),
    )

# id: 0x10004 offset: 0x1D2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 0,
            triggerZ            = 0,
            triggerY            = -102000,
            triggerRange        = 1000,
            actorX              = 0,
            actorZ              = 1000,
            actorY              = -102000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1F6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_20D',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_02_2AF)

    def _loc_20D(): pass

    label('loc_20D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_224',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_03_494)

    def _loc_224(): pass

    label('loc_224')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_24E',
    )

    ChrSetChipByIndex(0x0000, 0)
    ChrSetChipByIndex(0x0001, 1)
    ChrSetChipByIndex(0x0138, 2)
    ChrSetFlags(0x0000, 0x1000)
    ChrSetFlags(0x0001, 0x1000)
    ChrSetFlags(0x0138, 0x1000)

    def _loc_24E(): pass

    label('loc_24E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            Expr.Return,
        ),
        'loc_25A',
    )

    ChrSetFlags(0x000D, 0x0080)

    def _loc_25A(): pass

    label('loc_25A')

    Return()

# id: 0x0001 offset: 0x25B
@scena.Code('func_01_25B')
def func_01_25B():
    OP_72(0x0000, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 1, 0x661)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_286',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_1B(0x01, 0x00, 0x0005)
    OP_1B(0x03, 0x00, 0x0006)
    OP_6F(0x0000, 120)

    def _loc_286(): pass

    label('loc_286')

    OP_72(0x0001, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 6, 0x666)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 7, 0x667)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2A5',
    )

    OP_64(0x00, 0x0001)
    OP_71(0x0001, 0x0010)
    OP_1C(0x01, 0x00, 0x0008)

    def _loc_2A5(): pass

    label('loc_2A5')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x2AF
@scena.Code('func_02_2AF')
def func_02_2AF():
    EventBegin(0x00)
    CameraMove(9400, 0, -139720, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FormationDelMember(0x00, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationAddMember(0x01, 0xFF)
    FormationAddMember(0x03, 0xFF)
    FormationAddMember(0x07, 0xFF)
    ChrSetPos(0x0102, 14480, -1000, -140500, 270)
    ChrSetPos(0x0104, 14480, -1000, -140500, 270)
    ChrSetPos(0x0108, 14480, -1000, -140500, 270)
    ChrSetFlags(0x000D, 0x0080)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 120)
    OP_73(0x0000)
    OP_6F(0x0000, 120)
    OP_72(0x0000, 0x0010)
    PlayBGM(89)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x59),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x00000800)

    @scena.Lambda('lambda_036B')
    def lambda_036B():
        ChrWalkTo(0x00FE, 10050, 0, -139340, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_036B)

    Sleep(500)

    @scena.Lambda('lambda_038B')
    def lambda_038B():
        ChrWalkTo(0x00FE, 9570, 0, -140380, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_038B)

    Sleep(500)

    @scena.Lambda('lambda_03AB')
    def lambda_03AB():
        ChrWalkTo(0x00FE, 11260, 0, -140020, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_03AB)

    WaitForThreadExit(0x0102, 0x0001)
    ChrSetDirection(0x0102, 180, 400)
    WaitForThreadExit(0x0104, 0x0001)
    ChrSetDirection(0x0104, 90, 400)

    ChrTalk(
        0x0102,
        (
            '#0020131119V#012F城门的开关装置\n',
            '在亲卫队的值勤室里面！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131120V从南侧的楼梯上去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080131121V#076F明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0108, 400)

    ChrTalk(
        0x0104,
        (
            '#0040131122V#035F呵呵，那就走吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00CC, 0, 0x660))
    OP_1B(0x01, 0x00, 0x0005)
    OP_1B(0x03, 0x00, 0x0006)
    EventEnd(0x00)
    MapSetFlags(0x02000000)

    Return()

# id: 0x0003 offset: 0x494
@scena.Code('func_03_494')
def func_03_494():
    EventBegin(0x00)
    CameraMove(50, 0, -115650, 0)
    OP_67(0, 5880, -10000, 0)
    CameraSetDistance(1450, 0)
    OP_6C(41000, 0)
    OP_6E(563, 0)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000A, 0, 0, -103700, 0)
    ChrSetPos(0x0101, -1960, 0, -104120, 83)
    ChrSetPos(0x0008, 1550, 0, -103430, 281)
    ChrSetPos(0x0009, 1310, 0, -104570, 330)
    ChrSetPos(0x0105, 2540, 0, -103830, 273)
    ChrSetPos(0x000B, -460, 0, -105370, 12)
    ChrSetPos(0x000C, 710, 0, -106060, 348)
    ChrSetPos(0x0103, -1580, 0, -105070, 40)
    FadeIn(2000, 0)
    CameraMove(10, 0, -103450, 4000)

    ChrTalk(
        0x000A,
        (
            '#0020131453V#012F#4P果然没错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131454V看得出来，就在最近一段时间，\n',
            '这里有频繁出入的痕迹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030131455V#022F#6P……而且不单如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030131456V还有许多重物运送入内的迹象。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630131457V#094F也许是使用了备用钥匙，\n',
            '然后进去做了些什么吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630131458V#092F嗯，看来有必要进去调查一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, 180, 0, -102540, 2000, 0x00)
    ChrSetDirection(0x0008, 0, 400)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾莉茜雅女王取出了钥匙。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    PlaySE(115, 0x00, 0x64)
    Sleep(1000)

    FadeOut(2000, 0, -1)
    OP_70(0x0001, 60)
    OP_73(0x0001)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4241._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x753
@scena.Code('func_04_753')
def func_04_753():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8C0',
    )

    EventBegin(0x01)
    OP_4A(0x000D, 255)

    If(
        (
            (Expr.Eval, "OP_42(0x0037)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_81E',
    )

    ChrTurnDirection(0x000D, 0x0000, 400)

    ChrTalk(
        0x000D,
        (
            '#4340120525V哦，希尔丹夫人。\n',
            '您在这种地方有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#4340120526V您也是知道的，\n',
            '这里禁止无关人员进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#4340120527V如果没事的话，\n',
            '请快点离开这里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_87A')

    def _loc_81E(): pass

    label('loc_81E')

    ChrTurnDirection(0x000D, 0x0000, 400)

    ChrTalk(
        0x000D,
        (
            '#4340120528V这里禁止入内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#4340120529V可疑人员一律逮捕。\n',
            '请给我注意好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_87A(): pass

    label('loc_87A')

    Fade(1000)
    ChrSetPos(0x0000, 9440, 0, -153980, 270)
    ChrSetPos(0x0001, 9440, 0, -153980, 270)
    ChrSetPos(0x0002, 9440, 0, -153980, 270)
    OP_69(0x0000, 0)
    OP_0D()
    EventEnd(0x01)
    OP_4B(0x000D, 255)

    def _loc_8C0(): pass

    label('loc_8C0')

    Return()

# id: 0x0005 offset: 0x8C1
@scena.Code('func_05_8C1')
def func_05_8C1():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_932',
    )

    ChrTalk(
        0x0102,
        (
            '#0020131123V#012F城门的开关装置\n',
            '在亲卫队的值勤室里面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131124V赶快从南侧的楼梯上去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A59')

    def _loc_932(): pass

    label('loc_932')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9D2',
    )

    ChrTurnDirection(0x0102, 0x0104, 400)

    ChrTalk(
        0x0102,
        (
            '#0020131119V#012F城门的开关装置\n',
            '在亲卫队的值勤室里面！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131120V从南侧的楼梯上去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0102, 400)

    ChrTalk(
        0x0104,
        (
            '#0040131127V#035F呵呵，那就走吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A59')

    def _loc_9D2(): pass

    label('loc_9D2')

    ChrTurnDirection(0x0102, 0x0108, 400)

    ChrTalk(
        0x0102,
        (
            '#0020131119V#012F城门的开关装置\n',
            '在亲卫队的值勤室里面！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131120V从南侧的楼梯上去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0108, 0x0102, 400)

    ChrTalk(
        0x0108,
        (
            '#0080131130V#072F明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A59(): pass

    label('loc_A59')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0006 offset: 0xA75
@scena.Code('func_06_A75')
def func_06_A75():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AE6',
    )

    ChrTalk(
        0x0102,
        (
            '#0020131123V#012F城门的开关装置\n',
            '在亲卫队的值勤室里面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131124V赶快从南侧的楼梯上去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C0D')

    def _loc_AE6(): pass

    label('loc_AE6')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B86',
    )

    ChrTurnDirection(0x0102, 0x0104, 400)

    ChrTalk(
        0x0102,
        (
            '#0020131119V#012F城门的开关装置\n',
            '在亲卫队的值勤室里面！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131120V从南侧的楼梯上去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0102, 400)

    ChrTalk(
        0x0104,
        (
            '#0040131127V#035F呵呵，那就走吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C0D')

    def _loc_B86(): pass

    label('loc_B86')

    ChrTurnDirection(0x0102, 0x0108, 400)

    ChrTalk(
        0x0102,
        (
            '#0020131119V#012F城门的开关装置\n',
            '在亲卫队的值勤室里面！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131120V从南侧的楼梯上去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0108, 0x0102, 400)

    ChrTalk(
        0x0108,
        (
            '#0080131130V#072F明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C0D(): pass

    label('loc_C0D')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0007 offset: 0xC29
@scena.Code('func_07_C29')
def func_07_C29():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门紧紧地关着，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0008 offset: 0xC7D
@scena.Code('func_08_C7D')
def func_08_C7D():
    TalkBegin(0x00FF)
    Sleep(400)

    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
