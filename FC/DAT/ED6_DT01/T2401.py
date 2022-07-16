import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2401_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2401   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '扎古'),
    TXT(0x02, '索雷诺'),
    TXT(0x03, '梅威海道方向'),
    TXT(0x04, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2401.x'
    header.mapIndex       = 1
    header.bgm            = 83
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2444
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
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT06/CH20059._CH', 'ED6_DT06/CH20059P._CP'),
    ]

# id: 0x10002 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -7120,
            z                   = 0,
            y                   = 37380,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = -6060,
            z                   = 0,
            y                   = 37610,
            direction           = 13,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 1060,
            z                   = 0,
            y                   = -23220,
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

# id: 0x10003 offset: 0x122
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x122
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -2580,
            y           = 2000,
            z           = 3190,
            range       = 2800,
            dword_10    = 0xFFFFF448,
            dword_14    = 0x00000578,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000F,
        ),
    )

# id: 0x10005 offset: 0x142
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 1370,
            triggerZ            = 0,
            triggerY            = 30050,
            triggerRange        = 1000,
            actorX              = 1370,
            actorZ              = 0,
            actorY              = 30050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3480,
            triggerZ            = 0,
            triggerY            = 34330,
            triggerRange        = 1000,
            actorX              = 3480,
            actorZ              = 0,
            actorY              = 34330,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 6440,
            triggerZ            = 160,
            triggerY            = 23740,
            triggerRange        = 1200,
            actorX              = 6440,
            actorZ              = 1000,
            actorY              = 23740,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 12030,
            triggerZ            = 0,
            triggerY            = 18180,
            triggerRange        = 1200,
            actorX              = 12030,
            actorZ              = 0,
            actorY              = 18180,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 3580,
            triggerZ            = 0,
            triggerY            = 7000,
            triggerRange        = 1000,
            actorX              = 3580,
            actorZ              = 0,
            actorY              = 7000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -3040,
            triggerZ            = 0,
            triggerY            = 8250,
            triggerRange        = 1000,
            actorX              = -3040,
            actorZ              = 0,
            actorY              = 8250,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 12390,
            triggerZ            = 0,
            triggerY            = 25680,
            triggerRange        = 1000,
            actorX              = 12390,
            actorZ              = 500,
            actorY              = 25680,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 7430,
            triggerZ            = 0,
            triggerY            = 39210,
            triggerRange        = 1000,
            actorX              = 7430,
            actorZ              = 700,
            actorY              = 39210,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -8700,
            triggerZ            = 0,
            triggerY            = 35870,
            triggerRange        = 1000,
            actorX              = -8700,
            actorZ              = 700,
            actorY              = 35870,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -5150,
            triggerZ            = -200,
            triggerY            = 15360,
            triggerRange        = 1000,
            actorX              = -5150,
            actorZ              = -200,
            actorY              = 15360,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 5610,
            triggerZ            = -280,
            triggerY            = 16930,
            triggerRange        = 1000,
            actorX              = 5610,
            actorZ              = -280,
            actorY              = 16930,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -4980,
            triggerZ            = -350,
            triggerY            = 23150,
            triggerRange        = 1000,
            actorX              = -4980,
            actorZ              = -350,
            actorY              = 23150,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2F2
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_30D',
    )

    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0008)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0009, 0x0008)

    def _loc_30D(): pass

    label('loc_30D')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_319'),
        (-1, 'loc_32B'),
    )

    def _loc_319(): pass

    label('loc_319')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0084, 0, 0x420)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_328',
    )

    SetScenaFlags(ScenaFlag(0x0084, 0, 0x420))
    Event(0, 0x0005)

    def _loc_328(): pass

    label('loc_328')

    Jump('loc_32B')

    def _loc_32B(): pass

    label('loc_32B')

    Return()

# id: 0x0001 offset: 0x32C
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -128000, -108000, 196712)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_356',
    )

    OP_B1('t2401_y')

    Jump('loc_35F')

    def _loc_356(): pass

    label('loc_356')

    OP_B1('t2401_n')

    def _loc_35F(): pass

    label('loc_35F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0084, 7, 0x427)),
            Expr.Return,
        ),
        'loc_396',
    )

    OP_64(0x00, 0x0001)
    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)
    OP_64(0x05, 0x0001)
    OP_64(0x06, 0x0001)
    OP_64(0x07, 0x0001)
    OP_64(0x08, 0x0001)
    OP_64(0x09, 0x0001)
    OP_64(0x0A, 0x0001)
    OP_64(0x0B, 0x0001)

    def _loc_396(): pass

    label('loc_396')

    Return()

# id: 0x0002 offset: 0x397
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3AC',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_3AC(): pass

    label('loc_3AC')

    Return()

# id: 0x0003 offset: 0x3AD
@scena.Code('func_03_3AD')
def func_03_3AD():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0084, 7, 0x427)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4EE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_463',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '#1510050197V啊，昨天真的把我吓死了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1510050198V东边的天空变得通红，\n',
            '在玛诺利亚村那里也看得见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1510050199V虽然已经采取了紧急措施，\n',
            '但还是没有控制住火势。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4E4')

    def _loc_463(): pass

    label('loc_463')

    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '#1510050200V话说回来， \n',
            '怎么会弄得这么乱？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1510050201V昨天来的时候这里太暗，\n',
            '什么都看不清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1510050202V药草田也一塌糊涂。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4E4(): pass

    label('loc_4E4')

    SetScenaFlags(ScenaFlag(0x0084, 4, 0x424))
    Call(0, 0x000E)

    Jump('loc_598')

    def _loc_4EE(): pass

    label('loc_4EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_565',
    )

    ChrTalk(
        0x00FE,
        (
            '#1510050203V呼……\n',
            '已经烧得不剩什么了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1510050204V我还想要是孩子们的\n',
            '东西留下什么的话，\n',
            '就给他们带回去呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_598')

    def _loc_565(): pass

    label('loc_565')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0084, 7, 0x427)),
            Expr.Return,
        ),
        'loc_598',
    )

    ChrTalk(
        0x00FE,
        (
            '#1510050205V怎么样，游击士。\n',
            '明白什么了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_598(): pass

    label('loc_598')

    TalkEnd(0x0009)

    Return()

# id: 0x0004 offset: 0x59C
@scena.Code('func_04_59C')
def func_04_59C():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0084, 7, 0x427)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6B9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_627',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#1500050206V烧得这么彻底，\n',
            '看来要重新建造一间才行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1500050207V看来要花费很大一笔钱，\n',
            '特蕾莎院长打算怎么做呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6AF')

    def _loc_627(): pass

    label('loc_627')

    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#1500050208V特蕾莎院长也在\n',
            '教玛诺利亚村的孩子们念书。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1500050209V我也从小受她照顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1500050210V正是这种时候，\n',
            '我要向她好好报恩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6AF(): pass

    label('loc_6AF')

    SetScenaFlags(ScenaFlag(0x0084, 5, 0x425))
    Call(0, 0x000E)

    Jump('loc_7F4')

    def _loc_6B9(): pass

    label('loc_6B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_719',
    )

    ChrTalk(
        0x00FE,
        (
            '#1500050211V这里已经\n',
            '大致收拾完了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1500050212V接下来就只能等待\n',
            '你们的调查结果了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7F4')

    def _loc_719(): pass

    label('loc_719')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0084, 7, 0x427)),
            Expr.Return,
        ),
        'loc_7F4',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7A4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#1500050213V我小时候\n',
            '就认识特蕾莎院长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1500050214V收拾火后残局\n',
            '还真是累人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1500050215V怎么会发生\n',
            '这么惨的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7F4')

    def _loc_7A4(): pass

    label('loc_7A4')

    ChrTalk(
        0x00FE,
        (
            '#1500050216V我小时候\n',
            '就认识特蕾莎院长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1500050217V收拾火后残局\n',
            '还真是累人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7F4(): pass

    label('loc_7F4')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x7F8
@scena.Code('func_05_7F8')
def func_05_7F8():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    OP_28(0x003B, 0x01, 0x0001)
    OP_28(0x003B, 0x01, 0x0002)
    OP_28(0x003B, 0x01, 0x0004)
    CameraMove(-490, 8000, 30040, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0101, 850, 0, 15900, 0)
    SetChrPos(0x0102, -290, 0, 15900, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_085C')
    def lambda_085C():
        OP_6C(0, 8000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_085C)

    OP_67(0, 17000, -10000, 0)
    OP_67(0, 9500, -10000, 5000)

    @scena.Lambda('lambda_088E')
    def lambda_088E():
        ChrWalkTo(0x00FE, 850, 0, 24800, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_088E)

    Sleep(500)

    @scena.Lambda('lambda_08AE')
    def lambda_08AE():
        ChrWalkTo(0x00FE, -290, 20, 24200, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_08AE)

    CameraMove(190, 0, 25000, 4000)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010050155V#003F太、太惨了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050156V#013F房子完全被烧毁了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1500050157V#4P哎？你们两个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4A(0x0008, 255)
    OP_4A(0x0009, 255)

    @scena.Lambda('lambda_094F')
    def lambda_094F():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_094F')

    DispatchAsync2(0x0101, 0x0001, lambda_094F)

    @scena.Lambda('lambda_0960')
    def lambda_0960():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0960')

    DispatchAsync2(0x0102, 0x0001, lambda_0960)

    @scena.Lambda('lambda_0971')
    def lambda_0971():
        CameraMove(-450, 40, 26930, 1500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0971)

    @scena.Lambda('lambda_0989')
    def lambda_0989():
        ChrWalkTo(0x00FE, -5120, 120, 30950, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0989)

    Sleep(600)

    @scena.Lambda('lambda_09A9')
    def lambda_09A9():
        ChrWalkTo(0x00FE, -5120, 120, 30950, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_09A9)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_09C9')
    def lambda_09C9():
        ChrWalkTo(0x00FE, 630, 0, 27190, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_09C9)

    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_09E9')
    def lambda_09E9():
        ChrWalkTo(0x00FE, -420, 30, 27190, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_09E9)

    WaitForThreadExit(0x0008, 0x0002)
    SetChrDirection(0x0008, 180, 400)
    WaitForThreadExit(0x0009, 0x0002)
    SetChrDirection(0x0009, 180, 400)

    ChrTalk(
        0x0009,
        (
            '#1510050158V莫非你们就是\n',
            '游击士协会派来的人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050159V#002F嗯，是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050160V#012F你们是玛诺利亚村的人吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1500050161V是啊……\n',
            '我们正在清理瓦砾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1500050162V昨天半夜突然起火，\n',
            '我们就慌忙赶过来救火……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1500050163V唉，如你们所见，\n',
            '房子已经被烧了个精光啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050164V#005F那、那么……\n',
            '特蕾莎院长和孩子们呢！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1510050165V还好，大家都平安无事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1510050166V他们现在正在\n',
            '玛诺利亚的旅店里休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1510050167V虽然遇到那么大的火灾，\n',
            '但是大家最后还是平安无事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050168V#007F太、太好了～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050169V#011F嗯……真是不幸中的大幸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1500050170V我们还要在这里\n',
            '做一下清理的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1500050171V你们有什么打算呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050172V#501F啊，我想尽快赶去旅店\n',
            '看看那些孩子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0102, 0x01)
    SetChrDirection(0x0102, 45, 400)

    ChrTalk(
        0x0102,
        (
            '#0020050173V#015F艾丝蒂尔，现在还不能去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x01)
    SetChrDirection(0x0101, 225, 400)

    ChrTalk(
        0x0101,
        (
            '#0010050174V#004F哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050175V#012F这个现场，光是粗略一看，\n',
            '就可以发现很多可疑的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050176V而作为案件的线索，\n',
            '时间一久就会消失的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050177V……你的心情我很明白，\n',
            '不过现在要以现场取证为先。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050178V#003F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050179V#500F好吧……\n',
            '谁让我们是游击士呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050180V#002F一定把事情查个水落石出。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050181V#010F嗯……\n',
            '那就抓紧时间在房子周围调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#1510050182V你们似乎商量好了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1500050183V那就拜托你们了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0EB9')
    def lambda_0EB9():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0EB9')

    DispatchAsync2(0x0101, 0x0001, lambda_0EB9)

    @scena.Lambda('lambda_0ECA')
    def lambda_0ECA():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0ECA')

    DispatchAsync2(0x0102, 0x0001, lambda_0ECA)

    @scena.Lambda('lambda_0EDB')
    def lambda_0EDB():
        CameraMove(190, 0, 24500, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0EDB)

    SetChrDirection(0x0009, 315, 400)

    @scena.Lambda('lambda_0EFA')
    def lambda_0EFA():
        ChrWalkTo(0x00FE, -6530, 0, 33070, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0EFA)

    Sleep(300)

    SetChrDirection(0x0008, 315, 400)

    @scena.Lambda('lambda_0F21')
    def lambda_0F21():
        ChrWalkTo(0x00FE, -6530, 0, 33070, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0F21)

    WaitForThreadExit(0x0009, 0x0001)
    SetChrPos(0x0009, -6060, 0, 37610, 13)
    WaitForThreadExit(0x0008, 0x0001)
    SetChrPos(0x0008, -7120, 0, 37380, 315)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    OP_4B(0x0008, 255)
    OP_4B(0x0009, 255)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0xF75
@scena.Code('func_06_F75')
def func_06_F75():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1043',
    )

    EventBegin(0x00)
    CameraMove(3480, 0, 34330, 1000)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '石壁完全倒塌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010050187V#002F这里……\n',
            '塌得特别厉害呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050188V还有……\n',
            '你闻到什么古怪的味道吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050189V#012F是啊。\n',
            '这难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_1093')

    def _loc_1043(): pass

    label('loc_1043')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '石壁完全倒塌，\n',
            '附近漂着一股刺激性气味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    def _loc_1093(): pass

    label('loc_1093')

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    SetScenaFlags(ScenaFlag(0x0084, 2, 0x422))
    OP_28(0x003B, 0x01, 0x0010)
    Call(0, 0x000E)

    Return()

# id: 0x0007 offset: 0x10A4
@scena.Code('func_07_10A4')
def func_07_10A4():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 1, 0x9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_11EB',
    )

    EventBegin(0x00)
    CameraMove(1240, 0, 30880, 1000)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门的残骸倒在地上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010050190V#004F哇……\n',
            '都被烧得黑乎乎了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050191V#002F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050192V#014F怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050193V#002F可能是我多心了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050194V你觉不觉得\n',
            '门锁的部分坏得很特别？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050195V#012F……的确。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050196V感觉就像是\n',
            '起火前就已经被破坏了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_123D')

    def _loc_11EB(): pass

    label('loc_11EB')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '已经变成残骸的门，\n',
            '门锁的部分坏得很特别。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    def _loc_123D(): pass

    label('loc_123D')

    SetScenaFlags(ScenaFlag(0x0001, 1, 0x9))
    SetScenaFlags(ScenaFlag(0x0084, 3, 0x423))
    OP_28(0x003B, 0x01, 0x0008)
    Call(0, 0x000E)

    Return()

# id: 0x0008 offset: 0x124E
@scena.Code('func_08_124E')
def func_08_124E():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '种植的香草\n',
            '被连根拔起且四处散落。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    TalkEnd(0x00FF)

    Return()

# id: 0x0009 offset: 0x129C
@scena.Code('func_09_129C')
def func_09_129C():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '室外用的餐桌周围\n',
            '散落着东倒西歪的圆木椅子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    TalkEnd(0x00FF)

    Return()

# id: 0x000A offset: 0x12F4
@scena.Code('func_0A_12F4')
def func_0A_12F4():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '花坛里的泥土\n',
            '在周围的地面上撒得满处都是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    TalkEnd(0x00FF)

    Return()

# id: 0x000B offset: 0x134A
@scena.Code('func_0B_134A')
def func_0B_134A():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '暖炉用的木柴散落一地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    TalkEnd(0x00FF)

    Return()

# id: 0x000C offset: 0x138D
@scena.Code('func_0C_138D')
def func_0C_138D():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '倒下的牛奶桶\n',
            '已经没有一滴牛奶剩下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))
    TalkEnd(0x00FF)

    Return()

# id: 0x000D offset: 0x13DF
@scena.Code('func_0D_13DF')
def func_0D_13DF():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '装食物的木桶被烧得漆黑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))
    TalkEnd(0x00FF)

    Return()

# id: 0x000E offset: 0x1424
@scena.Code('func_0E_1424')
def func_0E_1424():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0084, 7, 0x427)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0084, 2, 0x422)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0084, 3, 0x423)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0084, 4, 0x424)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0084, 5, 0x425)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2336',
    )

    SetScenaFlags(ScenaFlag(0x0084, 7, 0x427))
    OP_28(0x003B, 0x01, 0x0020)
    OP_28(0x003B, 0x01, 0x0040)
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(1740, 0, 29000, 0)
    OP_6C(0, 0)
    FormationAddMember(0x35, 0xFF)
    SetChrPos(0x0101, 1070, 0, 28010, 90)
    SetChrPos(0x0102, 2840, 0, 27990, 270)
    SetChrPos(0x0136, 1810, 0, 26160, 45)
    SetChrFlags(0x0136, 0x0080)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0102,
        (
            '#0020050218V#012F#2P好了……\n',
            '已经发现不少线索了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050219V#012F就在这附近\n',
            '整理一下思绪吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050220V#002F#1P嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050221V#013F#2P首先，关于起火地点……\n',
            '从现场可以推断不是在屋内发生的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050222V在屋外的可能性很高。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050223V#004F#1P屋外？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050224V#012F#2P嗯，是这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    @scena.Lambda('lambda_15EE')
    def lambda_15EE():
        CameraMove(3590, 0, 34040, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_15EE)

    @scena.Lambda('lambda_1606')
    def lambda_1606():
        OP_6C(315000, 2500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1606)

    @scena.Lambda('lambda_1616')
    def lambda_1616():
        ChrWalkTo(0x00FE, 4190, 0, 33510, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1616)

    Sleep(500)

    ChrWalkTo(0x0101, 3080, 0, 28970, 3000, 0x00)

    @scena.Lambda('lambda_164A')
    def lambda_164A():
        ChrWalkTo(0x00FE, 4310, 0, 32200, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_164A)

    WaitForThreadExit(0x0102, 0x0001)
    SetChrDirection(0x0102, 315, 400)

    ChrTalk(
        0x0102,
        (
            '#0020050225V#012F#4P……火大概是从这一带开始，\n',
            '然后逐渐包围了整座房子吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010050226V#004F啊……\n',
            '是石壁倒塌的地方呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050227V#002F但是……\n',
            '你怎么知道这里就是起火地点呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050228V#013F#4P因为这里地面的烧焦程度\n',
            '比其它地方都要厉害。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050229V和周围比较一下就知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 270, 400)
    Sleep(200)

    SetChrDirection(0x0101, 90, 400)
    Sleep(200)

    SetChrDirection(0x0101, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010050230V#002F啊，真的呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020050231V#012F#2P火势是由屋外\n',
            '向屋内逐渐蔓延的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050232V你知道这意味着什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010050233V#002F这、这就是说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

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
            TXT(0x00, '【森林火灾造成的意外】\n'),
            TXT(0x01, '【人为的纵火案件】\n'),
            TXT(0x02, '【照明工具的过热引起的事故】\n'),
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
        (0x00000000, 'loc_18E2'),
        (0x00000001, 'loc_1A0E'),
        (0x00000002, 'loc_1AB1'),
        (-1, 'loc_1C0D'),
    )

    def _loc_18E2(): pass

    label('loc_18E2')

    ChrTalk(
        0x0102,
        (
            '#0020050234V#013F#2P虽然房屋附近的树木\n',
            '也被烧得焦黑……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050235V不过我想只是火从房屋\n',
            '蔓延到那里去了而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050236V#004F那么，难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050237V#015F很明显是有人放火。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050238V#012F#2P附近飘散着的这股气味……\n',
            '是一种可燃性极高的油。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050239V估计是在这附近洒满油之后，\n',
            '再点火引燃的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x003B, 0x0001)

    Jump('loc_1C0D')

    def _loc_1A0E(): pass

    label('loc_1A0E')

    ChrTalk(
        0x0102,
        (
            '#0020050240V#015F#2P嗯，我也是这么想。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050241V#012F#2P附近飘散着的这股气味……\n',
            '是一种可燃性极高的油。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050242V估计是在这附近洒满油之后，\n',
            '再点火引燃的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_2B(0x003B, 0x0002)

    Jump('loc_1C0D')

    def _loc_1AB1(): pass

    label('loc_1AB1')

    ChrTalk(
        0x0102,
        (
            '#0020050243V#013F#2P确实，由这个原因\n',
            '引起火灾的可能性也不是没有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050244V不过根据我的记忆，\n',
            '这个地方应该没有照明工具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050245V#004F你、你记得还真清楚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050246V#004F那么，难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050247V#015F#2P很明显是有人放火。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050248V#012F#2P附近飘散着的这股气味……\n',
            '是一种可燃性极高的油。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050249V估计是在这附近洒满油之后，\n',
            '再点火引燃的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C0D')

    def _loc_1C0D(): pass

    label('loc_1C0D')

    ChrTalk(
        0x0101,
        (
            '#0010050250V#003F怎、怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050251V#013F#2P还有，屋子四周乱七八糟的样子，\n',
            '这一点也很让人觉得可疑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050252V连跟救火完全没关系的\n',
            '香草田也被弄得一塌糊涂。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050253V我想这一定也是人为造成的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0136,
        '女孩的声音',
        (
            '#0060050254V#2P这是……真的吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ClearChrFlags(0x0136, 0x0080)

    @scena.Lambda('lambda_1D3F')
    def lambda_1D3F():
        CameraMove(4110, 0, 29630, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1D3F)

    @scena.Lambda('lambda_1D57')
    def lambda_1D57():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1D57)

    SetChrDirection(0x0101, 225, 400)
    ChrTurnDirection(0x0102, 0x0136, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010050255V#004F啊，科洛丝！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050256V#014F你也来了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1DBA')
    def lambda_1DBA():
        CameraMove(2000, 0, 27550, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1DBA)

    @scena.Lambda('lambda_1DD2')
    def lambda_1DD2():
        ChrWalkTo(0x00FE, 2640, 0, 26910, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1DD2)

    Sleep(300)

    @scena.Lambda('lambda_1DF2')
    def lambda_1DF2():
        ChrWalkTo(0x00FE, 3530, 0, 27000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1DF2)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_1E12')
    def lambda_1E12():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1E12)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_1E25')
    def lambda_1E25():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1E25)

    ChrTalk(
        0x0136,
        (
            '#0060050257V#049F为什么……\n',
            '是谁……竟然做出这种事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050258V这地方充满了\n',
            '多少无可替代的珍贵回忆……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050259V#046F为什么……这么……\n',
            '残忍的事也能做出来……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050260V#003F#2P科洛丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020050261V#013F#2P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050262V#049F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050263V对不起……\n',
            '……我现在心情很乱……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050264V我……我…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0101, 0x0136, 600, 1000, 0x00)
    Fade(500)
    SetChrPos(0x0136, 2060, 0, 26360, 45)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0136, 0x0002)
    ClearChrFlags(0x0136, 0x0001)
    SetChrChipByIndex(0x0136, 2)
    SetChrSubChip(0x0136, 1)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010050265V#003F#2P我明白的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050266V连我这个刚认识他们不久的人\n',
            '都觉得非常难受……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050267V……简直无法相信。\n',
            '竟然会有人做出这种事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050268V#043F艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050269V#006F#2P不过，好在特蕾莎院长\n',
            '和那些孩子都平安无事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010050270V所以呢，没事了。\n',
            '我这样说你可以放心了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050271V#049F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050272V#047F……谢谢你。\n',
            '我觉得现在镇定了很多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050273V早上我在上课的时候，\n',
            '校长突然跑过来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050274V告诉我孤儿院\n',
            '昨晚发生了火灾……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060050275V在来到这里之前……\n',
            '我整个人简直快要崩溃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050276V#000F#2P是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    SetChrPos(0x0136, 1810, 0, 26160, 45)
    ClearChrFlags(0x0101, 0x0080)
    ClearChrFlags(0x0136, 0x0002)
    SetChrFlags(0x0136, 0x0001)
    SetChrChipByIndex(0x0136, 65535)
    SetChrSubChip(0x0136, 0)
    OP_0D()
    OP_94(0x01, 0x0101, 0x00B4, 0x000001F4, 0x000003E8, 0x00)

    ChrTalk(
        0x0102,
        (
            '#0020050277V#010F#2P听说特蕾莎院长和孩子们\n',
            '都在玛诺利亚的旅店里休息。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050278V现场取证也结束了， \n',
            '就让我们陪你一起去看望他们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060050279V#048F嗯，好呢……\n',
            '这样我真是求之不得了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010050280V#006F#2P那么，\n',
            '我们就赶快去玛诺利亚村吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_64(0x00, 0x0001)
    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)
    OP_64(0x03, 0x0001)
    OP_64(0x04, 0x0001)
    OP_64(0x05, 0x0001)
    OP_64(0x06, 0x0001)
    OP_64(0x07, 0x0001)
    OP_64(0x08, 0x0001)
    OP_64(0x09, 0x0001)
    OP_64(0x0A, 0x0001)
    OP_64(0x0B, 0x0001)
    EventEnd(0x00)

    def _loc_2336(): pass

    label('loc_2336')

    Return()

# id: 0x000F offset: 0x2337
@scena.Code('func_0F_2337')
def func_0F_2337():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0084, 7, 0x427)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2423',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_23BB',
    )

    ChrTalk(
        0x0102,
        (
            '#0020050184V#013F你的心情我可以理解，\n',
            '不过还是等一会儿再去探望他们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020050185V现在要紧的是调查火灾的原因……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23BB(): pass

    label('loc_23BB')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2408',
    )

    ChrTalk(
        0x0102,
        (
            '#0020050186V#012F（总之调查的范围\n',
            '　还是限定在这附近比较好……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2408(): pass

    label('loc_2408')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_2423(): pass

    label('loc_2423')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
