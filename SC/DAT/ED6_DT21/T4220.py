import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4220_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4220   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4220.x'
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
        ('ED6_DT07/CH02013._CH', 'ED6_DT07/CH02013P._CP'),
        ('ED6_DT07/CH02080._CH', 'ED6_DT07/CH02080P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
        ('ED6_DT27/CH03080._CH', 'ED6_DT27/CH03080P._CP'),
        ('ED6_DT27/CH03670._CH', 'ED6_DT27/CH03670P._CP'),
        ('ED6_DT27/CH03580._CH', 'ED6_DT27/CH03580P._CP'),
        ('ED6_DT07/CH01600._CH', 'ED6_DT07/CH01600P._CP'),
        ('ED6_DT07/CH02010._CH', 'ED6_DT07/CH02010P._CP'),
        ('ED6_DT26/CH20411._CH', 'ED6_DT26/CH20411P._CP'),
        ('ED6_DT26/CH20432._CH', 'ED6_DT26/CH20432P._CP'),
        ('ED6_DT07/CH00041._CH', 'ED6_DT07/CH00041P._CP'),
        ('ED6_DT07/CH00061._CH', 'ED6_DT07/CH00061P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
    ]

# id: 0x10001 offset: 0x13A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '艾莉茜雅女王',
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
            name                = '摩尔根将军',
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
            name                = '雪拉扎德',
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
            name                = '奥利维尔',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '科洛蒂娅公主',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '阿加特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '提妲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            direction           = 0,
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
            name                = '凯文神父',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '卡西乌斯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '尤莉亚上尉',
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
            name                = '王国军士官',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
        ScenaNpcData(
            name                = '希德中校',
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
            name                = '理查德',
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
            name                = '亲卫队队员',
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
            name                = '卡西乌斯',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            name                = '布莉姆',
            x                   = 320,
            z                   = 0,
            y                   = 141880,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 17,
            chipIndex           = 17,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '目标用照相机',
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
    )

# id: 0x10002 offset: 0x39A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x39A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x39A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x39A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_3A9',
    )

    ChrSetFlags(0x0019, 0x0080)

    Jump('loc_3B5')

    def _loc_3A9(): pass

    label('loc_3A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3B5',
    )

    ChrSetFlags(0x0019, 0x0080)

    def _loc_3B5(): pass

    label('loc_3B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_3D4',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x72),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_04_555)

    Jump('loc_3F0')

    def _loc_3D4(): pass

    label('loc_3D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_3F0',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)
    Event(0, func_0F_3F70)

    def _loc_3F0(): pass

    label('loc_3F0')

    Return()

# id: 0x0001 offset: 0x3F1
@scena.Code('func_01_3F1')
def func_01_3F1():
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
        'loc_40D',
    )

    OP_B1('t4220_y')

    Jump('loc_416')

    def _loc_40D(): pass

    label('loc_40D')

    OP_B1('t4220_n')

    def _loc_416(): pass

    label('loc_416')

    Return()

# id: 0x0002 offset: 0x417
@scena.Code('func_02_417')
def func_02_417():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_43A',
    )

    OP_8D(0x00FE, -2480, 144940, 3210, 138830, 2000)

    Jump('func_02_417')

    def _loc_43A(): pass

    label('loc_43A')

    Return()

# id: 0x0003 offset: 0x43B
@scena.Code('func_03_43B')
def func_03_43B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_448',
    )

    Jump('loc_551')

    def _loc_448(): pass

    label('loc_448')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_4FD',
    )

    ChrTalk(
        0x00FE,
        (
            '哼，杜南公爵\n',
            '返回城堡了哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在要塞照顾上校都\n',
            '比现在好上一千倍～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……不过公爵先生\n',
            '不再直直地\n',
            '盯着别人看了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉……不知道是不是因为\n',
            '最近布莉姆发胖了～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_551')

    def _loc_4FD(): pass

    label('loc_4FD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_551',
    )

    ChrTalk(
        0x00FE,
        (
            '公爵去离宫生活之后\n',
            '我可轻松了不少～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为公爵\n',
            '会直直地盯着\n',
            '别人看～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_551(): pass

    label('loc_551')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x555
@scena.Code('func_04_555')
def func_04_555():
    EventBegin(0x00)
    CameraMove(840, 500, 153020, 0)
    OP_67(0, 5330, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(323, 0)
    ChrSetPos(0x0008, 40, 750, 155220, 180)
    ChrSetPos(0x0009, 1350, 500, 153580, 180)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0101, 610, 0, 150320, 0)
    ChrSetPos(0x0102, -590, 0, 150300, 0)
    ChrSetFlags(0x0019, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020340023V#1035F#6P──以上就是我在迄今为止的独自行动中，\n',
            '以及潜入方舟时所掌握到的一切情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600340024V#163F#5P唔……这真令人惊讶。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600340025V想不到会有那种怪物级的飞船\n',
            '侵入了利贝尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600340026V#166F他们拿出那种东西\n',
            '究竟打算干什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340027V#1043F#6P『福音计划』的全貌\n',
            '目前还是无法尽窥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340028V#1042F但他们已经开始\n',
            '下一步行动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340029V#1015F#4P我记得……\n',
            '好像是叫第三阶段。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630340030V#094F#5P现在真是事态紧急呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630340031V#093F摩尔根将军。\n',
            '王国军将有什么应对？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0600340032V#165F#2P这两人昨晚\n',
            '已经联络了卡西乌斯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600340033V在他的指示下，王国军全体\n',
            '已经进入到了一级警戒体制。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600340034V另外还出动了飞行舰队\n',
            '在王国全境进行巡逻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630340035V#090F#5P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 180, 400)

    ChrTalk(
        0x0008,
        (
            '#0630340036V#090F艾丝蒂尔、约修亚。\n',
            '真是有劳你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340037V#1016F#4P不、不不。\n',
            '我们只是做了理所应当的联络而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340038V#1043F#6P说实话……我应该\n',
            '早些联络大家才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340039V包括空贼艇抢夺事件在内，\n',
            '真的是非常抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0101,
        (
            '#0010340040V#1020F#2P等、等等，约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020340041V#1054F#6P没关系，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340042V#1053F我已经有接受\n',
            '制裁的觉悟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0600340043V#166F#2P唔……\n',
            '陛下，您意下如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630340044V#094F#5P嗯……\n',
            '虽然有点超越法规，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630340045V#090F不过这次多亏约修亚向我们提供了\n',
            '有关『结社』的大量情报……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630340046V因此，功过相抵，\n',
            '过去的事情就不用再追究了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0B83')
    def lambda_0B83():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B83)

    Sleep(100)

    ChrSetDirection(0x0102, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010340047V#1018F#4P是、是真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340048V#1042F#6P可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    ChrSetPos(0x0008, 10, 500, 154550, 180)
    ChrSetChipByIndex(0x0008, 12)
    ChrSetSubChip(0x0008, 0)
    OP_0D()

    @scena.Lambda('lambda_0C11')
    def lambda_0C11():
        CameraMove(840, 500, 152500, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0C11)

    @scena.Lambda('lambda_0C29')
    def lambda_0C29():
        ChrMoveTo(0x00FE, -10, 500, 152360, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0C29)

    Sleep(500)

    @scena.Lambda('lambda_0C49')
    def lambda_0C49():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0C49')

    DispatchAsync2(0x0009, 0x0001, lambda_0C49)

    WaitForThreadExit(0x0008, 0x0001)
    TerminateThread(0x0009, 0x01)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0630340049V#090F#5P没关系的，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630340050V#094F这样的裁决……\n',
            '还不足以弥补你这位『哈梅尔』\n',
            '遗孤所经受之痛苦的万分之一啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340051V#1004F#4P啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340052V#1043F#6P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630340053V#094F#5P……看来你\n',
            '早已知道了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630340054V#093F我虽然\n',
            '了解那次虐杀事件的真相，\n',
            '但却至今保持着沉默……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010340055V#1020F#4P啊！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340056V这、这是怎么回事！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0009, -180, 400)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0600340057V#166F#5P战争开始时，埃雷波尼亚向\n',
            '利贝尔发来了宣战公告……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600340058V他们坚决指称哈梅尔村\n',
            '发生的大屠杀\n',
            '是王国军所为。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600340059V#163F但战争临近结束前，帝国政府\n',
            '却突然撤回了那项指控，\n',
            '并提出了即刻停战的要求。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0600340060V#160F……而他们的条件，就是\n',
            '要我们对哈梅尔事件永远保持沉默。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340061V#1020F#4P#3S！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630340062V#094F#5P……我分析了事情的前因后果，\n',
            '大概可以想象得到在帝国内部\n',
            '发生了怎样的事态。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630340063V#093F反攻作战虽然取得了成功，\n',
            '但帝国军仍然保有相当的兵力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630340064V如果他们从帝国本土派来增援的话，\n',
            '王国必定将会再次陷入困境──',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630340065V#094F在这样的考虑下……\n',
            '最终我决定接受了那个条件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340066V#1026F#4P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340052V#1043F#6P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630340068V#092F#5P……我为了本国的安宁\n',
            '而放弃了对真相的追究。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630340069V背叛了那些无辜的受害者，\n',
            '没能为他们平息惨死的怨念。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630340070V#094F那个时候，洛伦斯少尉曾对我说过：\n',
            '『你没有怜悯我的资格』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630340071V那话真的是一针见血啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340072V#1026F#4P女王陛下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340073V#1035F#6P……请您\n',
            '不要再自责了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340074V#1040F那次虐杀事件与您完全无关，\n',
            '而且您身为一国之主，将国家的和平',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340075V摆在首位本就是最合理的决定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#0630340076V#093F#5P约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340077V#1053F#6P这个叫做利贝尔的国家\n',
            '使我这颗被冰封的心得到了温暖、痊愈，\n',
            '可以说是我的第二故乡。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340078V#1040F全靠陛下的决断，这片土地才能获得安宁，\n',
            '对此我只有感谢，又何来怨恨呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340079V#1025F#2P约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630340080V#096F#5P谢谢你……约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630340081V听你这么一说，\n',
            '我长年以来的愧疚终于稍有减轻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x000C, 520, 0, 138480, 0)
    ChrSetPos(0x000E, -850, 0, 138320, 0)
    ChrSetPos(0x000A, -2560, 0, 137730, 0)
    ChrSetPos(0x000D, -2280, 0, 136550, 0)
    ChrSetPos(0x000B, 1570, 0, 138000, 0)
    ChrSetPos(0x000F, 2440, 0, 137650, 0)
    Sleep(500)

    NpcTalk(
        0x000C,
        '女孩的声音',
        (
            '#0060340082V#1P艾丝蒂尔、约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_152E')
    def lambda_152E():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_152E)

    Sleep(100)

    ChrSetDirection(0x0102, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010340083V#1004F#5P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340084V#1044F#5P大家……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_158E')
    def lambda_158E():
        CameraMove(1130, 0, 150940, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_158E)

    @scena.Lambda('lambda_15A6')
    def lambda_15A6():
        OP_67(0, 5380, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_15A6)

    @scena.Lambda('lambda_15BE')
    def lambda_15BE():
        CameraSetDistance(2770, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_15BE)

    @scena.Lambda('lambda_15CE')
    def lambda_15CE():
        OP_6E(344, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_15CE)

    CreateThread(0x000C, 0x00, 0x00, func_06_3E1F)
    Sleep(300)

    CreateThread(0x000E, 0x00, 0x00, func_07_3E4A)
    Sleep(300)

    CreateThread(0x000A, 0x00, 0x00, func_08_3E75)
    Sleep(300)

    CreateThread(0x000D, 0x00, 0x00, func_09_3E96)
    Sleep(300)

    CreateThread(0x000B, 0x00, 0x00, func_0A_3EB7)
    Sleep(300)

    CreateThread(0x000F, 0x00, 0x00, func_0B_3ED8)
    WaitForThreadExit(0x000C, 0x0000)
    Sleep(500)

    NpcTalk(
        0x000C,
        '科洛丝',
        (
            '#0060340085V#041F#4P艾丝蒂尔！你没事真是太好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060340086V#048F还有……约修亚也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000E, 0x0000)

    ChrTalk(
        0x000E,
        (
            '#0070340087V#067F#6P太、太好了……\n',
            '两个人一起平安归来……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340088V#1054F#5P科洛丝、提妲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340089V#1025F#5P我让你们……\n',
            '担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000A, 0x0000)

    ChrTalk(
        0x000A,
        (
            '#0030340090V#027F#6P真是的……\n',
            '你还真会让人担惊受怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0050340091V#051F#6P嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050340092V不过能把这个离家出走的坏孩子\n',
            '顺利抓回来就比什么都好啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340093V#1040F#5P雪拉姐、阿加特……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000F, 0x0000)

    ChrTalk(
        0x000F,
        (
            '#0080340094V#070F#4P两个人全都……\n',
            '平安回来了啊…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040340095V#031F#2P呵呵，这也是\n',
            '女神的引导吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340096V#1016F#5P嘿嘿……\n',
            '抱歉，让大家担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0010, 40, 0, 140750, 0)

    NpcTalk(
        0x0010,
        '青年的声音',
        (
            '#0180340097V#1P一点也没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_18EC')
    def lambda_18EC():
        CameraMove(1130, 0, 150500, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_18EC)

    @scena.Lambda('lambda_1904')
    def lambda_1904():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_1904')

    DispatchAsync2(0x000B, 0x0001, lambda_1904)

    @scena.Lambda('lambda_1915')
    def lambda_1915():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_1915')

    DispatchAsync2(0x000F, 0x0001, lambda_1915)

    Sleep(50)

    @scena.Lambda('lambda_192B')
    def lambda_192B():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_192B')

    DispatchAsync2(0x000A, 0x0001, lambda_192B)

    @scena.Lambda('lambda_193C')
    def lambda_193C():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_193C')

    DispatchAsync2(0x000D, 0x0001, lambda_193C)

    Sleep(50)

    @scena.Lambda('lambda_1952')
    def lambda_1952():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1952)

    @scena.Lambda('lambda_1960')
    def lambda_1960():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1960)

    Sleep(50)

    @scena.Lambda('lambda_1973')
    def lambda_1973():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1973)

    ChrSetDirection(0x0101, 180, 400)
    ChrClearFlags(0x0010, 0x0080)

    @scena.Lambda('lambda_198D')
    def lambda_198D():
        ChrWalkTo(0x0010, -320, 0, 148480, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0000, lambda_198D)

    Sleep(500)

    CreateThread(0x000C, 0x00, 0x00, func_0D_3F1A)
    Sleep(100)

    CreateThread(0x000E, 0x00, 0x00, func_0E_3F45)
    WaitForThreadExit(0x0010, 0x0000)
    WaitForThreadExit(0x000C, 0x0000)
    WaitForThreadExit(0x000E, 0x0000)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000F, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000D, 0x01)
    TerminateThread(0x000E, 0x01)
    TerminateThread(0x000C, 0x01)

    @scena.Lambda('lambda_19E7')
    def lambda_19E7():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_19E7)

    @scena.Lambda('lambda_19F5')
    def lambda_19F5():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_19F5)

    Sleep(50)

    @scena.Lambda('lambda_1A08')
    def lambda_1A08():
        ChrSetDirection(0x00FE, 45, 400)
        Yield()

        Jump('lambda_1A08')

    DispatchAsync2(0x000A, 0x0001, lambda_1A08)

    @scena.Lambda('lambda_1A19')
    def lambda_1A19():
        ChrSetDirection(0x00FE, 45, 400)
        Yield()

        Jump('lambda_1A19')

    DispatchAsync2(0x000D, 0x0001, lambda_1A19)

    Sleep(50)

    @scena.Lambda('lambda_1A2F')
    def lambda_1A2F():
        ChrSetDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1A2F)

    @scena.Lambda('lambda_1A3D')
    def lambda_1A3D():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1A3D)

    ChrTalk(
        0x0101,
        (
            '#0010340098V#1004F#5P啊，凯文先生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0010, 0x0000)

    ChrTalk(
        0x0010,
        (
            '#0180340099V#1068F#4P艾丝蒂尔被掳走时，\n',
            '我真是眼前一片漆黑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340100V#1060F真是的……\n',
            '不要这么吓唬人嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340101V#1025F#5P嗯……对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0180340102V#1062F#4P那这位就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340103V#1040F#5P初次见面，凯文神父。\n',
            '我是约修亚·布莱特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0180340104V#1068F#4P哇……\n',
            '比想象中还英俊的美男子呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340105V#1064F嗯？你知道我？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340106V#1053F#5P有关你的存在，\n',
            '早已被收录到了我的情报网中。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340107V艾丝蒂尔数次陷入险境，\n',
            '全都是靠你出手相救。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340108V#1040F真是……非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0180340109V#1065F#4P嗯嗯……这没什么啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340110V#1060F既然你们已经重归于好，\n',
            '那我也就没什么可说的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340111V#1063F不过呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1D15')
    def lambda_1D15():
        CameraMove(840, 0, 151500, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1D15)

    @scena.Lambda('lambda_1D2D')
    def lambda_1D2D():
        CameraSetDistance(2700, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1D2D)

    @scena.Lambda('lambda_1D3D')
    def lambda_1D3D():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_1D3D')

    DispatchAsync2(0x0101, 0x0001, lambda_1D3D)

    @scena.Lambda('lambda_1D4E')
    def lambda_1D4E():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_1D4E')

    DispatchAsync2(0x000C, 0x0001, lambda_1D4E)

    @scena.Lambda('lambda_1D5F')
    def lambda_1D5F():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_1D5F')

    DispatchAsync2(0x000F, 0x0001, lambda_1D5F)

    ChrSetFlags(0x0010, 0x0040)
    ChrMoveTo(0x0010, -1040, 0, 149590, 1500, 0x00)
    ChrSetDirection(0x0010, 0, 400)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)

    @scena.Lambda('lambda_1D98')
    def lambda_1D98():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1D98)

    Sleep(100)

    ChrSetDirection(0x0101, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0010,
        (
            '#0180340112V#1066F#4P（……以后可不能再把\n',
            '这么可爱的女朋友扔下不管了哦。)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180340113V(如果不想被我这样的害虫\n',
            '趁虚而入的话。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340114V#1054F#5P（…………我会铭记在心的。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340115V#1004F#2P？　怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0010, 90, 400)

    ChrTalk(
        0x0010,
        (
            '#0180340116V#1061F#6P呀～没什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020340117V#1049F#6P是男人之间的对话呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340118V#1019F#2P感觉你们没说什么好话啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x000C, 0x01)
    TerminateThread(0x000F, 0x01)
    Sleep(500)

    ChrSetPos(0x0011, 40, 0, 140750, 0)

    NpcTalk(
        0x0011,
        '男性的声音',
        (
            '#0160340119V#1P失礼了，陛下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrClearFlags(0x0011, 0x0080)
    Sleep(1000)

    @scena.Lambda('lambda_1FBF')
    def lambda_1FBF():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_1FBF')

    DispatchAsync2(0x000B, 0x0001, lambda_1FBF)

    @scena.Lambda('lambda_1FD0')
    def lambda_1FD0():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_1FD0')

    DispatchAsync2(0x000F, 0x0001, lambda_1FD0)

    Sleep(50)

    @scena.Lambda('lambda_1FE6')
    def lambda_1FE6():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_1FE6')

    DispatchAsync2(0x000A, 0x0001, lambda_1FE6)

    @scena.Lambda('lambda_1FF7')
    def lambda_1FF7():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_1FF7')

    DispatchAsync2(0x000D, 0x0001, lambda_1FF7)

    Sleep(50)

    @scena.Lambda('lambda_200D')
    def lambda_200D():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_200D')

    DispatchAsync2(0x000E, 0x0001, lambda_200D)

    @scena.Lambda('lambda_201E')
    def lambda_201E():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_201E')

    DispatchAsync2(0x000C, 0x0001, lambda_201E)

    Sleep(50)

    @scena.Lambda('lambda_2034')
    def lambda_2034():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2034)

    @scena.Lambda('lambda_2042')
    def lambda_2042():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_2042)

    Sleep(50)

    ChrTurnDirection(0x0101, 0x0011, 400)

    @scena.Lambda('lambda_205C')
    def lambda_205C():
        CameraMove(960, 0, 151060, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_205C)

    @scena.Lambda('lambda_2074')
    def lambda_2074():
        CameraSetDistance(2800, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2074)

    @scena.Lambda('lambda_2084')
    def lambda_2084():
        ChrWalkTo(0x0011, -740, 0, 146000, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0000, lambda_2084)

    WaitForThreadExit(0x0010, 0x0001)
    Sleep(1000)

    CreateThread(0x0010, 0x00, 0x00, func_0C_3EF9)
    WaitForThreadExit(0x0011, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010340120V#1025F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340121V#1044F#5P父亲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630340122V#090F#5P卡西乌斯先生，辛苦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600340123V#165F#5P对各方面的指示都下达了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160340124V#1125F#4P嗯，刚刚完成我就\n',
            '马上赶来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160340125V#1120F那么，我首先要稍尽一点\n',
            '身为父亲的义务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340126V#1004F#5P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_21F3')
    def lambda_21F3():
        CameraMove(1130, 0, 151500, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_21F3)

    @scena.Lambda('lambda_220B')
    def lambda_220B():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_220B')

    DispatchAsync2(0x0101, 0x0001, lambda_220B)

    ChrWalkTo(0x0011, -450, 0, 149660, 1500, 0x00)
    Sleep(500)

    ChrTalk(
        0x0011,
        (
            '#0160340127V#1120F#4P……虽然昨天进行过通讯，\n',
            '但已经好久没有这么面对面地谈话了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340128V#1035F#5P嗯……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340129V#1043F……对不起。\n',
            '让您担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160340130V#1125F#4P你早就向我坦白过一切，\n',
            '所以从某种意义上说，我也算是共犯吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160340131V#1122F虽然你没有道歉的必要……\n',
            '但我却必须履行自己的义务！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)

    @scena.Lambda('lambda_2383')
    def lambda_2383():
        CameraSetDistance(2600, 1000)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_2383)

    Sleep(600)

    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x000C, 0x01)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x000F, 0x01)
    TerminateThread(0x000D, 0x01)
    TerminateThread(0x000E, 0x01)
    Fade(500)
    ChrSetPos(0x0011, -580, 0, 150280, 0)
    ChrSetPos(0x0018, -450, 0, 149780, 0)
    ChrSetPos(0x0102, -590, 0, 150200, 180)
    ChrSetFlags(0x0011, 0x0002)
    ChrSetSubChip(0x0011, 24)
    ChrSetChipByIndex(0x0011, 13)
    ChrSetFlags(0x0102, 0x0002)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 13)
    ChrSetFlags(0x0102, 0x0040)
    OP_0D()

    @scena.Lambda('lambda_2410')
    def lambda_2410():
        OP_99(0x0102, 0x00, 0x0A, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_2410)

    @scena.Lambda('lambda_2420')
    def lambda_2420():
        OP_99(0x0011, 0x18, 0x27, 2000)

        ExitThread()

    DispatchAsync(0x0011, 0x0000, lambda_2420)

    Sleep(300)

    PlaySE(165, 0x00, 0x64)
    WaitForThreadExit(0x0102, 0x0000)
    WaitForThreadExit(0x0011, 0x0000)

    ChrTalk(
        0x000E,
        (
            '#0070340132V#065F#6P……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '科洛丝',
        (
            '#0060340133V#043F#2P呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340134V#1020F#2P等、等等，老爸！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340135V#1035F#5P……没关系，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0102, 0x0B, 0x0F, 1500)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020340136V#1040F#5P对一个离家出走的儿子来说……\n',
            '这也是该有的惩罚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0018,
        '卡西乌斯',
        (
            '#0160340137V#1125F#4P没错，知道就好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160340138V#1120F你给大家带来的忧虑和麻烦\n',
            '比你自己想象中的更要严重……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160340139V如今已经深刻体会到了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340140V#1043F#5P……嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340141V#1035F我一直以为自己这种人根本不值得──\n',
            '现在看来，这种想法果然是错的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0018,
        '卡西乌斯',
        (
            '#0160340142V#1122F#4P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160340143V#1125F人类的一生，会受到\n',
            '无数人的影响。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160340144V反过来说，也会对自己周围\n',
            '的人们造成各种影响。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160340145V这就是『缘』──\n',
            '『缘』在不断加深之后，就成为了『羁绊』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340146V#1044F#5P……『羁绊』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0018,
        '卡西乌斯',
        (
            '#0160340147V#1120F#4P而『羁绊』一旦形成，\n',
            '就绝不可能割断。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160340148V既使相隔千里，或是立场相悖，\n',
            '也都会以某种形式永存在我们的心中……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160340149V#1121F它的力量之强，你已经明白了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340150V#1054F#5P嗯……我真是太轻视它了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340151V#1053F之前的我……\n',
            '浑浑噩噩，什么都没看清呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340152V#1025F#2P约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0018,
        '卡西乌斯',
        (
            '#0160340153V#1120F#4P呵呵，你能理解这一点，\n',
            '这次离家出走也算没有白费。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetPos(0x0011, -580, 0, 150130, 0)
    ChrSetPos(0x0018, -530, 0, 149780, 0)

    @scena.Lambda('lambda_293F')
    def lambda_293F():
        OP_99(0x0102, 0x10, 0x14, 1000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_293F)

    @scena.Lambda('lambda_294F')
    def lambda_294F():
        OP_99(0x0011, 0x28, 0x2C, 1000)

        ExitThread()

    DispatchAsync(0x0011, 0x0000, lambda_294F)

    WaitForThreadExit(0x0102, 0x0000)
    WaitForThreadExit(0x0011, 0x0000)
    Sleep(1000)

    NpcTalk(
        0x0018,
        '卡西乌斯',
        (
            '#0160340154V#1125F#4P约修亚……\n',
            '我的笨蛋儿子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160340155V你总算回来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340156V#1043F#5P父亲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340157V#1008F#2P呵……呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600340158V#165F#5P嘿，这对傻瓜父子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630340159V#091F#5P呵呵……真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0012, -40, 0, 138750, 0)

    NpcTalk(
        0x0012,
        '女性的声音',
        (
            '#0100340160V#1P报告！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000F, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000E, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0018, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0109, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_2BDA')
    def lambda_2BDA():
        CameraSetDistance(2800, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2BDA)

    @scena.Lambda('lambda_2BEA')
    def lambda_2BEA():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_2BEA')

    DispatchAsync2(0x000B, 0x0001, lambda_2BEA)

    @scena.Lambda('lambda_2BFB')
    def lambda_2BFB():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_2BFB')

    DispatchAsync2(0x000F, 0x0001, lambda_2BFB)

    Sleep(50)

    @scena.Lambda('lambda_2C11')
    def lambda_2C11():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_2C11')

    DispatchAsync2(0x000A, 0x0001, lambda_2C11)

    @scena.Lambda('lambda_2C22')
    def lambda_2C22():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_2C22')

    DispatchAsync2(0x000D, 0x0001, lambda_2C22)

    Sleep(50)

    @scena.Lambda('lambda_2C38')
    def lambda_2C38():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_2C38')

    DispatchAsync2(0x000C, 0x0001, lambda_2C38)

    @scena.Lambda('lambda_2C49')
    def lambda_2C49():
        ChrTurnDirection(0x00FE, 0x0012, 400)
        Yield()

        Jump('lambda_2C49')

    DispatchAsync2(0x000E, 0x0001, lambda_2C49)

    Sleep(50)

    @scena.Lambda('lambda_2C5F')
    def lambda_2C5F():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2C5F)

    @scena.Lambda('lambda_2C6D')
    def lambda_2C6D():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_2C6D)

    Fade(250)
    CreateThread(0x0011, 0x01, 0x00, func_05_3DD9)
    ChrClearFlags(0x0102, 0x0002)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetSubChip(0x0102, 0)
    OP_0D()

    @scena.Lambda('lambda_2C97')
    def lambda_2C97():
        CameraMove(1390, 0, 150800, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2C97)

    ChrClearFlags(0x0012, 0x0080)
    ChrWalkTo(0x0012, -450, 0, 147000, 4000, 0x00)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x000B, 0x01)
    TerminateThread(0x000F, 0x01)
    TerminateThread(0x000A, 0x01)

    ChrTalk(
        0x0008,
        (
            '#0630340161V#097F#5P尤莉亚上尉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlayBGM(35)
    Sleep(500)

    ChrTalk(
        0x0012,
        (
            '#0100340162V#172F#4P包括王都在内的五大都市的近郊\n',
            '全都出现了不明真身的魔兽群！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340163V从报告判断，\n',
            '看来是人形兵器！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340164V#1005F#5P你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340165V#1042F#5P终于出动了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0100340166V#172F#4P另外，各地的关所\n',
            '都出现了装甲魔兽群和\n',
            '红衣士兵！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340167V现在各守备队\n',
            '正在迎击！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160340168V#1125F#5P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600340169V#160F#5P看来我得尽快赶回\n',
            '哈肯大门……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0100340170V#175F而、而且……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600340171V#161F#5P什么？还有？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0100340172V#178F虽然详情不明……\n',
            '在『四轮之塔』上发生了非常事件。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340173V好像一股未知的『黑暗』\n',
            '包围在塔顶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340174V#1020F#5P！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0180340175V#1063F#5P哼……\n',
            '看来我那不祥的预感成真了',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0100340176V#178F另外，巡逻中的警备艇\n',
            '虽然试图接近调查……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100340177V可立即陷入了机能停止状态，\n',
            '因此不得不撤离现场。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0600340178V#160F#5P是『导力停止现象』吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160340179V#1122F#5P地面的侦察部队呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0100340180V#175F应该已经被派遣过去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0013, 70, 0, 136750, 0)
    ChrClearFlags(0x0013, 0x0080)

    NpcTalk(
        0x0013,
        '男人的声音',
        (
            '#2440340181V#1P报、报告！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0012, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000F, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000E, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0011, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0109, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_3257')
    def lambda_3257():
        CameraMove(1350, 0, 150430, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_3257)

    @scena.Lambda('lambda_326F')
    def lambda_326F():
        CameraSetDistance(2900, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_326F)

    @scena.Lambda('lambda_327F')
    def lambda_327F():
        ChrTurnDirection(0x00FE, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_327F)

    @scena.Lambda('lambda_328D')
    def lambda_328D():
        ChrTurnDirection(0x00FE, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_328D)

    Sleep(50)

    @scena.Lambda('lambda_32A0')
    def lambda_32A0():
        ChrTurnDirection(0x00FE, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_32A0)

    @scena.Lambda('lambda_32AE')
    def lambda_32AE():
        ChrTurnDirection(0x00FE, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_32AE)

    Sleep(50)

    @scena.Lambda('lambda_32C1')
    def lambda_32C1():
        ChrTurnDirection(0x00FE, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_32C1)

    @scena.Lambda('lambda_32CF')
    def lambda_32CF():
        ChrTurnDirection(0x00FE, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_32CF)

    Sleep(50)

    @scena.Lambda('lambda_32E2')
    def lambda_32E2():
        ChrTurnDirection(0x00FE, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_32E2)

    @scena.Lambda('lambda_32F0')
    def lambda_32F0():
        ChrTurnDirection(0x00FE, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_32F0)

    @scena.Lambda('lambda_32FE')
    def lambda_32FE():
        ChrTurnDirection(0x00FE, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_32FE)

    ChrWalkTo(0x0013, -200, 0, 145000, 4000, 0x00)

    ChrTalk(
        0x0013,
        (
            '#2440340182V#4P被派往各塔的侦察部队\n',
            '全部被击退了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#2440340183V#4P实、实在是难以置信！\n',
            '似乎每支部队都是\n',
            '被一个敌人给彻底打败的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0100340184V#173F#5P什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340185V#1005F#5P难、难道……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340186V#1035F#5P嗯……\n',
            '应该是『执行者』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340187V#1042F父亲……\n',
            '他们非普通士兵能敌。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340188V请让我去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_347B')
    def lambda_347B():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_347B)

    @scena.Lambda('lambda_3489')
    def lambda_3489():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3489)

    Sleep(50)

    @scena.Lambda('lambda_349C')
    def lambda_349C():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_349C)

    @scena.Lambda('lambda_34AA')
    def lambda_34AA():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_34AA)

    Sleep(50)

    @scena.Lambda('lambda_34BD')
    def lambda_34BD():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_34BD)

    @scena.Lambda('lambda_34CB')
    def lambda_34CB():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_34CB)

    Sleep(50)

    @scena.Lambda('lambda_34DE')
    def lambda_34DE():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_34DE)

    @scena.Lambda('lambda_34EC')
    def lambda_34EC():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_34EC)

    Sleep(50)

    @scena.Lambda('lambda_34FF')
    def lambda_34FF():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_34FF)

    ChrTurnDirection(0x0012, 0x0102, 400)
    Sleep(200)

    ChrTalk(
        0x0011,
        (
            '#0160340189V#1125F#4P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340190V#1009F#2P等等，约修亚……\n',
            '你又想单独行动了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340191V这么快就忘了昨天的约定？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020340192V#1043F#6P艾丝蒂尔，可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010340193V#1006F#2P既然『结社』已经出动，\n',
            '身为游击士也不能放任不管。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010340194V我一定要跟你去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020331089V#1044F#6P艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030340196V#020F#6P不光是艾丝蒂尔，\n',
            '我也要和你们一起去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030340197V毕竟我也有些个人恩怨要了结呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0080340198V#070F嗯，我也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020340199V#1044F#5P雪拉姐、金先生……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0050340200V#051F#6P好啦，这本来也不是\n',
            '你一个人的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050340201V可别抢着一个人立功。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0070340202V#560F#6P没、没错啊哥哥！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070340203V#061F在这种时候，\n',
            '才更需要大家齐心协力啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 225, 400)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020340204V#1054F#5P阿加特、提妲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020340205V#1053F……谢谢，你们真是帮了我大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0160340206V#1125F#4P看来你们已经决定好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160340207V#1122F我向游击士协会提出请求。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160340208V拜托你们调查并解决\n',
            '『四轮之塔』所发生的异变。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160340209V这是来自军队的正式委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 225, 400)

    @scena.Lambda('lambda_391D')
    def lambda_391D():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_391D)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010340210V#1006F#5P嗯……明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020340211V#1042F#5P我们正式接受此委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x000C)
    ChrSetDirection(0x000C, 0, 400)
    Sleep(500)

    NpcTalk(
        0x000C,
        '科洛丝',
        (
            '#0060340212V#042F#4P……祖母大人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060340213V能不能把『埃尔赛尤』\n',
            '借给我？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010340214V#1004F#5P咦……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0012, 0x000C, 400)

    @scena.Lambda('lambda_3A3B')
    def lambda_3A3B():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_3A3B)

    @scena.Lambda('lambda_3A49')
    def lambda_3A49():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3A49)

    ChrTalk(
        0x0012,
        (
            '#0100340215V#173F#6P殿、殿下？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630340216V#094F#5P呵呵……\n',
            '现在确实情况紧急。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630340217V我也正准备提供\n',
            '『埃尔赛尤』给你们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630340218V#090F你既然提出这个要求，\n',
            '就是说你已经有精神准备了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '科洛丝',
        (
            '#0060340219V#049F#4P不……还没有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060340220V#042F但是，当我将船归还给您的时候\n',
            '一定会有答案的，我保证。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630340221V#090F#5P呵呵……好吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630340222V#091F利贝尔的希望之翼，\n',
            '请你们任意使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '科洛丝',
        (
            '#0060340223V#048F#4P非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0012, 400)
    Sleep(500)

    NpcTalk(
        0x000C,
        '科洛丝',
        (
            '#0060340224V#042F#5P尤莉亚上尉，请做出发的准备。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060340225V我们要尽快\n',
            '前往『四轮之塔』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0100340226V#171F#6P遵命！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '就这样……\n',
            '利贝尔迎来了『百日战役』之后未曾有过的事态。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '为了指挥王国军的所有部队，\n',
            '卡西乌斯和摩尔根将军各自\n',
            '返回了雷斯顿要塞和哈肯大门……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔一行乘坐着『埃尔赛尤』，\n',
            '出发前往各座塔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_28(0x0098, 0x04, 0x10)
    OP_AF(0xCD, 0x0098)
    Sleep(100)

    OP_28(0x0099, 0x04, 0x10)
    OP_28(0x0099, 0x04, 0x20)
    NewScene('ED6_DT21/T4106._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x3DD9
@scena.Code('func_05_3DD9')
def func_05_3DD9():
    ChrSetPos(0x0011, -450, 0, 149660, 0)
    ChrClearFlags(0x0011, 0x8000)
    ChrClearFlags(0x0011, 0x0800)
    ChrClearFlags(0x00FE, 0x0002)
    ChrSetChipByIndex(0x00FE, 9)
    ChrSetSubChip(0x00FE, 0)
    ChrSetDirection(0x00FE, 180, 400)
    ChrMoveTo(0x00FE, -450, 0, 148800, 1000, 0x00)

    Return()

# id: 0x0006 offset: 0x3E1F
@scena.Code('func_06_3E1F')
def func_06_3E1F():
    ChrSetChipByIndex(0x00FE, 15)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 180, 0, 148140, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 4)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0007 offset: 0x3E4A
@scena.Code('func_07_3E4A')
def func_07_3E4A():
    ChrSetChipByIndex(0x00FE, 16)
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -920, 0, 148100, 5000, 0x00)
    ChrSetChipByIndex(0x00FE, 6)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x0008 offset: 0x3E75
@scena.Code('func_08_3E75')
def func_08_3E75():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -2720, 0, 148860, 3000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)

    Return()

# id: 0x0009 offset: 0x3E96
@scena.Code('func_09_3E96')
def func_09_3E96():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -2640, 0, 147270, 3000, 0x00)
    ChrSetDirection(0x00FE, 45, 400)

    Return()

# id: 0x000A offset: 0x3EB7
@scena.Code('func_0A_3EB7')
def func_0A_3EB7():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 2300, 0, 149090, 3000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x000B offset: 0x3ED8
@scena.Code('func_0B_3ED8')
def func_0B_3ED8():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, 920, 0, 147360, 3000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000C offset: 0x3EF9
@scena.Code('func_0C_3EF9')
def func_0C_3EF9():
    ChrClearFlags(0x00FE, 0x0080)
    ChrWalkTo(0x00FE, -1580, 0, 150640, 1000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x000D offset: 0x3F1A
@scena.Code('func_0D_3F1A')
def func_0D_3F1A():
    ChrClearFlags(0x00FE, 0x0080)
    ChrMoveTo(0x00FE, 900, 0, 148590, 1000, 0x00)

    @scena.Lambda('lambda_3F39')
    def lambda_3F39():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_3F39')

    DispatchAsync2(0x00FE, 0x0001, lambda_3F39)

    Return()

# id: 0x000E offset: 0x3F45
@scena.Code('func_0E_3F45')
def func_0E_3F45():
    ChrClearFlags(0x00FE, 0x0080)
    ChrMoveTo(0x00FE, -1980, 0, 148530, 1000, 0x00)

    @scena.Lambda('lambda_3F64')
    def lambda_3F64():
        ChrTurnDirection(0x00FE, 0x0010, 400)
        Yield()

        Jump('lambda_3F64')

    DispatchAsync2(0x00FE, 0x0001, lambda_3F64)

    Return()

# id: 0x000F offset: 0x3F70
@scena.Code('func_0F_3F70')
def func_0F_3F70():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(830, 0, 138280, 0)
    OP_67(0, 8039, -10000, 0)
    CameraSetDistance(2350, 0)
    OP_6C(44000, 0)
    OP_6E(488, 0)
    LoadChip('ED6_DT07/CH02010._CH', 'ED6_DT07/CH02010P._CP', 18)
    LoadChip('ED6_DT06/CH20143._CH', 'ED6_DT06/CH20143P._CP', 19)
    LoadChip('ED6_DT27/CH03590._CH', 'ED6_DT27/CH03590P._CP', 20)
    LoadChip('ED6_DT27/CH03110._CH', 'ED6_DT27/CH03110P._CP', 21)
    LoadChip('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP', 22)
    LoadChip('ED6_DT07/CH02323._CH', 'ED6_DT07/CH02323P._CP', 23)
    ChrSetChipByIndex(0x0008, 18)
    ChrSetChipByIndex(0x000C, 19)
    ChrSetChipByIndex(0x0015, 20)
    ChrSetChipByIndex(0x0016, 21)
    ChrSetChipByIndex(0x0017, 22)
    ChrSetChipByIndex(0x0014, 23)
    ChrClearFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, -90, 0, 150140, 180)
    ChrSetPos(0x0014, 3790, 800, 152270, 270)
    ChrSetPos(0x000C, -1510, 0, 148970, 180)
    ChrSetPos(0x0015, 1650, 0, 148500, 180)
    ChrSetPos(0x0016, 560, 0, 148300, 180)
    ChrSetPos(0x0101, -360, 0, 145930, 0)
    ChrSetPos(0x0102, 790, 0, 145890, 0)
    ChrSetPos(0x000A, 740, 0, 144730, 0)
    ChrSetPos(0x000D, -800, 0, 143680, 0)
    ChrSetPos(0x000E, -1250, 0, 144610, 0)
    ChrSetPos(0x000F, 1230, 0, 143850, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x0015, 0x0080)
    ChrClearFlags(0x0016, 0x0080)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0102, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)
    ChrClearFlags(0x000F, 0x0080)
    ChrClearFlags(0x0014, 0x0080)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_4123')
    def lambda_4123():
        CameraMove(290, 0, 147230, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4123)

    @scena.Lambda('lambda_413B')
    def lambda_413B():
        OP_67(0, 7500, -10000, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_413B)

    WaitForThreadExit(0x0101, 0x0001)
    Fade(500)
    CameraMove(1500, 0, 147770, 0)
    OP_67(0, 5140, -10000, 0)
    CameraSetDistance(2200, 0)
    OP_6C(44000, 0)
    OP_6E(433, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0015,
        (
            '#0620380512V#700F#5P就像我前面所说，\n',
            '这都是卡西乌斯准将的指示。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620380513V他事先就知道了\n',
            '王都会迎来危机。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620380514V#703F所以，想到以导力兵器为主武器的\n',
            '正规军是守不住的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620380515V#701F就决定投入白刃战经验\n',
            '丰富的特务兵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0130380516V#115F#5P当然，必须要有一个理由\n',
            '来让服刑中的我们投入战斗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130380517V#111F所以故意让我们在被\n',
            '押往王城的途中卷入这次骚乱，\n',
            '结果成功保卫了城市。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380518V#1007F#6P原，原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380519V#1019F虽然我怎么想都\n',
            '觉得说不通。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380520V#1040F好像陛下你们\n',
            '是知道的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630380521V#090F#5P嗯，关于这件事\n',
            '卡西乌斯先生事先跟我说过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630380522V虽然接下来可能会有很多\n',
            '批判的声音，\n',
            '但是，国民的安全是无可替代的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630380523V#091F最重要的是，我相信\n',
            '理查德先生的爱国心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0130380524V#115F#6P……您太抬举我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380525V#1006F#6P是吗，这样的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010380526V#1015F#6P这么说起来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380527V叫我们来王城也\n',
            '和此事有关？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630380528V#094F#5P嗯，也有这层因素……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630380529V#090F其实我有一些关于\n',
            '科洛蒂娅的事想跟你们说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380530V#1004F#6P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380531V#1044F……关于科洛丝？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380532V#406F#5P嗯，其实……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380533V#400F今早已经为我举办了\n',
            '一个继承王位的简单仪式。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380534V如今我的身份已经是\n',
            '利贝尔王国的下一任女王了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000E, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000F, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010380535V#1004F#6P咦咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0070380536V#560F哇……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380537V#1040F……你终于下了决心啊。',
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
        'loc_484E',
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
            TXT(0x00, '【◇完成过学院解放的任务】\n'),
            TXT(0x01, '【◇没完成过学院解放的任务】\n'),
            TXT(0x02, '【◇不变更】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_4842'),
        (0x00000001, 'loc_4848'),
        (-1, 'loc_484E'),
    )

    def _loc_4842(): pass

    label('loc_4842')

    SetScenaFlags(ScenaFlag(0x0405, 7, 0x202F))

    Jump('loc_484E')

    def _loc_4848(): pass

    label('loc_4848')

    ClearScenaFlags(ScenaFlag(0x0405, 7, 0x202F))

    Jump('loc_484E')

    def _loc_484E(): pass

    label('loc_484E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_4A4F',
    )

    ChrTalk(
        0x000C,
        (
            '#0060380538V#466F#5P哪里……\n',
            '只是任性妄为而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380539V#405F艾丝蒂尔、约修亚。\n',
            '还有……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380540V听说你们救了\n',
            '学院的各位？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380541V真是非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380542V#1016F#6P啊……嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380543V#1006F不过不光是我们\n',
            '的功劳哦，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380544V亚妮拉丝和\n',
            '基库也有帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0014,
        (
            '#0440361160V#311F#6P啾⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380546V#401F#5P呵呵，好像是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380547V#406F听说发生了事件之后……\n',
            '我认真地考虑了\n',
            '自己究竟能做些什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380548V为了保护那些我所珍爱的人，\n',
            '自己究竟能起到什么作用……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4B16')

    def _loc_4A4F(): pass

    label('loc_4A4F')

    ChrTalk(
        0x000C,
        (
            '#0060380549V#405F#5P哪里……\n',
            '只是任性妄为而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380550V#406F王国全境都陷入了混乱……\n',
            '我认真地考虑了\n',
            '自己究竟能做些什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380548V为了保护那些我所珍爱的人，\n',
            '自己究竟能起到什么作用……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4B16(): pass

    label('loc_4B16')

    ChrTalk(
        0x0102,
        (
            '#0020380552V#1040F答案就是……\n',
            '由自己来继承王位吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380553V#400F#5P是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380554V#406F对稚嫩的我来说，还没有\n',
            '自信来背负整个王国的重任。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380555V尽管如此，如果能通过继承王位\n',
            '来保护自己所珍爱的人们……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380556V并且保卫王国的话……\n',
            '无论怎样的结果我也会面对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380557V#401F──这就是我的想法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380558V#1017F#6P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    @scena.Lambda('lambda_4C8A')
    def lambda_4C8A():
        CameraMove(-40, 0, 149310, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4C8A)

    @scena.Lambda('lambda_4CA2')
    def lambda_4CA2():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_4CA2')

    DispatchAsync2(0x0008, 0x0002, lambda_4CA2)

    @scena.Lambda('lambda_4CB3')
    def lambda_4CB3():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_4CB3')

    DispatchAsync2(0x0015, 0x0002, lambda_4CB3)

    @scena.Lambda('lambda_4CC4')
    def lambda_4CC4():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_4CC4')

    DispatchAsync2(0x0016, 0x0002, lambda_4CC4)

    @scena.Lambda('lambda_4CD5')
    def lambda_4CD5():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_4CD5')

    DispatchAsync2(0x0102, 0x0002, lambda_4CD5)

    @scena.Lambda('lambda_4CE6')
    def lambda_4CE6():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_4CE6')

    DispatchAsync2(0x000A, 0x0002, lambda_4CE6)

    @scena.Lambda('lambda_4CF7')
    def lambda_4CF7():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_4CF7')

    DispatchAsync2(0x000D, 0x0002, lambda_4CF7)

    @scena.Lambda('lambda_4D08')
    def lambda_4D08():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_4D08')

    DispatchAsync2(0x000E, 0x0002, lambda_4D08)

    @scena.Lambda('lambda_4D19')
    def lambda_4D19():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_4D19')

    DispatchAsync2(0x000F, 0x0002, lambda_4D19)

    ChrSetFlags(0x0101, 0x0040)
    ChrWalkTo(0x0101, -1350, 0, 148350, 1500, 0x00)
    ChrSetChipByIndex(0x000C, 14)
    ChrSetSubChip(0x000C, 0)
    ChrSetFlags(0x000C, 0x0002)
    ChrSetFlags(0x0101, 0x0800)
    ChrSetChipByIndex(0x0101, 14)
    ChrSetSubChip(0x0101, 16)
    ChrSetFlags(0x0101, 0x0002)

    @scena.Lambda('lambda_4D66')
    def lambda_4D66():
        OP_99(0x0101, 0x10, 0x13, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4D66)

    OP_99(0x000C, 0x00, 0x03, 1500)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010380559V#1001F#6P科洛丝，恭喜你！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380560V#1018F你终于找到属于\n',
            '自己的路了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x000C, 0x04, 0x05, 1500)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0060380561V#406F#5P艾丝蒂尔……谢谢你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x000C, 0x05, 0x03, 1500)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0060380562V#405F#5P不过，我还不够成熟，\n',
            '也不知道自己能做些什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380563V当我感到为难的时候……\n',
            '能不能请你们帮忙？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380564V#1001F#6P哈哈！\n',
            '这还用说吗！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380565V#1008F再说我们自身\n',
            '也一样不成熟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380566V#1049F就像你一直以来\n',
            '对我们的帮助一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020380567V#1041F在必要时我们随时会帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380568V#409F#5P艾丝蒂尔、约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380569V#401F……真的很谢谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0x02)
    TerminateThread(0x0015, 0x02)
    TerminateThread(0x0016, 0x02)
    TerminateThread(0x0102, 0x02)
    TerminateThread(0x000A, 0x02)
    TerminateThread(0x000D, 0x02)
    TerminateThread(0x000E, 0x02)
    TerminateThread(0x000F, 0x02)
    CameraMove(910, 0, 149260, 1200)

    ChrTalk(
        0x0016,
        (
            '#0130380570V#115F#5P（……如今我才真正认识到…\n',
            '当初的自己有多么愚蠢。)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130380571V#116F（根本没看清这些担负着未来的\n',
            '年轻人所具备的可能性，\n',
            '而做出了那样的蠢事……)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0620380572V#700F#2P（理查德先生……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 180, 400)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0630380573V#091F#5P（呵呵，这叫什么话。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630380574V#090F（你自己也是担负着\n',
            '王国未来的年轻人啊。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0620380575V#701F#2P（陛下……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0130380576V#118F#2P（您、您开玩笑了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0017, 10, 0, 137650, 0)
    ChrClearFlags(0x0017, 0x0080)

    NpcTalk(
        0x0017,
        '青年的声音',
        (
            '#2690380577V#4S#1P报、报告！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x00000BB8)
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000A, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x000D, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x000E, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x000F, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x0015, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0016, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_52A8')
    def lambda_52A8():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_52A8)

    @scena.Lambda('lambda_52B6')
    def lambda_52B6():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_52B6)

    Sleep(50)

    @scena.Lambda('lambda_52C9')
    def lambda_52C9():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_52C9)

    @scena.Lambda('lambda_52D7')
    def lambda_52D7():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_52D7)

    Sleep(50)

    @scena.Lambda('lambda_52EA')
    def lambda_52EA():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_52EA)

    @scena.Lambda('lambda_52F8')
    def lambda_52F8():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_52F8)

    Sleep(50)

    @scena.Lambda('lambda_530B')
    def lambda_530B():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_530B)

    @scena.Lambda('lambda_5319')
    def lambda_5319():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_5319)

    ChrSetChipByIndex(0x000C, 19)
    ChrSetSubChip(0x000C, 0)
    ChrClearFlags(0x000C, 0x0002)
    ChrClearFlags(0x000C, 0x0800)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrClearFlags(0x0101, 0x0002)
    ChrClearFlags(0x0101, 0x0800)

    @scena.Lambda('lambda_534F')
    def lambda_534F():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_534F)

    @scena.Lambda('lambda_535D')
    def lambda_535D():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_535D)

    @scena.Lambda('lambda_536B')
    def lambda_536B():
        CameraMove(1100, 0, 146260, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_536B)

    @scena.Lambda('lambda_5383')
    def lambda_5383():
        OP_67(0, 5630, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_5383)

    @scena.Lambda('lambda_539B')
    def lambda_539B():
        CameraSetDistance(1900, 2500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_539B)

    @scena.Lambda('lambda_53AB')
    def lambda_53AB():
        OP_6E(488, 2500)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_53AB)

    Sleep(1000)

    @scena.Lambda('lambda_53C0')
    def lambda_53C0():
        ChrWalkTo(0x00FE, 340, 0, 141780, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_53C0)

    Sleep(1000)

    @scena.Lambda('lambda_53E0')
    def lambda_53E0():
        ChrWalkTo(0x00FE, -360, 0, 145930, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_53E0)

    WaitForThreadExit(0x0017, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0015,
        (
            '#0620380578V#702F#5P什么事？\n',
            '市区又发生了什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#2690380579V#2P不、不是，那边的\n',
            '局势已经勉强收拾住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#2690380580V#2P猎兵们也都从\n',
            '王都撤退了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0620380581V#700F#5P那么是什么事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(100)

    PlayBGM(35)
    Sleep(500)

    ChrTalk(
        0x0017,
        (
            '#2690380582V#2P刚、刚才收到了\n',
            '哈肯大门的联络……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#2690380583V#2P说帝国军开始在边境\n',
            '附近集结了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000E, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000F, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0015, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0016, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010380584V#1020F#5P#4S啊！？',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0130380585V#117F#5P果然来了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630380586V#092F#5P……集结的\n',
            '规模怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#2690380587V#2P现在有一个师\n',
            '左右的兵力……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#2690380588V#2P不、不过其中似乎有\n',
            '坦克部队……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000E, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000F, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0015, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0016, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0015,
        (
            '#0620380589V#704F#5P你说什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0050380590V#055F#5P等、等等！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050380591V在导力停止现象下\n',
            '为什么坦克能够开动！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030380592V#024F#5P难道他们使用了和\n',
            '『结社』相同的技术！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#2690380593V#2P不……他们使用的似乎是\n',
            '使用了不搭载导力机械的型号。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#2690380594V#2P据观察，是\n',
            '由『蒸气机』驱动的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380595V#1026F#5P蒸气……机？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000E, 45, 400)
    Sleep(300)

    ChrTalk(
        0x000E,
        (
            '#0070380596V#065F#6P那个那个……\n',
            '是比内燃引擎还要原始的\n',
            '使用蒸气能量的引擎……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070380597V随着导力器的普及，\n',
            '这种发明很快就被荒废了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0130380598V#112F#5P……应该不可能有哪个国家\n',
            '还拥有以它为动力的坦克。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130380599V因为与导力坦克相比，\n',
            '成本和性能的性价比实在太差了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5AC3')
    def lambda_5AC3():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_5AC3)

    ChrTalk(
        0x000F,
        (
            '#0080380600V#074F#5P那只有一种可能性了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080380601V#072F这是偷偷地在帝国\n',
            '内部制造的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380602V#1002F#5P就、就是说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0620380603V#703F#5P……他们早就预计到\n',
            '这种情况了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0620380604V#702F那么结社那伙儿人\n',
            '所说的『下一次试练』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_5BD1')
    def lambda_5BD1():
        CameraMove(1100, 0, 147600, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_5BD1)

    @scena.Lambda('lambda_5BE9')
    def lambda_5BE9():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5BE9)

    Sleep(50)

    @scena.Lambda('lambda_5BFC')
    def lambda_5BFC():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5BFC)

    @scena.Lambda('lambda_5C0A')
    def lambda_5C0A():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_5C0A)

    Sleep(50)

    @scena.Lambda('lambda_5C1D')
    def lambda_5C1D():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_5C1D)

    @scena.Lambda('lambda_5C2B')
    def lambda_5C2B():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_5C2B)

    Sleep(50)

    @scena.Lambda('lambda_5C3E')
    def lambda_5C3E():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_5C3E)

    @scena.Lambda('lambda_5C4C')
    def lambda_5C4C():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_5C4C)

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0102,
        (
            '#0020380605V#1043F#4P嗯……\n',
            '恐怕就是指这个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020380606V#1042F而且他们这次是\n',
            '把王都当作人质了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0130380607V#118F#5P『只要想的话\n',
            '随时可以攻击王都』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130380608V也有这种意图在里面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380609V#1035F#4P还有一点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020380610V#1042F父亲应该是把您\n',
            '当作了隐藏的牌。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020380611V在发生紧急情况时\n',
            '可以代替自己\n',
            '进行派遣的王牌。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020380612V可是现在这张牌已经\n',
            '使用过了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0130380613V#113F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0620380614V#703F#5P『噬身之蛇』……\n',
            '竟算计得这么深。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x000C)
    Sleep(500)

    ChrTurnDirection(0x000C, 0x0008, 400)

    ChrTalk(
        0x000C,
        (
            '#0060380615V#402F#6P……祖母大人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380616V请派我前往\n',
            '哈肯大门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x000E, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000F, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0016, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0015, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_5F90')
    def lambda_5F90():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_5F90)

    @scena.Lambda('lambda_5F9E')
    def lambda_5F9E():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_5F9E)

    Sleep(50)

    @scena.Lambda('lambda_5FB1')
    def lambda_5FB1():
        ChrSetDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_5FB1)

    @scena.Lambda('lambda_5FBF')
    def lambda_5FBF():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_5FBF)

    Sleep(50)

    @scena.Lambda('lambda_5FD2')
    def lambda_5FD2():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_5FD2)

    @scena.Lambda('lambda_5FE0')
    def lambda_5FE0():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_5FE0)

    ChrTalk(
        0x0101,
        (
            '#0010380617V#1004F#6P咦咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380618V#1044F#4P科洛丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380619V#406F#6P如果我什么也不做，\n',
            '怎么对得起为了让我们逃走\n',
            '而受伤的叔叔呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060380620V#402F我一定要作为祖母大人的代理人\n',
            '去完成和帝国军的交涉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630380621V#094F#5P……明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630380622V#092F虽然互不侵犯条约已经缔结，\n',
            '不过王国和帝国之间的天平\n',
            '至今还不稳定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630380623V这次的事件有可能会\n',
            '招致更大的动荡。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630380624V#090F恢复天平的平衡……\n',
            '这件事就拜托给你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380625V#401F#6P……是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_61DA')
    def lambda_61DA():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_61DA)

    Sleep(80)

    @scena.Lambda('lambda_61ED')
    def lambda_61ED():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_61ED)

    Sleep(80)

    @scena.Lambda('lambda_6200')
    def lambda_6200():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_6200)

    Sleep(80)

    @scena.Lambda('lambda_6213')
    def lambda_6213():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_6213)

    Sleep(80)

    @scena.Lambda('lambda_6226')
    def lambda_6226():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_6226)

    Sleep(80)

    @scena.Lambda('lambda_6239')
    def lambda_6239():
        ChrSetDirection(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_6239)

    Sleep(500)

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔她们互相交换了眼神。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)

    @scena.Lambda('lambda_6289')
    def lambda_6289():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_6289)

    Sleep(50)

    @scena.Lambda('lambda_629C')
    def lambda_629C():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_629C)

    Sleep(50)

    @scena.Lambda('lambda_62AF')
    def lambda_62AF():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_62AF)

    Sleep(50)

    @scena.Lambda('lambda_62C2')
    def lambda_62C2():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_62C2)

    Sleep(50)

    @scena.Lambda('lambda_62D5')
    def lambda_62D5():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_62D5)

    Sleep(50)

    @scena.Lambda('lambda_62E8')
    def lambda_62E8():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_62E8)

    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010380626V#1006F#6P我说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010380627V那我们也一起\n',
            '去，行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x0016, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(50)

    OP_62(0x0015, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_639F')
    def lambda_639F():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_639F)

    Sleep(50)

    @scena.Lambda('lambda_63B2')
    def lambda_63B2():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_63B2)

    Sleep(50)

    @scena.Lambda('lambda_63C5')
    def lambda_63C5():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_63C5)

    Sleep(50)

    ChrSetDirection(0x0015, 180, 400)

    ChrTalk(
        0x000C,
        (
            '#0060380628V#409F#5P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380629V#1040F#4P我们会护送公主殿下\n',
            '平安到达哈肯大门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0050380630V#051F#6P并且，万一\n',
            '战争一触即发，我们\n',
            '也会起到自己的作用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030380631V#027F当然，根据协会的规定，\n',
            '我们不能参与战争……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0080380632V#071F不过站在中立立场上的仲裁，\n',
            '我们会尽力而为。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0060380633V#405F#5P各位……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0630380634V#090F#5P呵呵……\n',
            '这真是求之不得。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0630380635V#091F拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380636V#1006F#6P是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380637V#1040F#4P请交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0130380638V#115F#5P……艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130380639V#110F关于『结社』的动向\n',
            '就让我们来负责监控吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#0620380640V#701F#5P我们会准备好万全的对策，\n',
            '即使那架巨大机器人出现在\n',
            '王都，我们也会积极应对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010380641V#1025F#6P二位……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020380642V#1035F#4P拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(500)

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '就这样，艾丝蒂尔她们\n',
            '护送着科洛丝前往哈肯大门了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '在穿过了格鲁纳门，以尽可能\n',
            '快的速度通过了洛连特地区后……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔她们终于抵达了哈肯大门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_20(0x00000BB8)
    OP_21()
    Sleep(1000)

    ChrClearFlags(0x0101, 0x0040)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T1400._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
