import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0301_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0301   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0301.x'
    header.mapIndex       = 15
    header.bgm            = 84
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
    ]

# id: 0x10001 offset: 0x19E
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
    )

# id: 0x10002 offset: 0x1FE
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1FE
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1FE
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1FE
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_208',
    )

    Jump('loc_20F')

    def _loc_208(): pass

    label('loc_208')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_20F',
    )

    def _loc_20F(): pass

    label('loc_20F')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_223'),
        (0x00000002, 'loc_28E'),
        (0x00000003, 'loc_326'),
        (-1, 'loc_32D'),
    )

    def _loc_223(): pass

    label('loc_223')

    MapClearFlags(0x00000001)
    ChrSetChipByIndex(0x0008, 2)
    ChrSetPos(0x0008, -6220, 3450, 4390, 180)
    ChrSetFlags(0x0008, 0x0004)

    @scena.Lambda('lambda_0249')
    def lambda_0249():
        OP_99(0x00FE, 0x00, 0x07, 800)
        Yield()

        Jump('lambda_0249')

    DispatchAsync2(0x0008, 0x0001, lambda_0249)

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
    Event(0, func_03_46A)

    Jump('loc_32D')

    def _loc_28E(): pass

    label('loc_28E')

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
    FadeIn(500, 0)
    Event(0, func_07_BCB)

    Jump('loc_32D')

    def _loc_326(): pass

    label('loc_326')

    Event(0, func_02_352)

    Jump('loc_32D')

    def _loc_32D(): pass

    label('loc_32D')

    Return()

# id: 0x0001 offset: 0x32E
@scena.Code('func_01_32E')
def func_01_32E():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_338',
    )

    Jump('loc_33F')

    def _loc_338(): pass

    label('loc_338')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_33F',
    )

    def _loc_33F(): pass

    label('loc_33F')

    OP_16(0x02, 4000, -125000, -133000, 196611)

    Return()

# id: 0x0002 offset: 0x352
@scena.Code('func_02_352')
def func_02_352():
    EventBegin(0x00)
    PlaySE(463, 0x00, 0x64)
    SetScenaFlags(ScenaFlag(0x0072, 0, 0x390))
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    CameraMove(800, -1000, -24180, 0)
    OP_67(0, 5600, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(350000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_03B7')
    def lambda_03B7():
        CameraMove(4000, 0, -1000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_03B7)

    @scena.Lambda('lambda_03CF')
    def lambda_03CF():
        OP_67(0, 8000, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_03CF)

    @scena.Lambda('lambda_03E7')
    def lambda_03E7():
        OP_6C(45000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_03E7)

    Sleep(8000)

    @scena.Lambda('lambda_03FC')
    def lambda_03FC():
        CameraSetDistance(3000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_03FC)

    Sleep(2000)

    FadeOut(2000, 0, -1)
    OP_24(0x01CF, 0x5F)
    Sleep(100)

    OP_24(0x01CF, 0x5A)
    Sleep(100)

    OP_24(0x01CF, 0x55)
    Sleep(100)

    OP_24(0x01CF, 0x50)
    Sleep(100)

    OP_24(0x01CF, 0x4B)
    Sleep(100)

    OP_24(0x01CF, 0x46)
    Sleep(100)

    OP_24(0x01CF, 0x3C)
    Sleep(100)

    OP_23(0x01CF)
    OP_0D()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T0311._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x46A
@scena.Code('func_03_46A')
def func_03_46A():
    EventBegin(0x00)
    MapClearFlags(0x00000001)
    OP_1F(0x64, 0x0000012C)
    ChrSetPos(0x0101, -1860, 3450, 930, 270)
    ChrSetFlags(0x0101, 0x0040)
    CreateThread(0x0101, 0x00, 0x00, func_04_B68)
    CreateThread(0x0008, 0x00, 0x00, func_05_BB1)
    CreateThread(0x0009, 0x00, 0x00, func_06_BCA)
    CameraMove(-5250, 3450, 3230, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(4380, 0)
    OP_6C(226000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_04E5')
    def lambda_04E5():
        OP_6C(45000, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_04E5)

    @scena.Lambda('lambda_04F5')
    def lambda_04F5():
        OP_67(0, 5000, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_04F5)

    CameraSetDistance(2940, 10000)

    @scena.Lambda('lambda_0516')
    def lambda_0516():
        OP_67(0, 8000, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0516)

    CameraSetDistance(2800, 5000)
    Sleep(4000)

    OP_70(0x0002, 60)
    Sleep(500)

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    OP_A5(0x0000)
    OP_21()
    TerminateThread(0x0008, 0x01)
    Sleep(500)

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
    Sleep(1000)

    PlayBGM(15)
    Fade(250)
    ChrSetChipByIndex(0x0008, 0)
    OP_0D()
    Sleep(400)

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#0020000119V#010F早上好，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '是不是把你吵醒了？\n',
            '那我要向你说抱歉……',
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

    @scena.Lambda('lambda_0647')
    def lambda_0647():
        CameraMove(-6350, 3450, 3460, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0647)

    ChrWalkTo(0x0101, -6220, 3450, 2860, 2000, 0x00)
    ChrTurnDirection(0x0101, 0x0008, 400)
    Sleep(100)

    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#001F不过，约修亚也真是的。\n',
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
            '#017F什么姐姐啊……\n',
            '明明和我一样大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#502F啧啧啧，你太天真了。',
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
            '#010F是是，我完全明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#009F呀～你这态度也太敷衍了吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#001F话说回来，这首曲子真的很好听呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#001F旋律明快，却又有点悲伤的意境……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#001F虽然其它的曲子也都不错，\n',
            '不过我最喜欢的还要数这首了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#000F对了……曲名叫什么来着？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#010F『星之所在』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊对对，叫『星之所在』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010000135V#007F啊～要是我也能\n',
            '把口琴吹得这么棒就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '看起来挺简单的，\n',
            '不过真的做起来却很难啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '比如手的动作啊，控制气息啊，\n',
            '我根本配合不起来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#019F比起你擅长的棒术，\n',
            '我倒觉得这个简单多了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#019F关键还是集中力的问题哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#009F那也是，要是让我一动不动地做事情，\n',
            '肯定一会儿就睡着了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#009F这就是所谓的『春眠不觉晓』吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#018F不，我想你搞错意思了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    ChrSetPos(0x0009, -6050, 0, -2610, 0)
    ChrClearFlags(0x0009, 0x0080)

    NpcTalk(
        0x0009,
        '男人的声音',
        (
            '喂～\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    CameraMove(-6400, 3450, -400, 2000)

    ChrTalk(
        0x0101,
        (
            '#001F啊～老爸，早啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#019F早上好，爸爸。\n',
            '早饭已经准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#080F啊啊，大功告成了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#080F你们俩，趁饭菜还没凉，\n',
            '赶快下来吃吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F明白～！',
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

# id: 0x0004 offset: 0xB68
@scena.Code('func_04_B68')
def func_04_B68():
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

# id: 0x0005 offset: 0xBB1
@scena.Code('func_05_BB1')
def func_05_BB1():
    OP_A6(0x0001)
    Sleep(400)

    ChrTurnDirection(0x00FE, 0x0009, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_A6(0x0001)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0006 offset: 0xBCA
@scena.Code('func_06_BCA')
def func_06_BCA():
    Return()

# id: 0x0007 offset: 0xBCB
@scena.Code('func_07_BCB')
def func_07_BCB():
    EventBegin(0x00)
    CameraSetDistance(3000, 0)
    CreateThread(0x0102, 0x00, 0x00, func_08_1528)
    CreateThread(0x0009, 0x00, 0x00, func_09_156B)
    PlaySE(463, 0x00, 0x64)
    ChrClearFlags(0x0101, 0x0080)
    ChrClearFlags(0x0101, 0x0008)
    ChrSetPos(0x0101, 0, 0, 0, 0)
    ChrClearFlags(0x0102, 0x0080)
    ChrClearFlags(0x0102, 0x0008)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x0009, 0x0008)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetPos(0x0009, 9600, 620, -2310, 90)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    CameraMove(7500, 450, 1022, 8000)
    OP_A5(0x0002)
    OP_67(0, 6710, -10000, 4000)
    OP_0D()
    OP_70(0x0001, 60)
    OP_73(0x0001)
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    Sleep(1000)

    OP_72(0x0001, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_70(0x0001, 0)
    OP_A5(0x0001)
    OP_71(0x0001, 0x0800)

    ChrTalk(
        0x0102,
        (
            '#0020001221V#015F……爸爸。',
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
            '#0020001223V#010F喝这么多酒，\n',
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
            '#0020001225V#017F还是免了。\n',
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
            '#0160001227V#081F哈哈……\n',
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
            '#0020001229V#015F…………………………',
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
            '#0020001232V#014F埃雷波尼亚帝国……',
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
            '#0020001236V#010F我知道了。\n',
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
            '#0160001238V她已经是游击士了，\n',
            '不好好学会照顾自己怎么行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001239V#010F艾丝蒂尔能行的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001240V#010F她有天生的直觉。虽然平常有点粗枝大叶，\n',
            '但在武术方面也算是个天才。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001241V#019F所以一定能成为一流的游击士。',
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
            '#0160001246V#080F已经过了五年了啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160001247V时间真是转瞬即逝啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020001248V#015F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001249V#010F真的是转瞬即逝。',
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
            '#0020001254V#015F所以我……再一次说抱歉了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0160001255V#085F……你没必要道歉啊。',
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
            '#0020001260V#013F……嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001261V#015F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001262V#010F#50W谢谢您……爸爸……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0009, 0xFF)
    OP_20(0x000009C4)
    FadeOut(2000, 0, -1)
    OP_24(0x01CF, 0x5F)
    Sleep(100)

    OP_24(0x01CF, 0x5A)
    Sleep(100)

    OP_24(0x01CF, 0x55)
    Sleep(100)

    OP_24(0x01CF, 0x50)
    Sleep(100)

    OP_24(0x01CF, 0x4B)
    Sleep(100)

    OP_24(0x01CF, 0x46)
    Sleep(100)

    OP_24(0x01CF, 0x3C)
    Sleep(100)

    OP_23(0x01CF)
    OP_0D()
    OP_21()
    Sleep(1000)

    OP_AD('ED6_DT04/C_VIS040._CH', 0x0000, 0x0000, 0x00000064)
    Sleep(4000)

    OP_56(0x02)
    OP_AE(0x000000C8)
    Sleep(2000)

    MapClearFlags(0x02000000)
    NewScene('ED6_DT01/T0700._SN', 1, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x1528
@scena.Code('func_08_1528')
def func_08_1528():
    OP_A6(0x0001)
    ChrWalkTo(0x00FE, 8492, 450, 2741, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x0009, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))
    OP_A6(0x0001)
    ChrWalkTo(0x00FE, 10000, 450, -170, 2000, 0x00)
    ChrTurnDirection(0x00FE, 0x0009, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x0009 offset: 0x156B
@scena.Code('func_09_156B')
def func_09_156B():
    OP_A6(0x0002)
    OP_6C(315000, 8000)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    OP_A6(0x0002)
    ClearScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
