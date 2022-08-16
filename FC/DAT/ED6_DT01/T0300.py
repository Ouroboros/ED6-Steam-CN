import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0300_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0300   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0300.x'
    header.mapIndex       = 15
    header.bgm            = 88
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
            dword_00        = 0x000007D0,
            dword_04        = 0x00000000,
            dword_08        = 0xFFFFE890,
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
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 15,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00002580,
            dword_04        = 0x0000036B,
            dword_08        = 0x0000012C,
            word_0C         = 0x0004,
            word_0E         = 0x0076,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 15,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00002580,
            dword_04        = 0x0000036B,
            dword_08        = 0x0000012C,
            word_0C         = 0x0004,
            word_0E         = 0x0076,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 15,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00002580,
            dword_04        = 0x0000036B,
            dword_08        = 0x0000012C,
            word_0C         = 0x0004,
            word_0E         = 0x0076,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 15,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0x174
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH00010._CH', 'ED6_DT07/CH00010P._CP'),
        ('ED6_DT07/CH02000._CH', 'ED6_DT07/CH02000P._CP'),
        ('ED6_DT06/CH20030._CH', 'ED6_DT06/CH20030P._CP'),
        ('ED6_DT06/CH20011._CH', 'ED6_DT06/CH20011P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT06/CH20132._CH', 'ED6_DT06/CH20132P._CP'),
    ]

# id: 0x10001 offset: 0x1A6
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '约修亚',
            x                   = 11500,
            z                   = 0,
            y                   = -3400,
            direction           = 135,
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
            name                = '卡西乌斯',
            x                   = 2000,
            z                   = 450,
            y                   = -1200,
            direction           = 90,
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
            name                = '器皿',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 262148,
            chipIndex           = 4,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '艾利兹街道方向',
            x                   = 4110,
            z                   = -1000,
            y                   = -46140,
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

# id: 0x10002 offset: 0x226
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x226
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x226
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 21670,
            triggerZ            = 0,
            triggerY            = -2000,
            triggerRange        = 800,
            actorX              = 21670,
            actorZ              = 1500,
            actorY              = -1980,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000C,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 21670,
            triggerZ            = 0,
            triggerY            = 0,
            triggerRange        = 800,
            actorX              = 21670,
            actorZ              = 1500,
            actorY              = 20,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000D,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 21670,
            triggerZ            = 0,
            triggerY            = 2000,
            triggerRange        = 800,
            actorX              = 21670,
            actorZ              = 1500,
            actorY              = 2020,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x292
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_2A6'),
        (0x00000002, 'loc_311'),
        (0x00000003, 'loc_3B2'),
        (-1, 'loc_436'),
    )

    def _loc_2A6(): pass

    label('loc_2A6')

    MapClearFlags(0x00000001)
    ChrSetChipByIndex(0x0008, 2)
    ChrSetPos(0x0008, -6220, 3450, 4390, 180)
    ChrSetFlags(0x0008, 0x0004)

    @scena.Lambda('lambda_02CC')
    def lambda_02CC():
        OP_99(0x00FE, 0x00, 0x07, 800)
        Yield()

        Jump('lambda_02CC')

    DispatchAsync2(0x0008, 0x0001, lambda_02CC)

    ChrClearFlags(0x0008, 0x0080)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x46),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(7170, 3450, -16520, 0)
    OP_6C(308000, 0)
    FadeIn(2000, 0)
    Event(0, func_05_5C8)

    Jump('loc_436')

    def _loc_311(): pass

    label('loc_311')

    MapClearFlags(0x00000001)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0102, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x0101, 0x0008)
    ChrClearFlags(0x0102, 0x0008)
    ChrClearFlags(0x0009, 0x0008)
    ChrSetPos(0x0102, 6021, 450, 3014, 90)
    ChrSetPos(0x0009, 9600, 500, -2310, 90)
    ChrSetChipByIndex(0x0009, 10)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetPos(0x000A, 10000, 1100, -3300, 0)
    ChrClearFlags(0x000A, 0x0080)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(-2924, 0, -6598, 0)
    OP_6C(48000, 0)
    OP_77(0x07, 0x45, 0x91, 0x00, 0x00000000)
    FadeIn(500, 0)
    Event(0, func_09_102F)

    Jump('loc_436')

    def _loc_3B2(): pass

    label('loc_3B2')

    SetScenaFlags(ScenaFlag(0x0043, 1, 0x219))
    FormationDelMember(0x01, 0xFF)
    FormationDelMember(0x03, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x06, 0xFF)
    FormationDelMember(0x04, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x07, 0xFF)
    FormationAddMember(0x00, 0xFF)
    ChrSetStatus(0x0000, 0x00, 3)
    OP_37(0x00, 0x0000)
    EquipCmd(0x00, 0x00F1)
    EquipCmd(0x00, 0x0001)
    AddCraft(0x0000, 0x0096)
    AddSCraft(0x0000, 0x00E6)
    ChrSetStatus(0x0001, 0x00, 3)
    OP_37(0x01, 0x0000)
    EquipCmd(0x01, 0x001F)
    EquipCmd(0x01, 0x00F1)
    AddCraft(0x0001, 0x00A0)
    AddSCraft(0x0001, 0x00EB)
    MapSetFlags(0x01000000)
    MapSetFlags(0x00800000)
    OP_16(0x00)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetPos(0x0008, -6220, 3450, 4390, 180)
    ChrSetFlags(0x0008, 0x0004)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_04_502)

    Jump('loc_436')

    def _loc_436(): pass

    label('loc_436')

    Return()

# id: 0x0001 offset: 0x437
@scena.Code('func_01_437')
def func_01_437():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_44F',
    )

    OP_B1('t0300_y')

    Jump('loc_458')

    def _loc_44F(): pass

    label('loc_44F')

    OP_B1('t0300_n')

    def _loc_458(): pass

    label('loc_458')

    OP_16(0x02, 4000, -125000, -133000, 196611)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_490',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_482',
    )

    MapSetFlags(0x00000800)

    def _loc_482(): pass

    label('loc_482')

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0xF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_1B(0x00, 0x00, 0x0002)

    def _loc_490(): pass

    label('loc_490')

    Return()

# id: 0x0002 offset: 0x491
@scena.Code('func_02_491')
def func_02_491():
    MapClearFlags(0x00000800)
    OP_1B(0x00, 0x00, 0xFFFF)

    Return()

# id: 0x0003 offset: 0x49C
@scena.Code('func_03_49C')
def func_03_49C():
    EventBegin(0x00)
    CameraMove(-186290, 0, -48440, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    PlayMovie(0x00, 'ed6_op.avi')
    OP_56(0x02)
    FadeOut(2000, 0, -1)
    OP_0D()
    PlayMovie(0x01, '')
    Sleep(2000)

    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x502
@scena.Code('func_04_502')
def func_04_502():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0080)
    PlaySE(450, 0x01, 0x64)
    CameraMove(800, -1000, -24180, 0)
    OP_67(0, 5600, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(350000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_055A')
    def lambda_055A():
        CameraMove(4000, 0, -1000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_055A)

    @scena.Lambda('lambda_0572')
    def lambda_0572():
        OP_67(0, 8000, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0572)

    @scena.Lambda('lambda_058A')
    def lambda_058A():
        OP_6C(45000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_058A)

    Sleep(8000)

    @scena.Lambda('lambda_059F')
    def lambda_059F():
        CameraSetDistance(3000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_059F)

    Sleep(2000)

    FadeOut(2000, 0, -1)
    OP_0D()
    MapSetFlags(0x00100000)
    NewScene('ED6_DT01/T0310._SN', 1, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x5C8
@scena.Code('func_05_5C8')
def func_05_5C8():
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    OP_1F(0x64, 0x000003E8)
    ChrSetPos(0x0101, -1860, 3450, 930, 270)
    ChrSetFlags(0x0101, 0x0040)
    CreateThread(0x0101, 0x00, 0x00, func_06_FCC)
    CreateThread(0x0008, 0x00, 0x00, func_07_1015)
    CreateThread(0x0009, 0x00, 0x00, func_08_102E)
    CameraMove(-5250, 3450, 3230, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(4380, 0)
    OP_6C(226000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_0643')
    def lambda_0643():
        OP_6C(45000, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0643)

    @scena.Lambda('lambda_0653')
    def lambda_0653():
        OP_67(0, 5000, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0653)

    Sleep(5000)

    @scena.Lambda('lambda_0670')
    def lambda_0670():
        OP_67(0, 6200, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0670)

    CameraSetDistance(3000, 10000)
    Sleep(4000)

    OP_70(0x0002, 60)
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_A5(0x0000)
    OP_21()
    TerminateThread(0x0008, 0x01)
    PlaySE(123, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 5)

    @scena.Lambda('lambda_06B7')
    def lambda_06B7():
        OP_99(0x00FE, 0x00, 0x02, 1500)
        Yield()

        Jump('lambda_06B7')

    DispatchAsync2(0x0101, 0x0001, lambda_06B7)

    ChrSetFlags(0x0101, 0x0002)
    Sleep(2000)

    TerminateThread(0x0101, 0x01)

    ChrTalk(
        0x0101,
        (
            '#0010000117V#001F咻——咻——！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000118V不错嘛，约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0101, 0)
    ChrClearFlags(0x0101, 0x0002)
    ChrSetChipByIndex(0x0101, 65535)
    PlayBGM(88)
    Fade(250)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetSubChip(0x0008, 0)
    OP_0D()
    Sleep(400)

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0020000119V#010F早上好，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000120V抱歉。\n',
            '是不是把你吵醒了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000121V#000F没有啊，\n',
            '我已经睡饱了，自然要起床嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_07D4')
    def lambda_07D4():
        CameraMove(-5850, 3450, 4410, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_07D4)

    ChrWalkTo(0x0101, -6220, 3450, 2860, 2000, 0x00)
    ChrTurnDirection(0x0101, 0x0008, 400)
    Sleep(100)

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#0010000122V#001F#2P不过，约修亚也真是的。\n',
            '一大早就这么认真地吹口琴～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000123V呵呵～姐姐我啊，\n',
            '都听得入神了呢㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020000124V#017F#5P什么姐姐啊……\n',
            '明明和我一样大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000125V#502F#2P啧啧啧，你太天真了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000126V虽然我和你同龄，\n',
            '不过在这个家里我可算是前辈哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000127V也可以说是你的师姐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020000128V#010F#5P是是，我完全明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000129V#009F#2P呀～你这态度也太敷衍了吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000130V#501F话说回来，这首曲子真的很好听呢。\n',
            '旋律明快，却又有点悲伤的意境……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000131V虽然其它的曲子也都不错，\n',
            '不过我最喜欢的还要数这首了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000132V#505F对了……曲名叫什么来着？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020000133V#010F#5P『星之所在』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000134V#006F#2P啊对对，叫『星之所在』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000135V#007F啊～\n',
            '要是我也能把口琴吹得这么棒就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000136V看起来挺简单的，\n',
            '不过真的做起来却很难啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020000137V#010F#5P比起你擅长的棒术，\n',
            '我倒觉得这个简单多了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000138V#010F关键还是集中力的问题哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000139V#506F#2P那也是，要是让我一动不动地做事情，\n',
            '肯定一会儿就睡着了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000140V#006F倒是约修亚你不能光喜欢吹口琴，\n',
            '有时候也该表现活跃一点才行啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000141V约修亚的兴趣除了吹口琴，\n',
            '就是读书和修理武器什么的吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000142V#502F在这种时代，\n',
            '老呆在屋里可是不能打动女孩子的心哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020000143V#017F#5P那也没办法，我向来都没什么人缘。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000144V#010F而且我觉得\n',
            '你的兴趣才真是特别呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020000145V比如钓鱼呢，捉虫子呢，\n',
            '还有收集运动鞋什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000146V#007F#2P唔……\n',
            '不行吗？我就是喜欢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000147V#509F不过话说回来，\n',
            '那个捉虫子什么的我早就不玩了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020000148V#019F#5P哦～真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0009, -6050, 0, -2610, 0)
    ChrClearFlags(0x0009, 0x0080)

    NpcTalk(
        0x0009,
        '男人的声音',
        (
            '#0160000149V#1P……喂。\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    CameraMove(-6400, 3450, -400, 1500)

    ChrTalk(
        0x0101,
        (
            '#0010000150V#501F啊～老爸，早啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020000151V#010F早上好，爸爸。\n',
            '早饭已经准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0160000152V#080F啊啊，大功告成了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160000153V你们俩，趁饭菜还没凉，\n',
            '赶快下来吃吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010000154V#006F明白～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0020000155V#010F马上就去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    NewScene('ED6_DT01/T0310._SN', 2, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0xFCC
@scena.Code('func_06_FCC')
def func_06_FCC():
    OP_A6(0x0000)
    ChrSetPos(0x0101, -1860, 3450, 930, 270)
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -3120, 3450, 990, 2000, 0x00)
    ChrClearFlags(0x00FE, 0x0040)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_A6(0x0000)
    ChrTurnDirection(0x00FE, 0x0009, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_A6(0x0000)
    ClearScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Return()

# id: 0x0007 offset: 0x1015
@scena.Code('func_07_1015')
def func_07_1015():
    OP_A6(0x0001)
    Sleep(400)

    ChrTurnDirection(0x00FE, 0x0009, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_A6(0x0001)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0008 offset: 0x102E
@scena.Code('func_08_102E')
def func_08_102E():
    Return()

# id: 0x0009 offset: 0x102F
@scena.Code('func_09_102F')
def func_09_102F():
    EventBegin(0x00)
    OP_77(0x07, 0x45, 0x91, 0x00, 0x00000000)
    CameraSetDistance(3000, 0)
    CreateThread(0x0102, 0x00, 0x00, func_0A_180F)
    CreateThread(0x0009, 0x00, 0x00, func_0B_1852)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0101, 0x0008)
    ChrSetPos(0x0101, 0, 0, 0, 0)
    ChrClearFlags(0x0102, 0x0080)
    ChrClearFlags(0x0102, 0x0008)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0009, 0x0008)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    CameraMove(7500, 450, 1022, 8000)
    OP_A5(0x0002)
    CameraSetDistance(2800, 2000)
    OP_0D()
    OP_70(0x0001, 60)
    OP_73(0x0001)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_A5(0x0001)

    ChrTalk(
        0x0102,
        (
            '#010F……爸爸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0009, 1)
    Sleep(300)

    ChrTalk(
        0x0009,
        (
            '#0160001222V#080F是约修亚啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    CameraMove(10020, 450, -790, 2000)
    OP_A5(0x0001)

    ChrTalk(
        0x0102,
        (
            '#010F喝这么多酒，\n',
            '又会被艾丝蒂尔骂的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0160001224V#080F出发前提提神嘛。\n',
            '要不，你也来一杯吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#018F还是免了。\n',
            '还有，请不要劝未成年人喝酒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001226V#018F况且我又不是雪拉姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#080F哈哈……\n',
            '那个大酒鬼，比我能喝多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001228V#080F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#012F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001230V#012F……看来任务很棘手吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0160001231V#085F现在还没有确实的证据……\n',
            '不过帝国那边似乎已经有动静了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#012F埃雷波尼亚帝国……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001233V#012F就是说很可疑吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0160001234V#082F虽然还没有明显的行动……\n',
            '不过这却反而让人更加怀疑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001235V所以我打算先\n',
            '到帝国大使馆那里打听一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我知道了。\n',
            '艾丝蒂尔就交给我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0160001237V#080F可别太娇惯她哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#080F她已经是游击士了，\n',
            '不好好学会照顾自己怎么行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#011F艾丝蒂尔能行的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#011F她有天生的直觉。虽然平常有点粗枝大叶，\n',
            '但在武术方面也算是个天才。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#011F所以一定能成为一流的游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0160001242V#085F现在还是不谙世事的小孩子呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001243V#085F总有一天她也要\n',
            '依自身的意志来选择前进的道路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001244V#082F……约修亚。\n',
            '这话也同样是对你说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001245V#013F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#085F已经过了５年了啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#085F时间真是转瞬即逝啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#015F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#015F真的是转瞬即逝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0160001250V#082F那时候的话……\n',
            '你还不打算收回吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001251V#013F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001252V#013F对我来说，那已经是最后的底线了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001253V#013F如果连那都不能守护，\n',
            '我……绝对不会原谅自己的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#013F所以我……\n',
            '爸爸……再一次抱歉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#080F……你没必要道歉啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001256V#080F但是，你要记住一件事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001257V#080F不管你选择什么样的道路，\n',
            '都无法抹消这五年的时光。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001258V#080F我和艾丝蒂尔，都是你的家人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001259V#080F无论发生什么事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#013F……嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001261V#013F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#019F谢谢您……爸爸……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0009, 0xFF)
    OP_20(0x000009C4)
    MapClearFlags(0x02000000)
    NewScene('ED6_DT01/T0700._SN', 1, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x180F
@scena.Code('func_0A_180F')
def func_0A_180F():
    OP_A6(0x0001)
    ChrWalkTo(0x00FE, 8492, 450, 2741, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x0009, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_A6(0x0001)
    ChrWalkTo(0x00FE, 10000, 450, -170, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x0009, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x000B offset: 0x1852
@scena.Code('func_0B_1852')
def func_0B_1852():
    OP_A6(0x0002)
    OP_6C(315000, 8000)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    OP_A6(0x0002)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Return()

# id: 0x000C offset: 0x1868
@scena.Code('func_0C_1868')
def func_0C_1868():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_18D4',
    )

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '仔细看能看到上面写着什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '『约修亚大笨蛋』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_1915')

    def _loc_18D4(): pass

    label('loc_18D4')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '竖立着棒术练习用的木桩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    def _loc_1915(): pass

    label('loc_1915')

    TalkEnd(0x00FF)

    Return()

# id: 0x000D offset: 0x1919
@scena.Code('func_0D_1919')
def func_0D_1919():
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '竖立着棒术练习用的木桩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000E offset: 0x195E
@scena.Code('func_0E_195E')
def func_0E_195E():
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '竖立着棒术练习用的木桩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
