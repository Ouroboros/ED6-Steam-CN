import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3172_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3172   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3172.x'
    header.mapIndex       = 1
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
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH02620._CH', 'ED6_DT07/CH02620P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
        ('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP'),
    ]

# id: 0x10001 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '拉赛尔博士',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '玛多克工房长',
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
            name                = '导力器',
            x                   = 20,
            z                   = 700,
            y                   = 39430,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 917506,
            chipIndex           = 2,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '感应妨碍器',
            x                   = 20,
            z                   = 700,
            y                   = 39430,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1179650,
            chipIndex           = 2,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x15A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x15A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 28740,
            y           = -2000,
            z           = 2700,
            range       = 30300,
            dword_10    = 0x000003E8,
            dword_14    = 0xFFFFF060,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000007,
        ),
    )

# id: 0x10004 offset: 0x17A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x17A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_188',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_0A_2903)

    def _loc_188(): pass

    label('loc_188')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_19F',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x5C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_0B_363B)

    def _loc_19F(): pass

    label('loc_19F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_1AD',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, func_0C_455A)

    def _loc_1AD(): pass

    label('loc_1AD')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_1BD'),
        (0x0000006A, 'loc_1E6'),
        (-1, 'loc_1F9'),
    )

    def _loc_1BD(): pass

    label('loc_1BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 7, 0x50F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1D0',
    )

    SetScenaFlags(ScenaFlag(0x00A1, 7, 0x50F))
    Event(0, func_04_53D)

    def _loc_1D0(): pass

    label('loc_1D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 6, 0x55E)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1E3',
    )

    SetScenaFlags(ScenaFlag(0x00AB, 6, 0x55E))
    Event(0, func_0D_4B2E)

    def _loc_1E3(): pass

    label('loc_1E3')

    Jump('loc_1F9')

    def _loc_1E6(): pass

    label('loc_1E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 0, 0x510)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 7, 0x50F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1F6',
    )

    Event(0, func_05_720)

    def _loc_1F6(): pass

    label('loc_1F6')

    Jump('loc_1F9')

    def _loc_1F9(): pass

    label('loc_1F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 7, 0x55F)),
            Expr.Return,
        ),
        'loc_203',
    )

    Jump('loc_220')

    def _loc_203(): pass

    label('loc_203')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_220',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 31850, 0, 30290, 0)

    def _loc_220(): pass

    label('loc_220')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_22A',
    )

    Jump('loc_29A')

    def _loc_22A(): pass

    label('loc_22A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 0, 0x510)),
            Expr.Return,
        ),
        'loc_251',
    )

    ChrClearFlags(0x0008, 0x0080)
    CreateThread(0x0008, 0x00, 0x00, func_02_2AC)
    ChrSetPos(0x0008, 30000, -1000, 8900, 270)

    Jump('loc_29A')

    def _loc_251(): pass

    label('loc_251')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_271',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 28000, 0, 31400, 180)

    Jump('loc_29A')

    def _loc_271(): pass

    label('loc_271')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_29A',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 29950, -1000, 8090, 269)
    CreateThread(0x0008, 0x00, 0x00, func_02_2AC)
    ChrSetFlags(0x0008, 0x0010)

    def _loc_29A(): pass

    label('loc_29A')

    Return()

# id: 0x0001 offset: 0x29B
@scena.Code('func_01_29B')
def func_01_29B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 7, 0x55F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_2AB',
    )

    OP_64(0x00, 0x0001)

    def _loc_2AB(): pass

    label('loc_2AB')

    Return()

# id: 0x0002 offset: 0x2AC
@scena.Code('func_02_2AC')
def func_02_2AC():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2C1',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_2AC')

    def _loc_2C1(): pass

    label('loc_2C1')

    Return()

# id: 0x0003 offset: 0x2C2
@scena.Code('func_03_2C2')
def func_03_2C2():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_539',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_49C',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D3',
    )

    ChrTalk(
        0x00FE,
        (
            '#0540091694V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0540091695V……唔唔………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091696V#010F艾丝蒂尔，这位老爷爷\n',
            '好像精力十分集中地在做什么事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091697V#010F我们又没什么事，\n',
            '还是不要打扰他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091698V#000F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_499')

    def _loc_3D3(): pass

    label('loc_3D3')

    ChrTalk(
        0x00FE,
        (
            '#0540091699V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0540091700V……唔唔………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091701V#010F这位老爷爷\n',
            '好像精力十分集中地在做什么事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091702V#010F我们又没什么事，\n',
            '还是不要打扰他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_499(): pass

    label('loc_499')

    Jump('loc_539')

    def _loc_49C(): pass

    label('loc_49C')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0540091690V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0540091691V……唔唔………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0540091692V问题果然在这里啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0540091693V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_539(): pass

    label('loc_539')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x53D
@scena.Code('func_04_53D')
def func_04_53D():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-380, 0, 8170, 0)
    ChrSetPos(0x0107, -680, 0, -1960, 225)
    ChrSetPos(0x0101, -2700, 0, -3100, 0)
    ChrSetPos(0x0102, -1600, 0, -3600, 0)
    FadeIn(1000, 0)
    CameraMove(-2000, 0, -600, 3000)

    ChrTalk(
        0x0107,
        (
            '#067F#2P嘿嘿……\n',
            '这里就是我家哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)
    Sleep(200)

    ChrSetDirection(0x0101, 0, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010070777V#001F哇～看起来很不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070778V#010F嗯，的确很不错。\n',
            '那么拉赛尔博士现在在哪呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F#2P嗯～爷爷他嘛，\n',
            '我想应该在工房里工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0689')
    def lambda_0689():
        CameraMove(1070, 0, -1350, 1500)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_0689)

    ChrSetDirection(0x0107, 90, 400)
    Sleep(300)

    ChrSetDirection(0x0102, 90, 400)
    ChrSetDirection(0x0101, 90, 400)
    WaitForThreadExit(0x0107, 0x0002)

    ChrTalk(
        0x0107,
        (
            '#0070070780V#060F进去那房间就是了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070781V#006F嗯，ＯＫ。\n',
            '那我们赶快去打个招呼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x720
@scena.Code('func_05_720')
def func_05_720():
    EventBegin(0x00)
    CameraMove(31150, 0, 36720, 0)
    ChrSetFlags(0x0107, 0x0080)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0107, 30900, 0, 36300, 225)
    ChrSetPos(0x0101, 29800, 0, 37500, 180)
    ChrSetPos(0x0102, 31000, 0, 37400, 225)
    ChrSetPos(0x0008, 28000, 0, 31400, 180)
    ChrClearFlags(0x0107, 0x0080)
    ChrClearFlags(0x0102, 0x0080)
    ChrClearFlags(0x0101, 0x0080)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0107,
        (
            '#0070070782V#061F爷爷，我回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(29900, 0, 34680, 1000)
    Sleep(500)

    OP_9E(0x0008, 15, 0, 300, 4000)

    ChrTalk(
        0x0008,
        (
            '#102F#6P……唔唔唔………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070784V这里这样，然后……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    ChrTalk(
        0x0008,
        (
            '#102F#6P………唔唔哦哦……！',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0008, 30, 0, 400, 5000)
    CloseMessageWindow()
    Sleep(200)

    ChrTalk(
        0x0008,
        (
            '#102F#6P………喔喔喔喔……！',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0008, 50, 0, 500, 6000)
    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070787V#065F……啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070788V#501F啊，就是这位吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_08F2')
    def lambda_08F2():
        CameraMove(29760, 0, 33950, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_08F2)

    @scena.Lambda('lambda_090A')
    def lambda_090A():
        ChrWalkTo(0x00FE, 29800, 0, 33900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_090A)

    Sleep(800)

    @scena.Lambda('lambda_092A')
    def lambda_092A():
        ChrWalkTo(0x00FE, 31100, 0, 34000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_092A)

    Sleep(200)

    @scena.Lambda('lambda_094A')
    def lambda_094A():
        ChrWalkTo(0x00FE, 30900, 0, 35100, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_094A)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_096A')
    def lambda_096A():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_096A)

    WaitForThreadExit(0x0107, 0x0001)

    @scena.Lambda('lambda_097D')
    def lambda_097D():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_097D)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_0990')
    def lambda_0990():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0990)

    WaitForThreadExit(0x0008, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010070789V#006F那个～初次见面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070790V我是游击士协会的准游击士\n',
            '艾丝蒂尔·布莱特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070791V其实我们有事想找博士您……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#102F#6P………………………………\n',
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070793V#002F……谈谈……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#103F#5S#6P完成啦啊啊啊啊啊！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0101,
        (
            '#0010070795V#004F呜哇！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#101F#6P哇哈哈，太好了！\n',
            '总算完成啦啊啊啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070797V真不愧是我呀！我实在是太厉害了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070798V嗯，好的！\n',
            '得快点拿它来测试。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0B7E')
    def lambda_0B7E():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0B7E')

    DispatchAsync2(0x0102, 0x0001, lambda_0B7E)

    @scena.Lambda('lambda_0B8F')
    def lambda_0B8F():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0B8F')

    DispatchAsync2(0x0107, 0x0001, lambda_0B8F)

    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetDirection(0x0008, 90, 0)
    ChrJumpTo(0x0008, 28840, 0, 31950, 500, 6000)

    @scena.Lambda('lambda_0BC8')
    def lambda_0BC8():
        CameraMove(29900, 0, 34680, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0BC8)

    @scena.Lambda('lambda_0BE0')
    def lambda_0BE0():
        ChrWalkTo(0x00FE, 29830, 0, 37050, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0BE0)

    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010070799V#504F#10A喂呀啊啊啊！？',
            0x5,
            TxtCtl.Enter,
        ),
    )

    CreateThread(0x0101, 0x01, 0x00, func_06_E4D)
    WaitForThreadExit(0x0008, 0x0001)
    ChrClearFlags(0x0008, 0x0040)
    ChrClearFlags(0x0008, 0x0004)
    ChrWalkTo(0x0008, 25500, -2000, 37300, 8000, 0x00)

    @scena.Lambda('lambda_0C53')
    def lambda_0C53():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_0C53)

    ChrWalkTo(0x0008, 25520, -2400, 34680, 8000, 0x00)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0107, 0xFF)
    ChrSetPos(0x0008, 30000, -1000, 8900, 270)

    @scena.Lambda('lambda_0C92')
    def lambda_0C92():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 0)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0C92)

    Sleep(1500)

    OP_63(0x0101)
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0101, 270, 800)
    ChrSetDirection(0x0101, 0, 800)

    ChrTalk(
        0x0101,
        (
            '#0010070800V#005F怎、怎么回事啊～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070801V#063F对、对不起，艾丝蒂尔姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070802V爷爷他，只要一进入研究状态，\n',
            '就会旁若无人的呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070803V几天前开始制造的装置终于完成了，\n',
            '所以爷爷他刚才这么兴奋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070804V#014F原来如此……\n',
            '真不愧是忘我的天才啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070805V#007F哎呀哎呀，\n',
            '我觉得这不是问题所在吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#067F真是不好意思呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00A2, 0, 0x510))
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0xE4D
@scena.Code('func_06_E4D')
def func_06_E4D():
    ChrSetFlags(0x00FE, 0x0020)
    ChrSetFlags(0x00FE, 0x1000)
    PlaySE(18, 0x00, 0x64)
    ChrMoveTo(0x00FE, 30240, 0, 33920, 8000, 0x00)
    ChrSetDirection(0x00FE, 0, 1000)
    ChrSetDirection(0x00FE, 90, 1000)
    ChrSetDirection(0x00FE, 180, 1000)
    ChrSetDirection(0x00FE, 270, 1000)
    ChrSetDirection(0x00FE, 0, 1000)
    ChrSetDirection(0x00FE, 90, 1000)
    ChrSetDirection(0x00FE, 180, 1000)
    ChrSetDirection(0x00FE, 270, 1000)
    ChrSetDirection(0x00FE, 0, 1000)
    ChrSetDirection(0x00FE, 90, 1000)
    ChrSetDirection(0x00FE, 180, 1000)
    ChrSetDirection(0x00FE, 270, 1000)
    ChrSetDirection(0x00FE, 0, 1000)
    ChrSetDirection(0x00FE, 90, 1000)
    ChrSetDirection(0x00FE, 180, 1000)
    ChrSetDirection(0x00FE, 270, 1000)
    ChrSetDirection(0x00FE, 0, 1000)
    ChrSetDirection(0x00FE, 90, 1000)
    ChrSetDirection(0x00FE, 180, 1000)
    ChrClearFlags(0x00FE, 0x0020)
    ChrClearFlags(0x00FE, 0x1000)
    OP_62(0x00FE, 0x00000000, 1900, 0x30, 0x32, 0x00000096, 0x00)
    PlaySE(48, 0x00, 0x64)

    Return()

# id: 0x0007 offset: 0xF17
@scena.Code('func_07_F17')
def func_07_F17():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 0, 0x510)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2884',
    )

    EventBegin(0x00)
    MapSetFlags(0x00400000)
    Fade(1000)
    OP_4A(0x0008, 255)
    CameraMove(32000, -1000, 10100, 0)
    ChrSetPos(0x0107, 31500, -1000, 200, 0)
    ChrSetPos(0x0101, 30600, -1000, -800, 0)
    ChrSetPos(0x0102, 31800, -1000, -1000, 0)
    OP_0D()

    @scena.Lambda('lambda_0F7E')
    def lambda_0F7E():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0F7E')

    DispatchAsync2(0x0101, 0x0001, lambda_0F7E)

    @scena.Lambda('lambda_0F8F')
    def lambda_0F8F():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0F8F')

    DispatchAsync2(0x0102, 0x0001, lambda_0F8F)

    @scena.Lambda('lambda_0FA0')
    def lambda_0FA0():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0FA0')

    DispatchAsync2(0x0107, 0x0001, lambda_0FA0)

    @scena.Lambda('lambda_0FB1')
    def lambda_0FB1():
        ChrWalkTo(0x00FE, 31300, -1000, 7600, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_0FB1)

    Sleep(100)

    @scena.Lambda('lambda_0FD1')
    def lambda_0FD1():
        ChrWalkTo(0x00FE, 30600, -1000, 6200, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0FD1)

    Sleep(100)

    @scena.Lambda('lambda_0FF1')
    def lambda_0FF1():
        ChrWalkTo(0x00FE, 31800, -1000, 6300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0FF1)

    WaitForThreadExit(0x0102, 0x0002)

    ChrTalk(
        0x0107,
        (
            '#0070070807V#560F#2P爷爷，我说啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070808V那个那个，\n',
            '这位姐姐有事要找您呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070809V#103F#1P嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0107, 400)

    ChrTalk(
        0x0008,
        (
            '#0540070810V#101F#1P哦哦，提妲！\n',
            '正好！你回来得正好！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070811V我正要做测试，\n',
            '你马上帮我收集一下资料吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070812V#065F#2P咦？但是，那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070813V#102F#1P这次的发明是\n',
            '让生命感应器无效化的导力器！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070814V它能产生特殊的导力场，\n',
            '使扫描不能正常地进行运行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070815V#064F#2P真、真的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070816V#101F#1P当然是真的。\n',
            '这可是货真价实的新发明啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070817V来来，\n',
            '快来帮我启动测试吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070818V#061F#2P嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_125F')
    def lambda_125F():
        CameraMove(32910, -1000, 8880, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_125F)

    @scena.Lambda('lambda_1277')
    def lambda_1277():
        ChrWalkTo(0x00FE, 32509, -1000, 10550, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1277)

    Sleep(300)

    @scena.Lambda('lambda_1297')
    def lambda_1297():
        ChrWalkTo(0x00FE, 34450, -1000, 8450, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_1297)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetDirection(0x0008, 0, 400)
    WaitForThreadExit(0x0107, 0x0001)
    ChrSetDirection(0x0107, 90, 400)
    WaitForThreadExit(0x0008, 0x0002)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '拉赛尔博士和提妲\n',
            '开始操作一部看似相当复杂的装置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010070819V#509F……喂喂，我说你们两位～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070820V#019F哈哈。\n',
            '看来得等上一段时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0008, 0x0102, 400)

    ChrTalk(
        0x0008,
        (
            '#0540070821V#102F喂，那边那个黑头发的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070822V#014F哎，是在叫我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070823V#102F除了你还有谁？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070824V快到二楼的书架那里，\n',
            '把那本『关于导力场的斥力值』\n',
            '的笔记给我拿来！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070825V听懂了没有！还不快去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070826V#012F好、好的，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_14EA')
    def lambda_14EA():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_14EA')

    DispatchAsync2(0x0101, 0x0001, lambda_14EA)

    ChrSetDirection(0x0102, 180, 600)
    CreateThread(0x0102, 0x01, 0x00, func_08_2885)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010070827V#004F等、等一下约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0541270002V#102F对了，\n',
            '还有那个头发像触角的。',
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
            '#509F#4P触、触角……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 800)

    ChrTalk(
        0x0101,
        (
            '#005F#4P你、你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070831V#102F别站在那里发呆，\n',
            '快点去给我泡杯咖啡！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#009F#4P为、为什么要我去！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070833V#101F顺带一提，我喜欢黑咖啡。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070834V要泡得像泥一样浓哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#509F#4P根本不听人家说话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070836V#007F唉，真是的，知道了啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 800)
    ChrWalkTo(0x0101, 31100, -1000, 1000, 6000, 0x00)

    @scena.Lambda('lambda_16E3')
    def lambda_16E3():
        ChrWalkTo(0x00FE, 20900, 0, 800, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_16E3)

    CameraMove(34600, -1000, 10700, 2000)

    ChrTalk(
        0x0107,
        (
            '#0070070837V#061F#2P……嗯，很顺利呢⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 0, 400)
    ChrSetDirection(0x0107, 270, 400)

    ChrTalk(
        0x0107,
        (
            '#0070070838V#560F#2P爷爷你看，\n',
            '我这里的设定完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070839V#101F#1P哦哦，很快嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070070840V#064F#2P对了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 180, 400)
    Sleep(200)

    ChrSetDirection(0x0107, 270, 400)
    OP_62(0x0107, 0x00000000, 1700, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070070841V#065F#2P哎呀……\n',
            '艾丝蒂尔姐姐他们呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070842V#103F#1P谁呀？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070843V……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070844V对了，说起来……\n',
            '刚才有两个以前没见过的年轻助手。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070845V咦……\n',
            '不是玛多克那家伙派来的新人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#561F#2P爷、爷爷啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(500)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '就这样，\n',
            '艾丝蒂尔和约修亚帮博士做起了实验……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '在两人的协助下实验顺利地进行，\n',
            '当实验结束的时候，已经是傍晚的时分了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    ChrSetFlags(0x0000, 0x0004)
    ChrSetFlags(0x0001, 0x0004)
    ChrSetFlags(0x0002, 0x0004)
    CameraMove(-300, 0, 2200, 0)
    ChrSetPos(0x0101, -2000, 0, 2000, 90)
    ChrSetPos(0x0102, -2000, 0, 500, 90)
    ChrSetPos(0x0107, 200, 0, 2000, 270)
    ChrSetPos(0x0008, 200, 0, 500, 270)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 0, 400)
    ChrClearFlags(0x0102, 0x0080)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0102, 4)
    ChrSetChipByIndex(0x0107, 5)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x0107, 0x0004)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#101F哇哈哈，抱歉抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070850V完全把你们俩\n',
            '当成是中央工房的新人了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070851V结果就和平常吩咐工房的员工那样，\n',
            '把你们使来唤去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#009F真是的，亏您还笑得出来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070853V不止是泡咖啡，\n',
            '还要我们帮这帮那的～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070854V#019F哈哈，我觉得挺好啊。\n',
            '当作是宝贵的工作经验不就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070855V而且新型导力器的启动实验\n',
            '也不是随便就能遇到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#103F哦，这个小伙子。\n',
            '十分之明白事理嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不如别再当什么游击士了，\n',
            '投身导力技术的研究事业吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#561F爷爷！真是的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#560F对不起，\n',
            '艾丝蒂尔姐姐、约修亚哥哥。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070860V刚才受到爷爷的影响，\n',
            '结果连我也沉迷进实验里去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070861V#008F哎哟～不要紧。\n',
            '提妲没有必要道歉啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070862V#007F我还在想『导力革命之父』\n',
            '会是个怎样厉害的人呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070863V今天终于见识到了，\n',
            '原来是个得意忘形的老爷爷……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#101F哇哈哈，过奖过奖。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#102F不过话说回来，\n',
            '真没想到卡西乌斯的孩子会来拜访我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070866V我也吓了一跳呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070867V#501F啊～\n',
            '博士果然认识老爸吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#104F嗯，很久以前就认识了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070869V从他还在军队当兵开始，\n',
            '我和卡西乌斯已经有２０年的交情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#064F嘿嘿……\n',
            '我也见过卡西乌斯叔叔哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070890004V蓄着胡子，是位很有型的叔叔呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070872V#007F唔～\n',
            '说不清是有型还是古怪啦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070873V#006F不过，既然这样的话，\n',
            '我们就放心把那东西交给你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070874V#010F是啊，我想没问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070875V#064F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#103F什么，是什么东西？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070877V说起来，\n',
            '你们不是说有事找我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070878V#002F嗯，其实是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们向博士详细地说明了有关的事情，\n',
            '并且拿出了黑色导力器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    Fade(500)
    ChrSetPos(0x000A, -560, 800, 270, 0)
    ChrClearFlags(0x000A, 0x0080)
    OP_0D()
    Sleep(500)

    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#103F……哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070880V#064F哇～\n',
            '漆黑的导力器……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#102F嗯，这东西很有意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0541270003V不仅没有生产序号，\n',
            '连个接缝都找不到。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070883V而且这个外壳……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '拉赛尔博士\n',
            '从腰上的皮带处拿出了工作用的小刀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '他用小刀大力地\n',
            '往黑色导力器的表面划了下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010070884V#004F什、什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070885V#012F特殊合金制的小刀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#102F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070887V#104F……果然如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070888V#100F来，你们看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#506F嗯、嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们\n',
            '仔细地往黑色导力器的表面看去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010070890V#004F咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#065F一点伤痕都没有……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070892V#012F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#104F看来这个外壳是用\n',
            '一种非常特殊的素材制作出来的。\n',
            '而这种素材比我所知的任何金属都要硬。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070894V要想切开它来调查内部，\n',
            '看来是相当困难了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#002F原、原来是\n',
            '这么不得了的东西啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070896V#013F连切开都不行的话，\n',
            '看来的确是相当麻烦了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#102F唔……\n',
            '花点时间还是能把外壳切开的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070898V不过在此之前，\n',
            '还是先用测定装置检查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070899V#004F测定装置？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#560F就是刚才做实验也用过的\n',
            '那个大型装置。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070901V是个能对导力波的动向\n',
            '进行实时测定的装置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#006F不、不是很明白……\n',
            '用了那个装置会怎么样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#102F简单来说，\n',
            '我们就能知道这东西是怎么工作的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070904V当然，只凭导力波动向的判断，\n',
            '还只能停留在推测的范围里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0102F即使如此，\n',
            '能得到重要线索的可能性还是很高吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#104F嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么事不宜迟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070908V#060F可是可是，爷爷。\n',
            '差不多是吃饭的时间了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#103F哎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070910V#067F艾丝蒂尔姐姐，\n',
            '你们不嫌弃的话，也一起吃吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070911V虽然我对自己的手艺没什么自信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070912V#001F啊，那我们就不客气啦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F可以的话我也来帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#101F好，那就这样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070915V晚饭准备好之前，\n',
            '我就先稍微对这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070916V#062F不、不行。\n',
            '我也想看嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070917V爷爷可不要耍赖先看哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#104F小气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#509F（怎么说呢，这两爷孙……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#019F（血缘果然是奇妙东西啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T3133._SN', 100, 0, 0)
    IdleLoop()

    def _loc_2884(): pass

    label('loc_2884')

    Return()

# id: 0x0008 offset: 0x2885
@scena.Code('func_08_2885')
def func_08_2885():
    ChrWalkTo(0x00FE, 30800, -1000, 460, 5000, 0x00)
    ChrWalkTo(0x00FE, 23440, 0, 190, 5000, 0x00)
    TerminateThread(0x0101, 0xFF)
    ChrWalkTo(0x00FE, 23100, 2000, 8950, 5000, 0x00)

    @scena.Lambda('lambda_28CB')
    def lambda_28CB():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_28CB)

    ChrWalkTo(0x00FE, 26010, 4000, 9120, 5000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x0009 offset: 0x28F1
@scena.Code('func_09_28F1')
def func_09_28F1():
    OP_A6(0x0001)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x000A offset: 0x2903
@scena.Code('func_0A_2903')
def func_0A_2903():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(32860, -1000, 8930, 0)
    ChrSetPos(0x0107, 32509, -1000, 10550, 180)
    ChrSetPos(0x0008, 34450, -1000, 8450, 270)
    ChrSetPos(0x0101, 31580, -1000, 8390, 45)
    ChrSetPos(0x0102, 32080, -1000, 7470, 45)
    OP_4A(0x0008, 255)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0540070921V#104F咳……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070922V肚子填饱了，\n',
            '这就准备开始吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070923V#102F那么，艾丝蒂尔。\n',
            '把那个导力器放到台上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070924V#002F嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2A16')
    def lambda_2A16():
        CameraMove(33550, -1000, 9600, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2A16)

    ChrSetFlags(0x0101, 0x0004)

    @scena.Lambda('lambda_2A33')
    def lambda_2A33():
        ChrWalkTo(0x00FE, 33050, -1000, 10140, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2A33)

    Sleep(300)

    @scena.Lambda('lambda_2A53')
    def lambda_2A53():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_2A53')

    DispatchAsync2(0x0107, 0x0002, lambda_2A53)

    @scena.Lambda('lambda_2A64')
    def lambda_2A64():
        ChrTurnDirection(0x00FE, 0x0101, 400)
        Yield()

        Jump('lambda_2A64')

    DispatchAsync2(0x0008, 0x0002, lambda_2A64)

    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0101, 90, 400)
    WaitForThreadExit(0x0101, 0x0002)
    Fade(500)
    PlaySE(130, 0x00, 0x64)
    ChrSetPos(0x000A, 34310, -270, 10390, 0)
    ChrClearFlags(0x000A, 0x0080)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010070925V#501F这样可以了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070926V#102F嗯，麻烦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 225, 400)
    TerminateThread(0x0107, 0xFF)
    TerminateThread(0x0008, 0xFF)

    @scena.Lambda('lambda_2B05')
    def lambda_2B05():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_2B05)

    @scena.Lambda('lambda_2B13')
    def lambda_2B13():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2B13)

    ChrWalkTo(0x0101, 31580, -1000, 8390, 3000, 0x00)
    ChrSetDirection(0x0101, 45, 400)
    ChrClearFlags(0x0101, 0x0004)

    ChrTalk(
        0x0008,
        (
            '#0540070927V#100F提妲呀，\n',
            '你那边准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070928V#061F嗯，很顺利哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070929V#104F很好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070930V#102F那么接下来……\n',
            '『黑色导力器』导力波测定实验现在开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070931V#014F『黑色导力器』？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070932V#000F这、这还真是\n',
            '最现成不过的命名啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070933V#100F简单的也就是最好的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070934V虽然搞实验重在过程，\n',
            '不过没有名字也很不方便嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070935V#560F好、好兴奋呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070936V#506F啊，提妲这孩子\n',
            '也是充满期待斗志满满啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070937V#067F啊……嘿嘿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070938V#102F好，那么开始啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070939V提妲。\n',
            '启动装置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070940V#062F嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2DAD')
    def lambda_2DAD():
        CameraMove(34330, -1000, 10370, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2DAD)

    OP_20(0x000003E8)
    ChrSetDirection(0x0107, 0, 400)
    ChrSetDirection(0x0008, 90, 400)
    OP_21()
    PlaySE(157, 0x00, 0x64)
    PlayBGM(87)
    LoadEffect(0x03, 'map\\\\mp029_00.eff')
    LoadEffect(0x04, 'map\\\\mp029_01.eff')
    LoadEffect(0x05, 'map\\\\mp029_02.eff')
    PlayEffect(0x03, 0x03, 0x00FF, 33570, -400, 9620, 0, 0, 0, 300, 300, 300, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x04, 0x04, 0x00FF, 31600, -500, 11150, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0540070941V#102F输出固定在４５％……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070942V各种测定器开始待命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070943V#062F明白……\n',
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(158, 0x01, 0x64)
    Sleep(200)

    PlayEffect(0x04, 0x05, 0x00FF, 35680, 750, 10480, 0, 0, 0, 400, 400, 400, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x04, 0x06, 0x00FF, 35820, 750, 9630, 0, 0, 0, 400, 400, 400, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x04, 0x07, 0x00FF, 35390, 930, 7320, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x04, 0x02, 0x00FF, 35360, 930, 6080, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)

    ChrTalk(
        0x0107,
        (
            '#0070070944V#560F嗯。\n',
            '各种测定器，准备完成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070945V#102F那么，接下来正式开始。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070946V在找不到输入输出接口的情况下，\n',
            '只能探测其中结晶回路所产生的导力波，\n',
            '对其发生的反应进行搜索……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070947V#101F这里就是这个测定装置\n',
            '发挥真正本领的地方！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070948V#506F真、真是热血沸腾啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070949V#102F按下按钮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(156, 0x00, 0x64)
    ChrSetDirection(0x0008, 0, 300)
    PlaySE(201, 0x00, 0x64)
    LoadEffect(0x00, 'map\\\\mp025_00.eff')
    PlayEffect(0x00, 0x00, 0x000A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010070950V#501F哎……\n',
            '好耀眼的光芒啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070951V#010F原来如此，\n',
            '这样就能给结晶回路加上负荷……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070952V#101F不错不错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 270, 300)

    ChrTalk(
        0x0008,
        (
            '#0540070953V#100F提妲呀，\n',
            '测定器有什么反应吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070954V#063F嗯、嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070955V好像有点奇怪……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070956V#103F怎么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070957V#063F转速计的指针\n',
            '在哆哆嗦嗦地抖个不停……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070958V#065F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070959V开、开始骨碌骨碌地来回转了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070960V#102F什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)
    OP_21()
    PlayBGM(92)
    OP_77(0x82, 0xFF, 0xFF, 0x00, 0x00001388)

    @scena.Lambda('lambda_338C')
    def lambda_338C():
        CameraMove(34810, -500, 10930, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_338C)

    @scena.Lambda('lambda_33A4')
    def lambda_33A4():
        CameraSetDistance(3160, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_33A4)

    @scena.Lambda('lambda_33B4')
    def lambda_33B4():
        OP_67(0, 3400, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_33B4)

    Sleep(1000)

    OP_23(0x009E)
    OP_23(0x00C9)
    PlaySE(144, 0x00, 0x64)
    LoadEffect(0x00, 'map\\\\mp007_00.eff')
    PlayEffect(0x00, 0x01, 0x000A, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetDirection(0x0008, 0, 400)
    ChrSetDirection(0x0107, 90, 400)
    WaitForThreadExit(0x0101, 0x0003)
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_345C')
    def lambda_345C():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_345C)

    Sleep(100)

    @scena.Lambda('lambda_3477')
    def lambda_3477():
        OP_94(0x01, 0x00FE, 0x00B4, 0x000001F4, 0x000007D0, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_3477)

    WaitForThreadExit(0x0107, 0x0001)

    ChrTalk(
        0x0107,
        (
            '#0070070961V#068F哎呀！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070962V#102F这、这是怎么回事！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070963V#005F#3P约修亚，这是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070964V#016F#4P那时候的黑色光芒……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(145, 0x00, 0x64)
    LoadEffect(0x02, 'map\\\\mp015_00.eff')
    PlayEffect(0x02, 0xFF, 0x000A, 0, 300, 0, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x02, 0xFF, 0x000A, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(50)

    StopEffect(0x03, 0x00)
    Sleep(50)

    StopEffect(0x05, 0x00)
    Sleep(50)

    StopEffect(0x06, 0x00)
    Sleep(50)

    StopEffect(0x04, 0x00)
    Sleep(50)

    StopEffect(0x07, 0x00)
    Sleep(50)

    StopEffect(0x02, 0x00)
    OP_62(0x0008, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetDirection(0x0008, 270, 400)

    ChrTalk(
        0x0008,
        (
            '#0540070965V#103F什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T3106._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000B offset: 0x363B
@scena.Code('func_0B_363B')
def func_0B_363B():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(34700, -1000, 10700, 0)
    OP_77(0x82, 0xFF, 0xFF, 0x00, 0x00000000)
    LoadEffect(0x00, 'map\\\\mp025_00.eff')
    PlayEffect(0x00, 0x00, 0x000A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(144, 0x00, 0x64)
    LoadEffect(0x01, 'map\\\\mp007_00.eff')
    PlayEffect(0x01, 0x01, 0x000A, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_4A(0x0008, 255)
    ChrSetPos(0x0008, 34400, -1000, 8900, 0)
    ChrSetPos(0x0107, 32759, -1000, 8640, 90)
    ChrSetPos(0x0101, 26210, 0, -230, 78)
    ChrSetPos(0x0102, 26210, 0, -230, 78)
    ChrSetPos(0x000A, 34310, -270, 10390, 0)
    ChrClearFlags(0x000A, 0x0080)
    CameraMove(34810, -500, 10930, 0)
    CameraSetDistance(3160, 0)
    OP_67(0, 3400, -10000, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0107,
        (
            '#0070070966V#068F爷、爷爷，\n',
            '不能再继续了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070967V必须停止测定装置！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070968V#102F不，还不能停！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070969V还差一点就能得出数据了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x0101, 30300, -1000, 900, 6000, 0x00)
    ChrWalkTo(0x0101, 33400, -1000, 6400, 6000, 0x00)
    ChrSetDirection(0x0101, 0, 800)

    ChrTalk(
        0x0101,
        (
            '#0010070970V#005F等、等一下！\n',
            '城镇里的照明灯都熄灭了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 800)

    ChrTalk(
        0x0107,
        (
            '#0070070971V#065F哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 800)

    ChrTalk(
        0x0008,
        (
            '#0540070972V#103F居然……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070973V#102F唔，没办法了！\n',
            '测定实验到此结束！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, 34480, -1000, 8390, 2000, 0x00)
    ChrSetDirection(0x0008, 90, 400)
    Sleep(500)

    PlaySE(225, 0x00, 0x64)
    Sleep(500)

    OP_20(0x00000BB8)
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00001388)

    @scena.Lambda('lambda_395C')
    def lambda_395C():
        CameraMove(34330, -1000, 10370, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_395C)

    @scena.Lambda('lambda_3974')
    def lambda_3974():
        CameraSetDistance(2750, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_3974)

    @scena.Lambda('lambda_3984')
    def lambda_3984():
        OP_67(0, 6150, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3984)

    StopEffect(0x00, 0x02)
    StopEffect(0x01, 0x02)
    OP_23(0x0090)
    LoadEffect(0x03, 'map\\\\mp029_00.eff')
    LoadEffect(0x04, 'map\\\\mp029_01.eff')
    LoadEffect(0x05, 'map\\\\mp029_02.eff')
    Sleep(300)

    Sleep(300)

    PlayEffect(0x04, 0xFF, 0x00FF, 31600, -500, 11150, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlayEffect(0x04, 0xFF, 0x00FF, 35680, 750, 10480, 0, 0, 0, 400, 400, 400, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlayEffect(0x04, 0xFF, 0x00FF, 35820, 750, 9630, 0, 0, 0, 400, 400, 400, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlayEffect(0x04, 0xFF, 0x00FF, 35390, 930, 7320, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(300)

    PlayEffect(0x04, 0xFF, 0x00FF, 35360, 930, 6080, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    ChrSetDirection(0x0008, 0, 400)
    ChrSetDirection(0x0107, 45, 400)
    WaitForThreadExit(0x0101, 0x0003)
    OP_21()
    PlayBGM(84)

    ChrTalk(
        0x0101,
        (
            '#0010070974V#004F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070975V恢、恢复原样了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070976V#561F#3P呼啊啊啊～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 90, 400)

    ChrTalk(
        0x0008,
        (
            '#0540070977V#102F记录器呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070978V不行，什么都没记录下来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070979V这么看来，能保持正常运作的\n',
            '只剩下这个『黑色导力器』本体了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070980V其他都被扫荡一空……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070981V#2P太好了，\n',
            '看来实验中止了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3C73')
    def lambda_3C73():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_3C73')

    DispatchAsync2(0x0101, 0x0001, lambda_3C73)

    @scena.Lambda('lambda_3C84')
    def lambda_3C84():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_3C84')

    DispatchAsync2(0x0107, 0x0001, lambda_3C84)

    @scena.Lambda('lambda_3C95')
    def lambda_3C95():
        ChrTurnDirection(0x00FE, 0x0102, 400)
        Yield()

        Jump('lambda_3C95')

    DispatchAsync2(0x0008, 0x0001, lambda_3C95)

    @scena.Lambda('lambda_3CA6')
    def lambda_3CA6():
        CameraMove(32900, -1000, 8060, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3CA6)

    ChrWalkTo(0x0102, 30300, -1000, 900, 4000, 0x00)
    ChrWalkTo(0x0102, 31500, -1000, 6100, 4000, 0x00)
    ChrSetDirection(0x0102, 45, 400)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0107, 0xFF)
    TerminateThread(0x0008, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010070982V#002F啊，约修亚！\n',
            '外面的情况怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070983V#010F还好没什么大碍……\n',
            '照明设备好像都恢复正常了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070984V不过大家的骚动还没平息下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070985V#007F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070986V#505F真奇怪……\n',
            '刚才到底是怎么一回事啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070987V#104F是呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070988V#102F要解释的话，\n',
            '应该是『导力停止现象』吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3E4D')
    def lambda_3E4D():
        ChrTurnDirection(0x0102, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3E4D)

    @scena.Lambda('lambda_3E5B')
    def lambda_3E5B():
        ChrTurnDirection(0x0107, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_3E5B)

    ChrTurnDirection(0x0101, 0x0008, 400)

    ChrTalk(
        0x0101,
        (
            '#0010070989V#004F『导力停止现象』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070990V#012F就是说导力器内部运作的导力\n',
            '停止工作了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070991V#063F果然是由那个『黑色导力器』\n',
            '造成的吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070992V#104F嗯，不会错的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070993V#102F但是，竟然能使\n',
            '如此大范围的导力器都停止工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070994V嗯嗯嗯嗯……\n',
            '真是出乎意料的东西呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070995V#101F有趣，实在是太有趣了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070996V#509F我、我认为现在\n',
            '不是觉得有趣的时候哦～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 26210, 0, -230, 78)

    NpcTalk(
        0x0009,
        '男性的声音',
        (
            '#0550070997V#2P博～士～啊～！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0107, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    PlaySE(6, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_40B2')
    def lambda_40B2():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_40B2')

    DispatchAsync2(0x0101, 0x0001, lambda_40B2)

    @scena.Lambda('lambda_40C3')
    def lambda_40C3():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_40C3')

    DispatchAsync2(0x0107, 0x0001, lambda_40C3)

    @scena.Lambda('lambda_40D4')
    def lambda_40D4():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_40D4')

    DispatchAsync2(0x0102, 0x0001, lambda_40D4)

    @scena.Lambda('lambda_40E5')
    def lambda_40E5():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_40E5')

    DispatchAsync2(0x0008, 0x0001, lambda_40E5)

    ChrWalkTo(0x0009, 30300, -1000, 900, 6000, 0x00)
    ChrWalkTo(0x0009, 32360, -1000, 6400, 6000, 0x00)
    ChrWalkTo(0x0009, 33150, -1000, 7460, 6000, 0x00)
    ChrTurnDirection(0x0009, 0x0008, 0)

    ChrTalk(
        0x0008,
        (
            '#0540070998V#103F哦，玛多克。\n',
            '你来得真巧呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0550070999V#804F#6P一点也不巧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550071000V已经不止一次两次了！\n',
            '每次一有新发明就要引起骚动！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550071001V刚刚城镇里的照明都中断了，\n',
            '一定又是你做的好事吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071002V#104F真是失礼。\n',
            '这次骚动可和我没关系哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071003V是放在那边的\n',
            '『黑色导力器』干的好事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0550071004V#802F#6P这、这就是那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550071005V#803F原来如此，原因在此的话，\n',
            '这异常事态倒是可以勉强接受……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0009)

    ChrTalk(
        0x0009,
        (
            '#0550071006V#804F#6P#3S不、不对啊！\n',
            '再怎么说，这事和你还是脱不了关系！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071007V#102F嘁，又被识破了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0107, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010071008V#006F感觉他们两人\n',
            '真是莫名地合拍呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071009V#010F他们平时一直这样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070071010V#067F啊……真是不好意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x00000BB8)
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '就这样，艾丝蒂尔他们\n',
            '慌忙地度过了来到蔡斯市的第一天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '由于实验完成之后已经是深夜了，\n',
            '艾丝蒂尔和约修亚就在拉赛尔工房借宿了一夜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(13, 0x00, 0x64)
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    Sleep(5000)

    SetScenaFlags(ScenaFlag(0x00A2, 1, 0x511))
    OP_28(0x003F, 0x01, 0x0010)
    OP_28(0x003F, 0x01, 0x0020)
    MapClearFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T3100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x455A
@scena.Code('func_0C_455A')
def func_0C_455A():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-2900, 0, 34200, 0)
    ChrSetPos(0x0102, -4100, 0, 33700, 180)
    ChrSetPos(0x0101, -5000, 0, 31300, 0)
    ChrSetPos(0x0107, -5900, -2000, 39200, 0)
    ChrSetFlags(0x0107, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#000F哎呀～\n',
            '昨天一天真是够呛啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071014V这个城镇本身就够惊人的，\n',
            '竟然还发生那样的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F哈哈，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '话说回来，\n',
            '那个『黑色导力器』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071017V的确出乎意料，\n',
            '看来是非同一般的东西啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071019V实验也失败了，\n',
            '博士打算怎么办呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F早上好。\n',
            '艾丝蒂尔姐姐、约修亚哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0107, 400)
    ChrClearFlags(0x0107, 0x0080)

    @scena.Lambda('lambda_46FA')
    def lambda_46FA():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_46FA')

    DispatchAsync2(0x0101, 0x0001, lambda_46FA)

    @scena.Lambda('lambda_470B')
    def lambda_470B():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_470B')

    DispatchAsync2(0x0102, 0x0001, lambda_470B)

    ChrWalkTo(0x0107, -1800, 0, 39000, 3000, 0x00)
    ChrWalkTo(0x0107, -1800, 0, 36400, 2000, 0x00)
    ChrTurnDirection(0x0107, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#000F啊，早啊～\n',
            '提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F早上好，\n',
            '昨天真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070890005V#060F嘿嘿，是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '艾丝蒂尔姐姐\n',
            '你们昨晚睡得还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，睡得超饱哦㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '说到这个，\n',
            '博士也已经起床了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070071027V#060F啊～爷爷他啊，\n',
            '一大早就赶去中央工房了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '他还对我说\n',
            '『一定要找出黑色导力器的秘密』呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎呀哎呀～\n',
            '昨晚被工房长先生那样训斥，\n',
            '还是不吸取教训啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F很感谢他能帮忙调查那个导力器，\n',
            '但是要这么麻烦他，\n',
            '我们还真是有点过意不去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F啊哈哈，请别介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071032V爷爷他呢，\n',
            '是自己想调查才会去调查的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '啊～对了，\n',
            '吃完早饭我也要去中央工房。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071034V艾丝蒂尔姐姐，你们准备怎么办呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F当然是跟你一起去啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F是啊。\n',
            '我们也希望能帮上点忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F哇，太好了～\n',
            '那我们这就出门吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070890006V#060F啊，不好！\n',
            '汤还在火上呢～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '早饭马上就要做好了，\n',
            '请姐姐你们再稍等一下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0107, -1800, 0, 39000, 6000, 0x00)
    ChrWalkTo(0x0107, -5900, -2000, 39200, 6000, 0x00)
    ChrSetFlags(0x0107, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#000F那孩子真可爱……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071042V好想把她带回家呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '艾丝蒂尔，别像个大叔一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T3100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x4B2E
@scena.Code('func_0D_4B2E')
def func_0D_4B2E():
    EventBegin(0x00)
    CameraMove(-1780, 0, -950, 0)
    ChrSetPos(0x0107, -2009, 0, -2300, 0)
    ChrSetPos(0x0101, -1530, 0, -3110, 0)
    ChrSetPos(0x0102, -3180, 0, -3090, 0)
    ChrSetPos(0x0106, -2410, 0, -3780, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#000F好了……\n',
            '开始找那个装置吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090427V会放在哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4BCE')
    def lambda_4BCE():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_4BCE)

    @scena.Lambda('lambda_4BDC')
    def lambda_4BDC():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4BDC)

    @scena.Lambda('lambda_4BEA')
    def lambda_4BEA():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4BEA)

    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070890007V#060F我想也许是在研究室的角落\n',
            '或者是二楼的书房里吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070890008V因为爷爷总是把刚发明的东西\n',
            '随意地丢在一边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F听起来是个很奇怪的老爷子嘛。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090431V不管了。\n',
            '总之快点找那东西出来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0043, 0x01, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x000E offset: 0x4CDA
@scena.Code('func_0E_4CDA')
def func_0E_4CDA():
    EventBegin(0x00)
    CameraMove(25700, -60, 31320, 1000)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '找到感应阻碍器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00AB, 7, 0x55F))
    OP_28(0x0043, 0x01, 0x0100)

    ChrTalk(
        0x0101,
        (
            '#000F找到啦找到啦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090433V#010F这机器的确就是\n',
            '那天我们帮忙实验的新型导力器。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090434V怎么样，能用吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F嗯……没问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090436V一切顺利的话，\n',
            '能完全瞒过生命感应器哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#050F好了，快点回协会吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090438V雾香应该也准备好\n',
            '有关雷斯顿要塞的资料了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_64(0x00, 0x0001)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
