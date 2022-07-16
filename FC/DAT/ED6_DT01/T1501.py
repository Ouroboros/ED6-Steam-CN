import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1501_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1501   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '小船'),
    TXT(0x02, '吉尔'),
    TXT(0x03, '乔丝特'),
    TXT(0x04, '黑衣男子'),
    TXT(0x05, '特务兵'),
    TXT(0x06, '安塞尔新街方向'),
    TXT(0x07, ''),
    TXT(0x08, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1501.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x22A9
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0xFFFFE4A8,
            dword_04        = 0x00000000,
            dword_08        = 0x00014050,
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
            word_30         = 225,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 50,
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
        ('ED6_DT07/CH02120._CH', 'ED6_DT07/CH02120P._CP'),
        ('ED6_DT07/CH02130._CH', 'ED6_DT07/CH02130P._CP'),
        ('ED6_DT07/CH02200._CH', 'ED6_DT07/CH02200P._CP'),
        ('ED6_DT07/CH00444._CH', 'ED6_DT07/CH00444P._CP'),
    ]

# id: 0x10002 offset: 0xCA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0184,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 26500,
            z                   = 0,
            y                   = 12600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 26500,
            z                   = 0,
            y                   = 12600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 26500,
            z                   = 0,
            y                   = 12600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 26500,
            z                   = 0,
            y                   = 12600,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x01C1,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -8640,
            z                   = 0,
            y                   = 96040,
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

# id: 0x10003 offset: 0x18A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x18A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -8691,
            y           = 3000,
            z           = 54000,
            range       = -10060,
            dword_10    = 0x00001388,
            dword_14    = 0x0000DEEE,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000004,
        ),
        ScenaEventData(
            x           = -29705,
            y           = -3000,
            z           = 53403,
            range       = -31123,
            dword_10    = 0x000007D0,
            dword_14    = 0x0000C4FE,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000007,
        ),
        ScenaEventData(
            x           = -4352,
            y           = -1000,
            z           = 81810,
            range       = -10405,
            dword_10    = 0x000003E8,
            dword_14    = 0x000142A8,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000A,
        ),
        ScenaEventData(
            x           = -5850,
            y           = -1000,
            z           = 80880,
            range       = -10140,
            dword_10    = 0x000007D0,
            dword_14    = 0x00014438,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000C,
        ),
        ScenaEventData(
            x           = -43330,
            y           = -3000,
            z           = 38850,
            range       = -46440,
            dword_10    = 0xFFFFFC18,
            dword_14    = 0x0000A046,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000008,
        ),
    )

# id: 0x10005 offset: 0x22A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x22A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_23D',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    SetMapFlags(0x10000000)
    Event(0, 0x0003)

    def _loc_23D(): pass

    label('loc_23D')

    Return()

# id: 0x0001 offset: 0x23E
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -145000, -73000, 196678)
    OP_71(0x0001, 0x0004)
    PlaySE(460, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x25B
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_270',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_270(): pass

    label('loc_270')

    Return()

# id: 0x0003 offset: 0x271
@scena.Code('func_03_271')
def func_03_271():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    FadeIn(2000, 0)
    CameraMove(-7046, 500, 43491, 0)
    CameraSetDistance(5900, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0101, -9345, 0, 78200, 180)
    SetChrPos(0x0102, -10370, 0, 78100, 180)
    SetChrPos(0x0104, -8638, 0, 79300, 180)
    SetChrPos(0x0103, -9788, 0, 79400, 180)

    @scena.Lambda('lambda_02EE')
    def lambda_02EE():
        OP_6C(327000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_02EE)

    Sleep(1000)

    @scena.Lambda('lambda_0303')
    def lambda_0303():
        OP_67(0, 4100, -10000, 7000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0303)

    @scena.Lambda('lambda_031B')
    def lambda_031B():
        CameraMove(-12358, 3550, 46969, 7000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_031B)

    CameraSetDistance(3547, 7000)
    FadeOut(1000, 0, -1)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    OP_0D()
    NewScene('ED6_DT01/T1511._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x34E
@scena.Code('func_04_34E')
def func_04_34E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006D, 2, 0x36A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 7, 0x34F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_72E',
    )

    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0069, 7, 0x34F))
    OP_28(0x0038, 0x01, 0x0200)
    SetChrPos(0x0009, -8576, 0, 86453, 0)
    SetChrPos(0x000A, -7848, 0, 86453, 0)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    SetChrDirection(0x0000, 0, 400)
    SetChrDirection(0x0001, 0, 400)
    SetChrDirection(0x0002, 0, 400)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F8',
    )

    ChrTalk(
        0x0101,
        (
            '#0010031182V#004F那、那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_445')

    def _loc_3F8(): pass

    label('loc_3F8')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_425',
    )

    ChrTalk(
        0x0102,
        (
            '#0020031183V#012F好像来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_445')

    def _loc_425(): pass

    label('loc_425')

    ChrTalk(
        0x0103,
        (
            '#0030031184V#027F有人过来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_445(): pass

    label('loc_445')

    Sleep(100)

    Fade(1000)

    @scena.Lambda('lambda_0455')
    def lambda_0455():
        CameraMove(-8786, 0, 78490, 0)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0455)

    @scena.Lambda('lambda_046D')
    def lambda_046D():
        OP_6C(0, 0)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_046D)

    OP_0D()

    @scena.Lambda('lambda_047E')
    def lambda_047E():
        ChrWalkTo(0x00FE, -8576, 0, 77200, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_047E)

    Sleep(600)

    ChrWalkTo(0x000A, -7848, 0, 78200, 3000, 0x00)

    ChrTalk(
        0x0009,
        (
            '#0290031185V#200F到了……\n',
            '看来我们来得有点早。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x000A, 225, 400)

    ChrTalk(
        0x000A,
        (
            '#0090031186V#210F#2P是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090031187V啊～如果现在是早上就好了，\n',
            '可以在这家旅馆吃上一顿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0009, 45, 400)

    ChrTalk(
        0x0009,
        (
            '#0290031188V#203F别说这种没用的话了。\n',
            '你明知我们现在被王国军通缉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031189V#200F好了，快点走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0009, 0x01, 0x00, 0x0005)
    OP_62(0x000A, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x000A,
        (
            '#0090031190V#213F#2P#15A啊，等等，吉尔哥。',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(1500)

    CreateThread(0x000A, 0x01, 0x00, 0x0006)

    @scena.Lambda('lambda_05F7')
    def lambda_05F7():
        CameraMove(-15030, 0, 60460, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_05F7)

    @scena.Lambda('lambda_060F')
    def lambda_060F():
        OP_6C(225000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_060F)

    WaitForThreadExit(0x000A, 0x0001)
    Sleep(1000)

    SetChrPos(0x0101, -12740, 4000, 55150, 315)
    SetChrPos(0x0102, -11650, 4000, 55060, 315)
    SetChrPos(0x0103, -10600, 4000, 55110, 270)
    CameraMove(-11630, 4000, 55050, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010031191V#002F……果然是这些家伙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031192V#012F好像往栈桥的方向走去了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031193V他们打算做什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031194V#027F反正我们就拭目以待吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031195V别被他们察觉，静静地跟在后面就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    def _loc_72E(): pass

    label('loc_72E')

    Return()

# id: 0x0005 offset: 0x72F
@scena.Code('func_05_72F')
def func_05_72F():
    SetChrDirection(0x00FE, 0, 400)
    ChrWalkTo(0x00FE, -10100, 0, 65400, 3000, 0x00)
    ChrWalkTo(0x00FE, -21690, 0, 55490, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0006 offset: 0x764
@scena.Code('func_06_764')
def func_06_764():
    ChrWalkTo(0x00FE, -10100, 0, 65400, 4000, 0x00)
    ChrWalkTo(0x00FE, -21690, 0, 55490, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0007 offset: 0x792
@scena.Code('func_07_792')
def func_07_792():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 7, 0x34F)),
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 0, 0x350)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7A5',
    )

    Call(0, 0x0009)

    Jump('loc_7B5')

    def _loc_7A5(): pass

    label('loc_7A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 1, 0x351)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 0, 0x350)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_7B5',
    )

    Call(0, 0x000B)

    def _loc_7B5(): pass

    label('loc_7B5')

    Return()

# id: 0x0008 offset: 0x7B6
@scena.Code('func_08_7B6')
def func_08_7B6():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006D, 2, 0x36A)),
            Expr.Return,
        ),
        'loc_7C0',
    )

    Jump('loc_A50')

    def _loc_7C0(): pass

    label('loc_7C0')

    SetScenaFlags(ScenaFlag(0x006D, 2, 0x36A))
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0101, -45460, -2000, 38500, 180)
    SetChrPos(0x0102, -44530, -2000, 39140, 180)
    SetChrPos(0x0103, -45500, -2000, 39550, 180)
    CameraMove(-45030, -2000, 38970, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010031174V#007F#6P唔……一个人都没有呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031175V#505F虽然不知道他们的目的，\n',
            '不过那对兄妹真的会出现吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0102, 225, 400)

    ChrTalk(
        0x0102,
        (
            '#0020031176V#012F#4P目前还没有确实的证据……\n',
            '但如果罗伊德先生的情报没错的话，\n',
            '那他们今晚肯定会出现的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0103, 135, 400)

    ChrTalk(
        0x0103,
        (
            '#0030031177V#022F不过，要是我们随处乱走的话，\n',
            '说不定会打草惊蛇哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031178V那些空贼应该会从街道那边过来，\n',
            '我们最好还是仔细注意门口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010031179V#006F#6P的确是啊……\n',
            '那么躲在哪里守候比较好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031180V#015F#4P能够看到街道方向而又\n',
            '不容易被别人发现的地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031181V#010F看来也只有那里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0038, 0x01, 0x0100)
    EventEnd(0x00)

    def _loc_A50(): pass

    label('loc_A50')

    Return()

# id: 0x0009 offset: 0xA51
@scena.Code('func_09_A51')
def func_09_A51():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 7, 0x34F)),
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 0, 0x350)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1EBA',
    )

    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x006A, 0, 0x350))
    OP_28(0x0038, 0x01, 0x0400)
    SetChrPos(0x0009, -44910, -1970, 38660, 180)
    SetChrPos(0x000A, -44520, -1970, 39860, 180)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)

    @scena.Lambda('lambda_0A9F')
    def lambda_0A9F():
        OP_6C(225000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0A9F)

    CameraMove(-44910, -1970, 38660, 3000)
    SetChrPos(0x0101, -31171, 0, 56060, 180)
    SetChrPos(0x0102, -32244, 0, 56400, 180)
    SetChrPos(0x0103, -30520, 0, 55440, 180)

    ChrTalk(
        0x0009,
        (
            '#0290031203V#200F果然还没来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031204V今天怎么了……\n',
            '平时他们都是很准时的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0090031205V#212F本小姐可不太喜欢那些家伙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090031206V老是摆出一副高傲的架子……\n',
            '而且行事又那么鬼鬼祟祟的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0009, 0, 400)

    ChrTalk(
        0x0009,
        (
            '#0290031207V#200F确实……\n',
            '一群来历不明的家伙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031208V不过没法啦。\n',
            '这可是多伦大哥的命令啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    OP_6C(45000, 0)
    CameraMove(-30885, 0, 55794, 0)
    OP_0D()

    ChrTalk(
        0x0103,
        (
            '#0030031209V#020F（这个距离应该没问题吧……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031210V#006F#5P（嗯，可以清楚听到他们说话呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    OP_6C(225000, 0)
    CameraMove(-44910, -1970, 38660, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#0090031211V#215F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090031212V喂，吉尔哥……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090031213V不觉得多伦大哥最近怪怪的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290031214V#204F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0090031215V#212F真的很怪呢。\n',
            '无缘无故叫我们去劫定期船。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090031216V虽说干这个收获肯定不少，\n',
            '不过现在军队已经全力介入了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090031217V就连那些多管闲事的\n',
            '游击士也插了一脚进来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090031218V而且我们还扣押人质，\n',
            '要求数额这么大的赎金……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090031219V我们是不是干得太过分了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290031220V#200F你在说什么呀？\n',
            '也难怪，毕竟你是个女孩子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031221V身为空贼的觉悟果然还不够啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0090031222V#216F什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290031223V#202F我这可是在称赞你哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031224V#200F如果觉得不适应，\n',
            '也可以自己一个人先回老家嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031225V只要不介意老家有点落后，\n',
            '在那生活倒也挺轻松自在的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031226V不过那里可比这国家冷很多哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0090031227V#214F你、你再这么说我可要生气了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090031228V你没看到我不在的时候，\n',
            '做饭洗衣服这些家务通通没人管吗！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090031229V难道你们还想重现\n',
            '我去洛连特那段时期自己的惨状吗！？',
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
            '#0290031230V#203F好啦好啦……\n',
            '算我刚才说错了，不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031231V#200F不过我还是希望你能想清楚。\n',
            '再跟我们干下去，想回头可就难了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0090031232V#215F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290031233V#203F算了，先不说这些。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031234V其实我也觉得，\n',
            '多伦大哥最近有些奇怪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031235V就算要为抬高赎金而拖延时间，\n',
            '也应该有个限度啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031236V多伦大哥应该不至于\n',
            '蠢到连这一点都想不到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0090031237V#212F多伦大哥……\n',
            '就是在他来了之后才发生变化的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090031238V恐怕只能这样想了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290031239V#200F确实……\n',
            '把那些家伙介绍给我们的人也是他。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031240V总有种被他唆使的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    OP_6C(45000, 0)
    CameraMove(-30885, 0, 55794, 0)
    OP_0D()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1200)

    ChrTalk(
        0x0101,
        (
            '#0010031241V#505F#5P（“他”？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031242V#022F（唔，究竟是指谁呢？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_20(0x000005DC)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020031243V#014F（啊，那是……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010031244V#004F#5P（怎么了？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031245V#012F（……有人来了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_21()
    PlayBGM(81)
    Sleep(100)

    Fade(1000)
    OP_6C(225000, 0)
    CameraMove(-45040, -1970, 29060, 0)

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrDirection(0x0009, 180, 0)
    SetChrDirection(0x000A, 180, 0)
    SetChrPos(0x0008, -45110, -2700, 20060, 180)
    SetChrFlags(0x0008, 0x0040)
    OP_A1(0x0008, 0x0001)
    LoadEffect(0x04, 'map\\\\mp013_00.eff')
    LoadEffect(0x05, 'map\\\\mp013_01.eff')
    PlayEffect(0x04, 0x00, 0x0008, 0, -300, 2200, 180, 0, 0, 600, 100, 3000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x05, 0x01, 0x0008, 0, -300, -1800, 180, 0, 0, 700, 700, 700, 0x00FF, 0, 0, 0, 0)
    ClearChrFlags(0x000B, 0x0004)
    SetChrFlags(0x000B, 0x0020)
    SetChrBattleFlags(0x000B, 0x0020)
    ClearChrFlags(0x000C, 0x0004)
    SetChrFlags(0x000C, 0x0020)
    SetChrBattleFlags(0x000C, 0x0020)
    OP_72(0x0001, 0x0004)
    OP_72(0x0001, 0x0002)
    OP_71(0x0001, 0x0400)
    OP_71(0x0001, 0x0040)
    Yield()
    OP_89(0x000B, -45060, -2000, 21500, 0)
    OP_89(0x000C, -45060, -2000, 20000, 0)
    PlaySE(212, 0x00, 0x64)

    @scena.Lambda('lambda_14F8')
    def lambda_14F8():
        CameraMove(-45380, -1970, 36390, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_14F8)

    @scena.Lambda('lambda_1510')
    def lambda_1510():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 70000, 2400, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1510)

    Sleep(2000)

    @scena.Lambda('lambda_1530')
    def lambda_1530():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 10000, 2200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1530)

    Sleep(800)

    @scena.Lambda('lambda_1550')
    def lambda_1550():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 10000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1550)

    Sleep(700)

    @scena.Lambda('lambda_1570')
    def lambda_1570():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 75000, 1800, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1570)

    Sleep(600)

    StopEffect(0x01, 0x02)

    @scena.Lambda('lambda_1593')
    def lambda_1593():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 75000, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1593)

    Sleep(500)

    @scena.Lambda('lambda_15B3')
    def lambda_15B3():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 50000, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_15B3)

    Sleep(400)

    @scena.Lambda('lambda_15D3')
    def lambda_15D3():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 50000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_15D3)

    PlayEffect(0x04, 0x02, 0x0008, 0, -300, 2400, 180, 0, 0, 1100, 100, 1600, 0x00FF, 0, 0, 0, 0)
    Sleep(400)

    @scena.Lambda('lambda_1628')
    def lambda_1628():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 50000, 800, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1628)

    Sleep(300)

    StopEffect(0x00, 0x02)

    @scena.Lambda('lambda_164B')
    def lambda_164B():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 5000, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_164B)

    Sleep(300)

    @scena.Lambda('lambda_166B')
    def lambda_166B():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 5000, 500, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_166B)

    Sleep(300)

    @scena.Lambda('lambda_168B')
    def lambda_168B():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 5000, 400, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_168B)

    Sleep(300)

    @scena.Lambda('lambda_16AB')
    def lambda_16AB():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 1000, 300, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_16AB)

    StopEffect(0x02, 0x02)
    WaitForThreadExit(0x0000, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0290031246V#200F哟，他们来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031247V还是老样子，和约定的时间分秒不差啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0090031248V#210F哼，就不能偶尔迟到一次\n',
            '或提前一次吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090031249V真是的，一点都不讨人喜欢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0140031250V#280F呵……\n',
            '严守时间是我们的一贯准则。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140031251V如果令你们感到不快，我在此道歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0090031252V#214F我、我是在讽刺你们啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090031253V真是讨厌的家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0009, 0, 400)

    ChrTalk(
        0x0009,
        (
            '#0290031254V#201F#5P算了，别再说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0009, 180, 400)

    ChrTalk(
        0x0009,
        (
            '#0290031255V#200F总之……\n',
            '我们还是先回正题吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031256V那件事进展得如何了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0140031257V#280F啊啊，陛下终于出面了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140031258V她打算动用自己的资产\n',
            '来支付你们所要求的赎金。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290031259V#202F这、这还真是……\n',
            '竟然让女王陛下亲自掏腰包……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031260V看来这件事也到了尾声了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0090031261V#210F王国军方面怎么样了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090031262V他们应该不会发现\n',
            '我们的据点在那种地方吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0140031263V#280F暂时还不会。\n',
            '不过这也只是时间上的问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140031264V我这里收到情报，\n',
            '游击士协会的人也在行动了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0140031265V总之，成功之后，\n',
            '你们就得马上舍弃那个基地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0290031266V#200F嗯，没问题。\n',
            '不过就是个偶然发现的临时根据地而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0290031267V大哥肯定不会舍不得那里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(-30885, 0, 55794, 0)
    SetChrDirection(0x0101, 180, 0)
    OP_6C(45000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010031268V#002F#5P（又有奇怪的人出现了。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031269V（雪拉姐，怎么办？\n',
            '　一口气冲出去把他们抓住吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0103, 270, 400)

    ChrTalk(
        0x0103,
        (
            '#0030031270V#026F（还不行……\n',
            '　比起这样做，我反而有个良策。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031271V#004F#5P（良策？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031272V#027F（既然那对兄妹出现了，\n',
            '　那这附近应该会停泊有空贼飞艇。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031273V#027F（这次一定不能再让他们逃走，\n',
            '　我们可以先找出空贼飞艇让他们无处可逃。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031274V#006F#5P（原来是这样啊……\n',
            '　我们要先截断他们的退路。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010031275V#006F#5P（我赞成这样做，约修亚你呢？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031276V#510F（………………………………）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031277V#505F#5P（你怎么了……？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031278V#014F（啊、啊啊……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031279V（先找出空贼飞艇的确是个良策，\n',
            '　嗯，我也赞同这个做法。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031280V#002F#5P（……你没事吧？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031281V（怎么了，这么凝重的脸色？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031282V#013F（没什么……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031283V（可能是错觉吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031284V#002F#5P（………………？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031285V#020F（看来还有一点时间。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031286V（趁他们还没有谈完，\n',
            '　我们赶快到街道找空贼飞艇吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    OP_20(0x000005DC)
    Sleep(50)

    EventEnd(0x04)
    OP_21()
    OP_1E()

    def _loc_1EBA(): pass

    label('loc_1EBA')

    Return()

# id: 0x000A offset: 0x1EBB
@scena.Code('func_0A_1EBB')
def func_0A_1EBB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 1, 0x351)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 0, 0x350)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1F51',
    )

    EventBegin(0x00)
    OP_20(0x000007D0)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '离开川蝉亭的艾丝蒂尔等人\n',
            '到街道去搜索空贼飞艇能停降的地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '之后——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_28(0x0038, 0x01, 0x0800)
    OP_28(0x0039, 0x04, 0x02)
    OP_28(0x0039, 0x04, 0x04)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/R1403._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1F51(): pass

    label('loc_1F51')

    Return()

# id: 0x000B offset: 0x1F52
@scena.Code('func_0B_1F52')
def func_0B_1F52():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 1, 0x351)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 0, 0x350)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2066',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1FB2',
    )

    ChrTalk(
        0x0101,
        (
            '#0010031287V#006F（得先控制住空贼艇才行。\n',
            '　赶快去街道上找找吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_204B')

    def _loc_1FB2(): pass

    label('loc_1FB2')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_200C',
    )

    ChrTalk(
        0x0102,
        (
            '#0020031288V#012F（我们要首先控制空贼艇……\n',
            '　去街道周边地区搜索一下吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_204B')

    def _loc_200C(): pass

    label('loc_200C')

    ChrTalk(
        0x0103,
        (
            '#0030031289V#022F（没时间了……\n',
            '　要赶快去街道上找到空贼艇。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_204B(): pass

    label('loc_204B')

    ChrWalkTo(0x0000, -28790, 0, 52000, 2000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_2066(): pass

    label('loc_2066')

    Return()

# id: 0x000C offset: 0x2067
@scena.Code('func_0C_2067')
def func_0C_2067():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 7, 0x34F)),
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 0, 0x350)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2172',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_20C5',
    )

    ChrTalk(
        0x0101,
        (
            '#0010031196V#006F（啊，这边是街道。\n',
            '　现在最好去栈桥那边看看。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2154')

    def _loc_20C5(): pass

    label('loc_20C5')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2117',
    )

    ChrTalk(
        0x0102,
        (
            '#0020031197V#012F（去街道上也没有用……\n',
            '　现在要赶快去栈桥那边。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2154')

    def _loc_2117(): pass

    label('loc_2117')

    ChrTalk(
        0x0103,
        (
            '#0030031198V#022F（这边是街道……\n',
            '　现在要赶快去栈桥那边。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2154(): pass

    label('loc_2154')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_228E')

    def _loc_2172(): pass

    label('loc_2172')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            (Expr.TestScenaFlags, ScenaFlag(0x006A, 0, 0x350)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_228E',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2196',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_219D')

    def _loc_2196(): pass

    label('loc_2196')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_219D(): pass

    label('loc_219D')

    @scena.Lambda('lambda_21A3')
    def lambda_21A3():
        ChrTurnDirection(0x0101, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_21A3)

    @scena.Lambda('lambda_21B1')
    def lambda_21B1():
        ChrTurnDirection(0x0102, 0x0103, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_21B1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006D, 2, 0x36A)),
            Expr.Return,
        ),
        'loc_221C',
    )

    ChrTalk(
        0x0103,
        (
            '#0030031199V#022F现在没有回到街道上的必要。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031200V要先找到能够监视\n',
            '街道方向来人的地点。',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2272')

    def _loc_221C(): pass

    label('loc_221C')

    ChrTalk(
        0x0103,
        (
            '#0030031201V#022F现在没有回到街道上的必要。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031202V还是先去栈桥那边巡视一下吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    def _loc_2272(): pass

    label('loc_2272')

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_228E(): pass

    label('loc_228E')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
