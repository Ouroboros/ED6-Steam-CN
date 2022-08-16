import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1100   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1100.x'
    header.mapIndex       = 1
    header.bgm            = 11
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
            dword_00        = 0x0000BB80,
            dword_04        = 0xFFFFF448,
            dword_08        = 0x00006978,
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
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01310._CH', 'ED6_DT07/CH01310P._CP'),
        ('ED6_DT07/CH02030._CH', 'ED6_DT07/CH02030P._CP'),
        ('ED6_DT07/CH02100._CH', 'ED6_DT07/CH02100P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH02070._CH', 'ED6_DT07/CH02070P._CP'),
    ]

# id: 0x10001 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 52155,
            z                   = -3000,
            y                   = 17688,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 48810,
            z                   = -3000,
            y                   = 27604,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 72117,
            z                   = 3000,
            y                   = 28437,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0004,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '王国军士兵',
            x                   = 36188,
            z                   = 0,
            y                   = 16750,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0005,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '王国军军官',
            x                   = 48683,
            z                   = -3000,
            y                   = 29357,
            direction           = 270,
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
            name                = '穿黑衣的将校',
            x                   = 48626,
            z                   = 0,
            y                   = 39390,
            direction           = 270,
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
            name                = '女性军官',
            x                   = 47692,
            z                   = 0,
            y                   = 39390,
            direction           = 270,
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
            name                = '奈尔',
            x                   = -620,
            z                   = -1000,
            y                   = -3500,
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
            name                = '朵洛希',
            x                   = -620,
            z                   = -1000,
            y                   = -3500,
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
            name                = '安塞尔新街方向',
            x                   = 47970,
            z                   = -3000,
            y                   = 4220,
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
        ScenaNpcData(
            name                = '柏斯市·北街区',
            x                   = 48070,
            z                   = 0,
            y                   = 48590,
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

# id: 0x10002 offset: 0x23A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x23A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 41890,
            y           = -6000,
            z           = 37580,
            range       = 56300,
            dword_10    = 0xFFFFFC18,
            dword_14    = 0x00004A88,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000A,
        ),
        ScenaEventData(
            x           = 53090,
            y           = -3000,
            z           = 20940,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000000F,
        ),
        ScenaEventData(
            x           = 55320,
            y           = -3000,
            z           = 33040,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000010,
        ),
    )

# id: 0x10004 offset: 0x29A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x29A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_323',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 5, 0x32D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 0, 0x338)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_323',
    )

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x0008, 48000, -3000, 30522, 180)
    ChrSetPos(0x0009, 49200, -3000, 30522, 180)
    ChrSetPos(0x000A, 48000, -3000, 31900, 180)
    ChrSetPos(0x000B, 49200, -3000, 31900, 180)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)

    def _loc_323(): pass

    label('loc_323')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_331',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_0C_1F67)

    def _loc_331(): pass

    label('loc_331')

    Return()

# id: 0x0001 offset: 0x332
@scena.Code('func_01_332')
def func_01_332():
    OP_16(0x02, 4000, -80000, -100000, 196672)

    If(
        (
            (Expr.Eval, "OP_42(0x0033)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_35A',
    )

    OP_1B(0x0D, 0x00, 0x000D)

    Jump('loc_367')

    def _loc_35A(): pass

    label('loc_35A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 0, 0x308)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_367',
    )

    OP_1B(0x0D, 0x00, 0x000D)

    def _loc_367(): pass

    label('loc_367')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_387',
    )

    OP_1B(0x0D, 0x00, 0x000D)
    OP_1B(0x00, 0x00, 0x000E)
    OP_1B(0x01, 0x00, 0x000E)
    OP_1B(0x02, 0x00, 0x000E)

    def _loc_387(): pass

    label('loc_387')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 4, 0x35C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_399',
    )

    OP_10(0x0E, 0x01)
    OP_10(0x05, 0x00)

    def _loc_399(): pass

    label('loc_399')

    Return()

# id: 0x0002 offset: 0x39A
@scena.Code('func_02_39A')
def func_02_39A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3AF',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_39A')

    def _loc_3AF(): pass

    label('loc_3AF')

    Return()

# id: 0x0003 offset: 0x3B0
@scena.Code('func_03_3B0')
def func_03_3B0():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_431',
    )

    ChrWalkTo(0x00FE, 48120, -3000, 32200, 2000, 0x00)
    Sleep(500)

    ChrSetDirection(0x00FE, 90, 500)
    Sleep(500)

    ChrSetDirection(0x00FE, 270, 500)
    Sleep(500)

    ChrSetDirection(0x00FE, 180, 500)
    ChrWalkTo(0x00FE, 48100, -3000, 19750, 2000, 0x00)
    Sleep(300)

    Sleep(500)

    ChrSetDirection(0x00FE, 90, 500)
    Sleep(500)

    ChrSetDirection(0x00FE, 270, 500)
    Sleep(500)

    ChrSetDirection(0x00FE, 0, 500)

    Jump('func_03_3B0')

    def _loc_431(): pass

    label('loc_431')

    Return()

# id: 0x0004 offset: 0x432
@scena.Code('func_04_432')
def func_04_432():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_455',
    )

    OP_8D(0x00FE, 75166, 31996, 63100, 26500, 2000)

    Jump('func_04_432')

    def _loc_455(): pass

    label('loc_455')

    Return()

# id: 0x0005 offset: 0x456
@scena.Code('func_05_456')
def func_05_456():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_50C',
    )

    Sleep(2000)

    ChrWalkTo(0x00FE, 21570, 0, 16747, 2000, 0x00)
    Sleep(1000)

    ChrWalkTo(0x00FE, 20190, 3000, 32182, 2000, 0x00)
    Sleep(2000)

    ChrWalkTo(0x00FE, 20420, 3000, 28362, 2000, 0x00)
    Sleep(1000)

    ChrWalkTo(0x00FE, 23300, 3000, 27654, 2000, 0x00)
    Sleep(4000)

    ChrWalkTo(0x00FE, 21645, 3000, 26374, 2000, 0x00)
    ChrWalkTo(0x00FE, 21570, 0, 16747, 2000, 0x00)
    Sleep(2000)

    ChrWalkTo(0x00FE, 36190, 0, 16750, 2000, 0x00)

    Jump('func_05_456')

    def _loc_50C(): pass

    label('loc_50C')

    Return()

# id: 0x0006 offset: 0x50D
@scena.Code('func_06_50D')
def func_06_50D():
    TalkBegin(0x0008)

    ChrTalk(
        0x00FE,
        (
            '你们就是那几个\n',
            '游击士协会的人啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看在市长的份上这次就饶过你们，\n',
            '但是不能再妨碍我们办事哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    Return()

# id: 0x0007 offset: 0x57C
@scena.Code('func_07_57C')
def func_07_57C():
    TalkBegin(0x0009)

    ChrTalk(
        0x00FE,
        (
            '竟然在我们搜索的背后捣乱，\n',
            '公然在大街上实行抢劫……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很漂亮地将了我们一军啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0009)

    Return()

# id: 0x0008 offset: 0x5DA
@scena.Code('func_08_5DA')
def func_08_5DA():
    TalkBegin(0x000A)

    ChrTalk(
        0x00FE,
        (
            '在废坑里的空贼\n',
            '好像是二女一男的团伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '根据传言，\n',
            '其中好像还有小孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '什么，你说他们不是空贼？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000A)

    Return()

# id: 0x0009 offset: 0x64F
@scena.Code('func_09_64F')
def func_09_64F():
    TalkBegin(0x000B)

    ChrTalk(
        0x00FE,
        (
            '摩尔根将军虽然很顽固，\n',
            '但是他指挥得当，是个很厉害的人物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是在１０年前\n',
            '击退帝国军的元老啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，\n',
            '他这次也遇到了如此棘手的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000B)

    Return()

# id: 0x000A offset: 0x6EB
@scena.Code('func_0A_6EB')
def func_0A_6EB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 5, 0x32D)),
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 0, 0x338)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1F38',
    )

    SetScenaFlags(ScenaFlag(0x0067, 1, 0x339))
    OP_28(0x0037, 0x01, 0x0004)
    OP_28(0x0037, 0x01, 0x0008)
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    ChrSetFlags(0x000D, 0x0040)
    ChrSetFlags(0x000E, 0x0040)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000E, 0x0080)

    @scena.Lambda('lambda_072B')
    def lambda_072B():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_072B')

    DispatchAsync2(0x000C, 0x0001, lambda_072B)

    @scena.Lambda('lambda_073C')
    def lambda_073C():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_073C')

    DispatchAsync2(0x0008, 0x0001, lambda_073C)

    @scena.Lambda('lambda_074D')
    def lambda_074D():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_074D')

    DispatchAsync2(0x0009, 0x0001, lambda_074D)

    @scena.Lambda('lambda_075E')
    def lambda_075E():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_075E')

    DispatchAsync2(0x000A, 0x0001, lambda_075E)

    @scena.Lambda('lambda_076F')
    def lambda_076F():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_076F')

    DispatchAsync2(0x000B, 0x0001, lambda_076F)

    ChrTalk(
        0x000C,
        (
            '#2420030395V喂！你们几个！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_07A0')
    def lambda_07A0():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_07A0')

    DispatchAsync2(0x0000, 0x0002, lambda_07A0)

    Sleep(100)

    Fade(1000)

    @scena.Lambda('lambda_07BB')
    def lambda_07BB():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_07BB')

    DispatchAsync2(0x0001, 0x0002, lambda_07BB)

    @scena.Lambda('lambda_07CC')
    def lambda_07CC():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_07CC')

    DispatchAsync2(0x0002, 0x0002, lambda_07CC)

    @scena.Lambda('lambda_07DD')
    def lambda_07DD():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_07DD')

    DispatchAsync2(0x0003, 0x0002, lambda_07DD)

    @scena.Lambda('lambda_07EE')
    def lambda_07EE():
        OP_69(0x000C, 0)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_07EE)

    @scena.Lambda('lambda_07FC')
    def lambda_07FC():
        OP_6C(0, 0)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_07FC)

    @scena.Lambda('lambda_080C')
    def lambda_080C():
        CameraSetDistance(2800, 0)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_080C)

    ChrSetPos(0x0102, 47362, -3000, 27682, 0)
    ChrSetPos(0x0101, 48132, -3000, 27051, 0)
    ChrSetPos(0x0103, 49152, -3000, 27309, 0)
    ChrSetPos(0x0104, 49977, -3000, 28146, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010030396V#501F嗯？怎么了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2420030397V有一句话要忠告你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2420030398V虽说是在为市长办事，\n',
            '但你们压根儿还是普通市民。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2420030399V在调查正紧张进行的时候，\n',
            '别老是在我们面前走来走去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010030400V#509F什、什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030401V#017F说是忠告，其实是警告才对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2420030402V我只是把丑话说在前面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2420030403V你们那么喜欢多管闲事的话，\n',
            '等我们撤退之后，再去调查个够吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2420030404V不自量力只会惹来麻烦，\n',
            '再被招待进牢房可不好吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030405V#009F唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030406V#027F别在意，艾丝蒂尔。\n',
            '反正我们也没有做错任何事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030407V#035F那当然了，\n',
            '狐假虎威之辈根本不足为惧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000C,
        (
            '#2420030408V什、什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000D,
        '男性的声音',
        (
            '#0130030409V#6P……你们在做什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_20(0x000005DC)
    OP_21()
    PlayBGM(101)
    TerminateThread(0x000C, 0xFF)
    ChrSetDirection(0x000C, 0, 400)

    @scena.Lambda('lambda_0B8D')
    def lambda_0B8D():
        CameraMove(48924, -3000, 31700, 2000)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_0B8D)

    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)
    TerminateThread(0x0003, 0xFF)

    @scena.Lambda('lambda_0BC9')
    def lambda_0BC9():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0BC9)

    @scena.Lambda('lambda_0BD7')
    def lambda_0BD7():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0BD7)

    @scena.Lambda('lambda_0BE5')
    def lambda_0BE5():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0BE5)

    @scena.Lambda('lambda_0BF3')
    def lambda_0BF3():
        ChrTurnDirection(0x00FE, 0x000D, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0BF3)

    @scena.Lambda('lambda_0C01')
    def lambda_0C01():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_0C01')

    DispatchAsync2(0x0000, 0x0001, lambda_0C01)

    @scena.Lambda('lambda_0C12')
    def lambda_0C12():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_0C12')

    DispatchAsync2(0x0001, 0x0001, lambda_0C12)

    @scena.Lambda('lambda_0C23')
    def lambda_0C23():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_0C23')

    DispatchAsync2(0x0002, 0x0001, lambda_0C23)

    @scena.Lambda('lambda_0C34')
    def lambda_0C34():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_0C34')

    DispatchAsync2(0x0003, 0x0001, lambda_0C34)

    Sleep(1000)

    @scena.Lambda('lambda_0C4A')
    def lambda_0C4A():
        ChrWalkTo(0x000D, 48626, -3000, 31225, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0C4A)

    Sleep(600)

    @scena.Lambda('lambda_0C6A')
    def lambda_0C6A():
        ChrWalkTo(0x000E, 47692, -3000, 31909, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0C6A)

    @scena.Lambda('lambda_0C85')
    def lambda_0C85():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_0C85')

    DispatchAsync2(0x0008, 0x0002, lambda_0C85)

    @scena.Lambda('lambda_0C96')
    def lambda_0C96():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_0C96')

    DispatchAsync2(0x0009, 0x0002, lambda_0C96)

    @scena.Lambda('lambda_0CA7')
    def lambda_0CA7():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_0CA7')

    DispatchAsync2(0x000A, 0x0002, lambda_0CA7)

    @scena.Lambda('lambda_0CB8')
    def lambda_0CB8():
        ChrTurnDirection(0x00FE, 0x000D, 0)
        Yield()

        Jump('lambda_0CB8')

    DispatchAsync2(0x000B, 0x0002, lambda_0CB8)

    Sleep(900)

    @scena.Lambda('lambda_0CCE')
    def lambda_0CCE():
        ChrMoveTo(0x00FE, 49863, -3000, 32095, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0CCE)

    @scena.Lambda('lambda_0CE9')
    def lambda_0CE9():
        ChrMoveTo(0x00FE, 50983, -3000, 32095, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0CE9)

    Sleep(500)

    @scena.Lambda('lambda_0D09')
    def lambda_0D09():
        ChrMoveTo(0x00FE, 49863, -3000, 30825, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0D09)

    @scena.Lambda('lambda_0D24')
    def lambda_0D24():
        ChrMoveTo(0x00FE, 50983, -3000, 30825, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0D24)

    WaitForThreadExit(0x000E, 0x0001)

    ChrTalk(
        0x000C,
        (
            '#2420030410V是、是上校！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0130030411V#112F#5P身为王国军的军人，\n',
            '竟然在这里威胁善良的市民……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130030412V真是的，简直不知廉耻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2420030413V可、可是上校，\n',
            '这几个家伙都不是普通人啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2420030414V他们是游击士啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0130030415V#113F#5P啊，原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130030416V#112F所以你们更不应如此无礼，\n',
            '军队和协会向来就存在合作关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130030417V难道你们想煽动两方对立吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2420030418V可、可我这也是\n',
            '遵照将军的意思行事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0130030419V#115F#5P你错了。这样做只会\n',
            '给摩尔根将军增添无谓的麻烦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130030420V#110F这里就交给我处理吧。\n',
            '你召集好自己的部下马上撤走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2420030421V可、可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0130030422V#110F#5P从早上就开始调查，\n',
            '应该已经收集到足够的情报了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130030423V至于将军那里，\n',
            '我稍后会亲自向他交代。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130030424V你们还有什么疑问吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2420030425V明、明白……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000C, 0xFF)
    ChrSetDirection(0x000C, 45, 400)

    @scena.Lambda('lambda_1075')
    def lambda_1075():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_1075')

    DispatchAsync2(0x0008, 0x0002, lambda_1075)

    @scena.Lambda('lambda_1086')
    def lambda_1086():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_1086')

    DispatchAsync2(0x0009, 0x0002, lambda_1086)

    @scena.Lambda('lambda_1097')
    def lambda_1097():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_1097')

    DispatchAsync2(0x000A, 0x0002, lambda_1097)

    @scena.Lambda('lambda_10A8')
    def lambda_10A8():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_10A8')

    DispatchAsync2(0x000B, 0x0002, lambda_10A8)

    Sleep(400)

    ChrTalk(
        0x000C,
        (
            '#2420030426V撤退！\n',
            '返回哈肯大门！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_10E5')
    def lambda_10E5():
        CameraMove(48683, -3000, 30000, 2000)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_10E5)

    OP_62(0x000C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x000C, 90, 400)
    CreateThread(0x000C, 0x01, 0x00, func_0B_1F39)
    Sleep(700)

    CreateThread(0x0009, 0x01, 0x00, func_0B_1F39)
    Sleep(300)

    CreateThread(0x0008, 0x01, 0x00, func_0B_1F39)
    Sleep(400)

    CreateThread(0x000B, 0x01, 0x00, func_0B_1F39)
    Sleep(400)

    CreateThread(0x000A, 0x01, 0x00, func_0B_1F39)
    Sleep(1500)

    ChrTalk(
        0x000D,
        (
            '#0130030427V#115F#5P那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x000D, 48626, -3000, 29357, 2000, 0x00)

    ChrTalk(
        0x000D,
        (
            '#0130030428V#110F#5P游击士协会的各位，\n',
            '刚才我的同僚说了些失礼的话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130030429V请允许我代他们说声抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030430V#020F没什么，您太客气了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030431V其实我们也有失言的地方，\n',
            '这次就算扯平了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0130030432V#110F#5P你这么说是最好不过了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130030433V……我之前也说过，\n',
            '军队和协会向来就存在合作关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130030434V而作为王国的重要组织，\n',
            '两者的关系更是互不可缺。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130030435V对于最近发生的一系列事件，\n',
            '我十分期待你们会有出色的表现。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030436V#021F呵呵，我们会更加努力，\n',
            '一定不会让您失望的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030437V#008F（看、看起来……\n',
            '　是个超级正派的人呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030438V#010F（嗯……他是谁呢？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0610030439V#181F上校……\n',
            '已经到时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000D, 0x00000000, 2300, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x000D,
        (
            '#0130030440V#113F#5P噢，是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130030441V#110F那么各位……\n',
            '我这就先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000D, 0, 400)
    ChrWalkTo(0x000D, 48626, -3000, 30225, 2000, 0x00)
    Sleep(400)

    ChrTalk(
        0x000D,
        (
            '#0130030442V#115F#5P……啊，对了。\n',
            '我还没有报上名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000D, 0x0101, 400)
    Sleep(400)

    NpcTalk(
        0x000D,
        '理查德上校',
        (
            '#0130030443V#110F#5P王国军上校，理查德。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130030444V如果有什么事情不妨和我联系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    ChrSetDirection(0x000D, 0, 400)

    @scena.Lambda('lambda_156A')
    def lambda_156A():
        ChrWalkTo(0x000D, 48626, 0, 39390, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_156A)

    Sleep(900)

    ChrSetDirection(0x000E, 0, 400)

    @scena.Lambda('lambda_1591')
    def lambda_1591():
        ChrWalkTo(0x000E, 47692, 0, 39390, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1591)

    OP_21()
    OP_1E()
    WaitForThreadExit(0x000E, 0x0001)
    ChrSetFlags(0x000D, 0x0080)
    ChrSetFlags(0x000E, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#0010030445V#505F理查德上校……\n',
            '好像在哪听过这个名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030446V#010F嗯，奈尔先生提过这个人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020030447V王国军情报部的负责人，\n',
            '据说是位十分能干的年轻将校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030448V#506F啊，这样啊☆',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030449V#006F不过，以军人来讲，\n',
            '也算是一位通情达理的人物呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030450V#021F嗯，年纪才三十出头，\n',
            '长相也十分之帅气哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030451V比起军人，更适合成为政治家吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)
    TerminateThread(0x0003, 0xFF)
    ChrSetFlags(0x000F, 0x0040)
    ChrSetFlags(0x0010, 0x0040)
    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 55617, -2500, 33010, 270)
    ChrSetPos(0x0010, 55617, -2500, 33010, 270)

    NpcTalk(
        0x000F,
        '男人的声音',
        (
            '#0270030452V#3P喂，你们几个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_17A9')
    def lambda_17A9():
        CameraMove(49974, -3000, 30500, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_17A9)

    @scena.Lambda('lambda_17C1')
    def lambda_17C1():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_17C1')

    DispatchAsync2(0x0000, 0x0001, lambda_17C1)

    @scena.Lambda('lambda_17D2')
    def lambda_17D2():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_17D2')

    DispatchAsync2(0x0001, 0x0001, lambda_17D2)

    @scena.Lambda('lambda_17E3')
    def lambda_17E3():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_17E3')

    DispatchAsync2(0x0002, 0x0001, lambda_17E3)

    @scena.Lambda('lambda_17F4')
    def lambda_17F4():
        ChrTurnDirection(0x00FE, 0x000F, 0)
        Yield()

        Jump('lambda_17F4')

    DispatchAsync2(0x0003, 0x0001, lambda_17F4)

    @scena.Lambda('lambda_1805')
    def lambda_1805():
        ChrWalkTo(0x00FE, 50270, -3000, 31257, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1805)

    ChrClearFlags(0x0010, 0x0080)
    Sleep(500)

    @scena.Lambda('lambda_182A')
    def lambda_182A():
        ChrWalkTo(0x00FE, 51420, -3000, 30953, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_182A)

    OP_62(0x0000, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0001, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0002, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0003, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    WaitForThreadExit(0x000F, 0x0001)
    ChrTurnDirection(0x000F, 0x0101, 400)
    WaitForThreadExit(0x0010, 0x0001)
    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x000F,
        (
            '#0270030453V#140F刚才穿黑衣服的军人是谁啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270030454V这身打扮好像在哪见过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030455V#006F#3P难道你没见过他吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030456V他就是你之前提到的那个\n',
            '掌管情报部的理查德上校啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '#0270030457V#143F什、什么————？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270030458V喂喂，这是真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030459V#004F#3P嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030460V#010F#3P他本人亲口报上自己的名字，\n',
            '我想应该不会有错的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#0270030461V#141F没想到能在这种地方\n',
            '碰到如此难得一见的人物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0010, 400)

    ChrTalk(
        0x000F,
        (
            '#0270030462V#144F这机会绝对不能放过！\n',
            '朵洛希，我们赶快去追上他！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x000F, 400)

    ChrTalk(
        0x0010,
        (
            '#0280030463V#151F好啊好啊～！\n',
            '虽然不清楚怎么回事～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1B09')
    def lambda_1B09():
        ChrWalkTo(0x000F, 47780, 0, 39390, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1B09)

    Sleep(300)

    ChrWalkTo(0x0010, 47780, 0, 39390, 6000, 0x00)
    ChrSetFlags(0x000F, 0x0080)
    ChrSetFlags(0x0010, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#0010030464V#008F#3P啊，还真有干劲啊～\n',
            '又要去采访了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030465V#021F#4P呵呵，要做报道的话，\n',
            '的确就要首选这样的重要人物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030466V#032F#4P……唔………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)
    TerminateThread(0x0003, 0xFF)

    @scena.Lambda('lambda_1C05')
    def lambda_1C05():
        ChrTurnDirection(0x00FE, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1C05)

    @scena.Lambda('lambda_1C13')
    def lambda_1C13():
        ChrTurnDirection(0x00FE, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1C13)

    @scena.Lambda('lambda_1C21')
    def lambda_1C21():
        ChrTurnDirection(0x00FE, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_1C21)

    @scena.Lambda('lambda_1C2F')
    def lambda_1C2F():
        CameraMove(48950, -3000, 29000, 1200)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_1C2F)

    Sleep(1200)

    ChrTalk(
        0x0101,
        (
            '#0010030467V#004F嗯？怎么了？\n',
            '你会这么认真地板着脸还真是稀奇啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030468V#032F#2P没什么，刚才那位上校……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030469V的确是相当有男子气概，\n',
            '这一点我绝对不吝否认。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030470V不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030471V#014F不过……怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0104, 225, 400)
    OP_62(0x0104, 0x0000012C, 1600, 0x36, 0x39, 0x000000FA, 0x00)

    ChrTalk(
        0x0104,
        (
            '#0040030472V#031F#2P不过想要达到我这种境界，\n',
            '还要继续修行才行哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030473V期待他有更精彩的演出。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010030474V#007F又开始自我陶醉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030475V#019F这种自信到底是从哪涌出来的呢？\n',
            '真有点不可思议啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_63(0x0104)

    ChrTalk(
        0x0103,
        (
            '#0030030476V#020F呵呵，好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030477V既然士兵都撤走了，\n',
            '我们就继续展开调查吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030478V刚才没办法和那些住户交谈，\n',
            '我们再回去打听一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030479V#006F嗯，明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    def _loc_1F38(): pass

    label('loc_1F38')

    Return()

# id: 0x000B offset: 0x1F39
@scena.Code('func_0B_1F39')
def func_0B_1F39():
    ChrWalkTo(0x00FE, 52844, -3000, 28844, 5000, 0x00)
    ChrWalkTo(0x00FE, 56108, -1250, 28905, 5000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000C offset: 0x1F67
@scena.Code('func_0C_1F67')
def func_0C_1F67():
    EventBegin(0x00)
    CameraMove(44480, -3000, 27780, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 43850, -3000, 27070, 45)
    ChrSetPos(0x0102, 45240, -3000, 27130, 270)
    ChrSetPos(0x0103, 45170, -3000, 28450, 225)
    ChrSetPos(0x0104, 43750, -3000, 28620, 180)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0103,
        (
            '#0030030547V#020F虽然这起强盗事件\n',
            '暂时还没有什么重要的线索……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030548V不过却听到了很耐人寻味的话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030549V#035F嗯，同感。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030550V特别是\n',
            '『旅馆的饭菜美味』那一句。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030551V#007F不是这句话吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030552V#000F不过，我听说那里能钓鱼时，\n',
            '也觉得心里痒痒的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030553V但既然没出什么事件，\n',
            '也就没有调查的价值了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030554V#015F不，我的意见正好相反。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020030555V因为发生案件的场所\n',
            '绝对会受到军队的彻底调查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020030556V所以空贼反而应该挑那些\n',
            '风平浪静之处作为活动场所。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030557V#002F对啊……\n',
            '这种说法也很有道理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030558V#022F的确这一连串的事件……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030559V先不说军队里是否有间谍，\n',
            '那些空贼的慎密行事也让人捉摸不透。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030560V我想只靠调查现有案件的话，\n',
            '要找到他们的藏身之处相当困难。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030561V既然他们有可能在旅馆出现，\n',
            '那么我们也就有必要走一趟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030562V#006F原来是这样啊……\n',
            '与其守株待兔，不如先发制人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030563V#035F赞成，那我们出发吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030564V被誉为利贝尔的珍珠——\n',
            '美丽的瓦雷利亚湖，我们来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_1B(0x0D, 0x00, 0xFFFF)
    OP_1B(0x00, 0x00, 0xFFFF)
    OP_1B(0x01, 0x00, 0xFFFF)
    OP_1B(0x02, 0x00, 0xFFFF)
    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x23F8
@scena.Code('func_0D_23F8')
def func_0D_23F8():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_258B',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_241C',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_2423')

    def _loc_241C(): pass

    label('loc_241C')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_2423(): pass

    label('loc_2423')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Return,
        ),
        'loc_249A',
    )

    ChrTalk(
        0x0103,
        (
            '#0030020537V#027F现在去其他地方调查\n',
            '也是没有用的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020538V先听听刚才没有问过的居民\n',
            '是怎么说的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2535')

    def _loc_249A(): pass

    label('loc_249A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2503',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0103,
        (
            '#0030020539V#020F还没有得到\n',
            '重要的情报呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020540V继续在这一带\n',
            '打听打听消息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2535')

    def _loc_2503(): pass

    label('loc_2503')

    ChrTalk(
        0x0103,
        (
            '#0030020541V#020F好了，\n',
            '赶快继续打听情报吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2535(): pass

    label('loc_2535')

    Fade(1000)
    ChrSetPos(0x0000, 47790, -3000, 17080, 0)
    ChrSetPos(0x0001, 47790, -3000, 17080, 0)
    ChrSetPos(0x0002, 47790, -3000, 17080, 0)
    ChrSetPos(0x0003, 47790, -3000, 17080, 0)
    OP_69(0x0000, 0)
    OP_0D()
    EventEnd(0x02)

    Jump('loc_2713')

    def _loc_258B(): pass

    label('loc_258B')

    If(
        (
            (Expr.Eval, "OP_42(0x0033)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_264D',
    )

    EventBegin(0x02)
    ChrTurnDirection(0x0134, 0x0000, 400)

    ChrTalk(
        0x0134,
        (
            '#0370020542V#620F各位要到哪里去呢？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0370020543V市长应该就在\n',
            '柏斯超市视察。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    ChrSetPos(0x0000, 47790, -3000, 17080, 0)
    ChrSetPos(0x0001, 47790, -3000, 17080, 0)
    ChrSetPos(0x0002, 47790, -3000, 17080, 0)
    ChrSetPos(0x0003, 47790, -3000, 17080, 0)
    OP_69(0x0000, 0)
    OP_0D()
    EventEnd(0x02)

    Jump('loc_2713')

    def _loc_264D(): pass

    label('loc_264D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 0, 0x308)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2713',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_266D',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_2674')

    def _loc_266D(): pass

    label('loc_266D')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_2674(): pass

    label('loc_2674')

    ChrTalk(
        0x0103,
        (
            '#0030020544V#020F先回协会支部\n',
            '确认一下现在的状况吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030020545V柏斯支部在北街区。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(1000)
    ChrSetPos(0x0000, 47790, -3000, 17080, 0)
    ChrSetPos(0x0001, 47790, -3000, 17080, 0)
    ChrSetPos(0x0002, 47790, -3000, 17080, 0)
    OP_69(0x0000, 0)
    OP_0D()
    EventEnd(0x02)

    def _loc_2713(): pass

    label('loc_2713')

    Return()

# id: 0x000E offset: 0x2714
@scena.Code('func_0E_2714')
def func_0E_2714():
    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_272C',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_2733')

    def _loc_272C(): pass

    label('loc_272C')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_2733(): pass

    label('loc_2733')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 1, 0x339)),
            Expr.Return,
        ),
        'loc_27AA',
    )

    ChrTalk(
        0x0103,
        (
            '#0030030335V#027F现在去其他地方调查\n',
            '也是没有用的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030336V先听听刚才没有问过的居民\n',
            '是怎么说的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2845')

    def _loc_27AA(): pass

    label('loc_27AA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2813',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0103,
        (
            '#0030030337V#020F还没有得到\n',
            '重要的情报呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030338V继续在这一带\n',
            '打听打听消息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2845')

    def _loc_2813(): pass

    label('loc_2813')

    ChrTalk(
        0x0103,
        (
            '#0030030339V#020F好了，\n',
            '赶快继续打听情报吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2845(): pass

    label('loc_2845')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x000F offset: 0x2861
@scena.Code('func_0F_2861')
def func_0F_2861():
    OP_13(0x0022)

    Return()

# id: 0x0010 offset: 0x2865
@scena.Code('func_10_2865')
def func_10_2865():
    OP_13(0x0024)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
