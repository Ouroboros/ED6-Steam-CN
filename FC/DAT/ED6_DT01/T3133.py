import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3133_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3133   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3133.x'
    header.mapIndex       = 1
    header.bgm            = 13
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
        ('ED6_DT07/CH01250._CH', 'ED6_DT07/CH01250P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
        ('ED6_DT07/CH00063._CH', 'ED6_DT07/CH00063P._CP'),
        ('ED6_DT06/CH20130._CH', 'ED6_DT06/CH20130P._CP'),
    ]

# id: 0x10001 offset: 0xE2
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
            name                = '黑色导力器',
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

# id: 0x10002 offset: 0x162
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x162
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

# id: 0x10004 offset: 0x182
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 31850,
            triggerZ            = 0,
            triggerY            = 30290,
            triggerRange        = 800,
            actorX              = 31850,
            actorZ              = 500,
            actorY              = 30290,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1A6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_1B4',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_0B_2EAD)

    def _loc_1B4(): pass

    label('loc_1B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_1C2',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_0C_34E8)

    def _loc_1C2(): pass

    label('loc_1C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_1D0',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, func_0D_3E69)

    def _loc_1D0(): pass

    label('loc_1D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 5, 0x3FD)),
            Expr.Return,
        ),
        'loc_1E7',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    Event(0, func_08_1D52)
    OP_B1('t3133_y')

    def _loc_1E7(): pass

    label('loc_1E7')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_1F7'),
        (0x0000006A, 'loc_225'),
        (-1, 'loc_238'),
    )

    def _loc_1F7(): pass

    label('loc_1F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 7, 0x50F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_20A',
    )

    SetScenaFlags(ScenaFlag(0x00A1, 7, 0x50F))
    Event(0, func_04_5CA)

    def _loc_20A(): pass

    label('loc_20A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 6, 0x55E)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_222',
    )

    MapSetFlags(0x10000000)
    SetScenaFlags(ScenaFlag(0x00AB, 6, 0x55E))
    Event(0, func_0E_4627)

    def _loc_222(): pass

    label('loc_222')

    Jump('loc_238')

    def _loc_225(): pass

    label('loc_225')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 0, 0x510)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 7, 0x50F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_235',
    )

    Event(0, func_05_7C5)

    def _loc_235(): pass

    label('loc_235')

    Jump('loc_238')

    def _loc_238(): pass

    label('loc_238')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 7, 0x55F)),
            Expr.Return,
        ),
        'loc_242',
    )

    Jump('loc_27F')

    def _loc_242(): pass

    label('loc_242')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_262',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 31850, 0, 30290, 0)

    Jump('loc_27F')

    def _loc_262(): pass

    label('loc_262')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 0, 0x510)),
            Expr.Return,
        ),
        'loc_27F',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrSetPos(0x000B, 34470, -300, 10490, 0)

    def _loc_27F(): pass

    label('loc_27F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_289',
    )

    Jump('loc_2F9')

    def _loc_289(): pass

    label('loc_289')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 0, 0x510)),
            Expr.Return,
        ),
        'loc_2B0',
    )

    ChrClearFlags(0x0008, 0x0080)
    CreateThread(0x0008, 0x00, 0x00, func_02_339)
    ChrSetPos(0x0008, 30000, -1000, 8900, 270)

    Jump('loc_2F9')

    def _loc_2B0(): pass

    label('loc_2B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_2D0',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 28000, 0, 31400, 180)

    Jump('loc_2F9')

    def _loc_2D0(): pass

    label('loc_2D0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_2F9',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 29950, -1000, 8090, 269)
    CreateThread(0x0008, 0x00, 0x00, func_02_339)
    ChrSetFlags(0x0008, 0x0010)

    def _loc_2F9(): pass

    label('loc_2F9')

    Return()

# id: 0x0001 offset: 0x2FA
@scena.Code('func_01_2FA')
def func_01_2FA():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_312',
    )

    OP_B1('t3133_y')

    Jump('loc_31B')

    def _loc_312(): pass

    label('loc_312')

    OP_B1('t3133_n')

    def _loc_31B(): pass

    label('loc_31B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 7, 0x55F)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_32B',
    )

    OP_64(0x00, 0x0001)

    def _loc_32B(): pass

    label('loc_32B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_338',
    )

    StopEffect(0x80, 0x00)
    StopEffect(0x81, 0x00)

    def _loc_338(): pass

    label('loc_338')

    Return()

# id: 0x0002 offset: 0x339
@scena.Code('func_02_339')
def func_02_339():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_34E',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_339')

    def _loc_34E(): pass

    label('loc_34E')

    Return()

# id: 0x0003 offset: 0x34F
@scena.Code('func_03_34F')
def func_03_34F():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_5C6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_529',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_460',
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

    Jump('loc_526')

    def _loc_460(): pass

    label('loc_460')

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

    def _loc_526(): pass

    label('loc_526')

    Jump('loc_5C6')

    def _loc_529(): pass

    label('loc_529')

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

    def _loc_5C6(): pass

    label('loc_5C6')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x5CA
@scena.Code('func_04_5CA')
def func_04_5CA():
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
            '#0070070776V#067F#2P嘿嘿……\n',
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
            '#0070070779V#060F#2P嗯～爷爷他嘛，\n',
            '我想应该在工房里工作吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_072E')
    def lambda_072E():
        CameraMove(1070, 0, -1350, 1500)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_072E)

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

# id: 0x0005 offset: 0x7C5
@scena.Code('func_05_7C5')
def func_05_7C5():
    EventBegin(0x00)
    CameraMove(31150, 0, 36720, 0)
    ChrSetFlags(0x0107, 0x0080)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0107, 30900, 0, 36300, 225)
    ChrSetPos(0x0101, 29800, 0, 37500, 180)
    ChrSetPos(0x0102, 31000, 0, 37400, 225)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, 27800, 500, 31400, 180)
    ChrSetChipByIndex(0x0008, 6)

    @scena.Lambda('lambda_0840')
    def lambda_0840():
        OP_99(0x00FE, 0x01, 0x02, 1000)
        Yield()

        Jump('lambda_0840')

    DispatchAsync2(0x0008, 0x0001, lambda_0840)

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
            '#0540070783V#102F#6P……唔唔唔………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070784V这里这样，然后……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0906')
    def lambda_0906():
        OP_99(0x00FE, 0x01, 0x02, 1500)
        Yield()

        Jump('lambda_0906')

    DispatchAsync2(0x0008, 0x0001, lambda_0906)

    Sleep(200)

    ChrTalk(
        0x0008,
        (
            '#0540070785V#102F#6P………唔唔哦哦……！',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0008, 30, 0, 400, 5000)
    CloseMessageWindow()

    @scena.Lambda('lambda_095F')
    def lambda_095F():
        OP_99(0x00FE, 0x01, 0x02, 2000)
        Yield()

        Jump('lambda_095F')

    DispatchAsync2(0x0008, 0x0001, lambda_095F)

    Sleep(200)

    ChrTalk(
        0x0008,
        (
            '#0540070786V#102F#6P………喔喔喔喔……！',
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
    ChrSetFlags(0x0101, 0x0004)

    @scena.Lambda('lambda_0A03')
    def lambda_0A03():
        CameraMove(29760, 0, 33950, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0A03)

    @scena.Lambda('lambda_0A1B')
    def lambda_0A1B():
        ChrWalkTo(0x00FE, 29800, 0, 33900, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A1B)

    Sleep(800)

    @scena.Lambda('lambda_0A3B')
    def lambda_0A3B():
        ChrWalkTo(0x00FE, 31100, 0, 34000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0A3B)

    Sleep(200)

    @scena.Lambda('lambda_0A5B')
    def lambda_0A5B():
        ChrWalkTo(0x00FE, 30900, 0, 35100, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0A5B)

    WaitForThreadExit(0x0101, 0x0001)
    ChrClearFlags(0x0101, 0x0004)

    @scena.Lambda('lambda_0A80')
    def lambda_0A80():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A80)

    WaitForThreadExit(0x0107, 0x0001)

    @scena.Lambda('lambda_0A93')
    def lambda_0A93():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0A93)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_0AA6')
    def lambda_0AA6():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0AA6)

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

    @scena.Lambda('lambda_0B41')
    def lambda_0B41():
        OP_99(0x00FE, 0x00, 0x02, 3000)
        Yield()

        Jump('lambda_0B41')

    DispatchAsync2(0x0008, 0x0001, lambda_0B41)

    ChrTalk(
        0x0008,
        (
            '#0540070792V#102F#6P………………………………\n',
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
    OP_62(0x0008, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    TerminateThread(0x0008, 0xFF)
    ChrSetSubChip(0x0008, 0)
    OP_9E(0x0008, 50, 0, 1000, 6000)
    OP_63(0x0008)
    ChrSetSubChip(0x0008, 3)

    ChrTalk(
        0x0008,
        (
            '#0540070794V#103F#5S#6P完、完成啦啊啊啊啊啊！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 300, 3000, 100)
    ChrJumpToRelative(0x0008, 0, 0, 0, 300, 4000)
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
    OP_9E(0x0008, 30, 0, 500, 6000)

    ChrTalk(
        0x0008,
        (
            '#0540070796V#101F#6P哇哈哈，太好了！\n',
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

    @scena.Lambda('lambda_0D2F')
    def lambda_0D2F():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0D2F')

    DispatchAsync2(0x0102, 0x0001, lambda_0D2F)

    @scena.Lambda('lambda_0D40')
    def lambda_0D40():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0D40')

    DispatchAsync2(0x0107, 0x0001, lambda_0D40)

    ChrSetFlags(0x0008, 0x0040)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetDirection(0x0008, 90, 0)
    ChrJumpTo(0x0008, 28840, 0, 31950, 500, 6000)

    @scena.Lambda('lambda_0D7E')
    def lambda_0D7E():
        CameraMove(29900, 0, 34680, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0D7E)

    @scena.Lambda('lambda_0D96')
    def lambda_0D96():
        ChrWalkTo(0x00FE, 29830, 0, 37050, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0D96)

    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010070799V#504F#10A喂呀啊啊啊！？',
            0x5,
            TxtCtl.Enter,
        ),
    )

    CreateThread(0x0101, 0x01, 0x00, func_06_100F)
    WaitForThreadExit(0x0008, 0x0001)
    ChrClearFlags(0x0008, 0x0040)
    ChrClearFlags(0x0008, 0x0004)
    ChrWalkTo(0x0008, 25500, -2000, 37300, 8000, 0x00)

    @scena.Lambda('lambda_0E09')
    def lambda_0E09():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_0E09)

    ChrWalkTo(0x0008, 25520, -2400, 34680, 8000, 0x00)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0107, 0xFF)
    ChrSetPos(0x0008, 30000, -1000, 8900, 270)

    @scena.Lambda('lambda_0E48')
    def lambda_0E48():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 0)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0E48)

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
            '#0070070806V#562F真是不好意思呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00A2, 0, 0x510))
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x100F
@scena.Code('func_06_100F')
def func_06_100F():
    ChrSetFlags(0x00FE, 0x0020)
    ChrSetFlags(0x00FE, 0x1000)
    PlaySE(125, 0x00, 0x64)
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

# id: 0x0007 offset: 0x10D9
@scena.Code('func_07_10D9')
def func_07_10D9():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 0, 0x510)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1D51',
    )

    EventBegin(0x00)
    MapSetFlags(0x10000000)
    Fade(1000)
    OP_4A(0x0008, 255)
    CameraMove(32000, -1000, 10100, 0)
    ChrSetPos(0x0107, 31500, -1000, 200, 0)
    ChrSetPos(0x0101, 30600, -1000, -800, 0)
    ChrSetPos(0x0102, 31800, -1000, -1000, 0)
    OP_0D()

    @scena.Lambda('lambda_1140')
    def lambda_1140():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1140')

    DispatchAsync2(0x0101, 0x0001, lambda_1140)

    @scena.Lambda('lambda_1151')
    def lambda_1151():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1151')

    DispatchAsync2(0x0102, 0x0001, lambda_1151)

    @scena.Lambda('lambda_1162')
    def lambda_1162():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1162')

    DispatchAsync2(0x0107, 0x0001, lambda_1162)

    @scena.Lambda('lambda_1173')
    def lambda_1173():
        ChrWalkTo(0x00FE, 31300, -1000, 7600, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0002, lambda_1173)

    Sleep(100)

    @scena.Lambda('lambda_1193')
    def lambda_1193():
        ChrWalkTo(0x00FE, 30600, -1000, 6200, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1193)

    Sleep(100)

    @scena.Lambda('lambda_11B3')
    def lambda_11B3():
        ChrWalkTo(0x00FE, 31800, -1000, 6300, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_11B3)

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
    ChrSetFlags(0x0008, 0x0004)

    @scena.Lambda('lambda_1426')
    def lambda_1426():
        CameraMove(32910, -1000, 8880, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1426)

    @scena.Lambda('lambda_143E')
    def lambda_143E():
        ChrWalkTo(0x00FE, 32509, -1000, 10550, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_143E)

    Sleep(300)

    @scena.Lambda('lambda_145E')
    def lambda_145E():
        ChrWalkTo(0x00FE, 34450, -1000, 8450, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_145E)

    WaitForThreadExit(0x0008, 0x0001)
    ChrSetDirection(0x0008, 0, 400)
    WaitForThreadExit(0x0107, 0x0001)
    ChrSetDirection(0x0107, 90, 400)
    WaitForThreadExit(0x0008, 0x0002)
    PlaySE(157, 0x00, 0x64)
    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    LoadEffect(0x00, 'map\\\\mp029_00.eff')
    LoadEffect(0x01, 'map\\\\mp029_01.eff')
    LoadEffect(0x02, 'map\\\\mp029_02.eff')
    PlayEffect(0x01, 0x04, 0x00FF, 31600, -500, 11150, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x05, 0x00FF, 33570, -400, 9620, 0, 0, 0, 300, 300, 300, 0x00FF, 0, 0, 0, 0)
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

    ChrTurnDirection(0x0008, 0x0102, 800)

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

    @scena.Lambda('lambda_175E')
    def lambda_175E():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_175E')

    DispatchAsync2(0x0101, 0x0001, lambda_175E)

    ChrSetDirection(0x0102, 180, 600)
    CreateThread(0x0102, 0x01, 0x00, func_09_2E2F)
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
            '#0540070828V#102F对了，\n',
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
            '#0010070829V#509F#4P触、触角……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 0, 800)

    ChrTalk(
        0x0101,
        (
            '#0010070830V#005F#4P你、你、你说什么～！？',
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
            '#0010070832V#009F#4P为、为什么要我去！？',
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
            '#0010070835V#509F#4P根本不听人家说话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070836V#007F唉，真是的，知道了啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 180, 800)
    ChrWalkTo(0x0101, 31100, -1000, 1000, 6000, 0x00)

    @scena.Lambda('lambda_1987')
    def lambda_1987():
        ChrWalkTo(0x00FE, 20900, 0, 800, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1987)

    CameraMove(34600, -1000, 10700, 2000)
    PlaySE(158, 0x01, 0x64)
    Sleep(200)

    PlayEffect(0x01, 0x00, 0x00FF, 35680, 750, 10480, 0, 0, 0, 400, 400, 400, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0x01, 0x00FF, 35820, 750, 9630, 0, 0, 0, 400, 400, 400, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0x02, 0x00FF, 35390, 930, 7320, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(200)

    PlayEffect(0x01, 0x03, 0x00FF, 35360, 930, 6080, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(600)

    ChrTalk(
        0x0107,
        (
            '#0070070837V#061F#2P……嗯，很顺利呢⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 315, 400)

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
            '#0070070846V#562F#2P爷、爷爷啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_23(0x009E)
    FadeOut(1000, 0, -1)
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
    SetScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    NewScene('ED6_DT01/T3133._SN', 100, 0, 1)
    IdleLoop()

    def _loc_1D51(): pass

    label('loc_1D51')

    Return()

# id: 0x0008 offset: 0x1D52
@scena.Code('func_08_1D52')
def func_08_1D52():
    EventBegin(0x00)
    ChrSetFlags(0x0000, 0x0004)
    ChrSetFlags(0x0001, 0x0004)
    ChrSetFlags(0x0002, 0x0004)
    CameraMove(-300, 0, 2200, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    TerminateThread(0x0008, 0xFF)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 300, 0, 500, 270)
    ChrSetPos(0x0107, 300, 200, 1700, 270)
    ChrSetPos(0x0101, -2300, 200, 500, 90)
    ChrSetPos(0x0102, -2300, 200, 1700, 90)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 255, 0)
    ChrClearFlags(0x0102, 0x0080)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0102, 4)
    ChrSetChipByIndex(0x0107, 5)
    ChrSetFlags(0x0101, 0x0004)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetFlags(0x0107, 0x0004)
    ChrSetSubChip(0x0102, 2)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0540070849V#101F#2P哇哈哈，抱歉抱歉。',
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
            '#0010070852V#509F真是的，亏您还笑得出来。',
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
            '#0540070856V#103F#2P哦，这个小伙子。\n',
            '十分之明白事理嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070857V#101F不如别再当什么游击士了，\n',
            '投身导力技术的研究事业吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0107, 1)

    ChrTalk(
        0x0107,
        (
            '#0070070858V#063F爷爷！真是的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070859V#562F对不起，\n',
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
            '#0540070864V#101F#2P哇哈哈，过奖过奖。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070865V#100F不过话说回来，\n',
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
            '#0540070868V#100F#2P嗯，很久以前就认识了。',
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
            '#0070070870V#061F嘿嘿……\n',
            '我也见过卡西乌斯叔叔哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070871V蓄着胡子，是位很有型的叔叔呢。',
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
            '#0540070876V#103F#2P什么，是什么东西？',
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
    RemoveItem(0x035B, 1)
    Fade(500)
    PlaySE(130, 0x00, 0x64)
    ChrSetPos(0x000A, -900, 800, 270, 0)
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
            '#0540070879V#103F#2P……哦。',
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
            '#0540070881V#102F#2P嗯，这东西很有意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070882V不仅没有生产序号，\n',
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
            '#0540070886V#102F#2P……………………………',
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
            '#0010070889V#002F嗯、嗯……？',
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
            '#0070070891V#064F一点伤痕都没有……',
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
            '#0540070893V#102F#2P看来这个外壳是用\n',
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
            '#0010070895V#505F原、原来是\n',
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
            '#0540070897V#104F#2P唔……\n',
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
            '#0070070900V#060F就是刚才做实验也用过的\n',
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
            '#0010070902V#506F不、不是很明白……\n',
            '用了那个装置会怎么样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070903V#102F#2P简单来说，\n',
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
            '#0020070905V#012F即使如此，\n',
            '能得到重要线索的可能性还是很高吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070906V#102F#2P嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070907V#101F那么事不宜迟……',
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
            '#0540070909V#103F#2P哎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0107, 0)

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
            '#0020070913V#019F可以的话我也来帮忙吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070914V#101F#2P好，那就这样吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070915V晚饭准备好之前，\n',
            '我就先稍微对这个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0107, 1)

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
            '#0540070918V#102F#2P小气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010070919V#007F（怎么说呢，这两爷孙……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070920V#010F（血缘果然是奇妙东西啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T3172._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x2E2F
@scena.Code('func_09_2E2F')
def func_09_2E2F():
    ChrWalkTo(0x00FE, 30800, -1000, 460, 5000, 0x00)
    ChrWalkTo(0x00FE, 23440, 0, 190, 5000, 0x00)
    TerminateThread(0x0101, 0xFF)
    ChrWalkTo(0x00FE, 23100, 2000, 8950, 5000, 0x00)

    @scena.Lambda('lambda_2E75')
    def lambda_2E75():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_2E75)

    ChrWalkTo(0x00FE, 26010, 4000, 9120, 5000, 0x00)
    ChrSetFlags(0x00FE, 0x0080)

    Return()

# id: 0x000A offset: 0x2E9B
@scena.Code('func_0A_2E9B')
def func_0A_2E9B():
    OP_A6(0x0001)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)
    ClearScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Return()

# id: 0x000B offset: 0x2EAD
@scena.Code('func_0B_2EAD')
def func_0B_2EAD():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(34700, -1000, 10700, 0)
    ChrSetPos(0x0008, 34400, -1000, 8900, 0)
    ChrSetPos(0x0107, 32299, -1000, 10400, 0)
    ChrSetPos(0x0101, 32299, -1000, 8400, 45)
    ChrSetPos(0x0102, 32800, -1000, 7400, 45)

    ChrTalk(
        0x0101,
        (
            '#008F展示晚上的拉赛尔工房（※假定）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#100F咳……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070922V既然肚子已经吃饱了，\n',
            '那么就快点开始吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，艾丝蒂尔，\n',
            '把那个导力器放到机器上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, 32900, -1000, 10300, 2000, 0x00)
    ChrSetDirection(0x0101, 90, 400)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#000F这样就好了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#100F嗯，麻烦你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070927V#100F提妲，\n',
            '你那边准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F嗯，很顺利哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#100F很好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么『黑色导力器』的\n',
            '导力波测定实验开始了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F『黑色导力器』？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070932V#000F真是\n',
            '马马乎乎的命名。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540070933V#100FSimple·is·best。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070934V总之\n',
            '没有名字是很不方便的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F好紧张，好兴奋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，提妲也\n',
            '斗志满满呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F嘿嘿～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#100F好，那么开始啰！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070939V提妲。\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0541270001V#100F出力固定在４５％……各种测定器开始待命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F明白……\n',
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F嗯。\n',
            '各种测定器准备工作完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#100F那么，现在正式开始啰。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070946V在找不到出入力的情况下，\n',
            '能探测到其中结晶回路产生的导力波，\n',
            '对其发生的反应进行搜索……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这里就是这个测定装置\n',
            '发挥真正本领的地方！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F还真来劲了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#100F按下按钮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F好、好刺眼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070951V#010F原来如此，这样的话\n',
            '就能增强结晶回路的负荷了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#100F对对……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '提妲，\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070955V怎么回事，好奇怪呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#100F怎么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F转速计的指针\n',
            '在哆哆嗦嗦地震动……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070959V开始骨碌骨碌地转了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#100F什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F哎呀！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#100F这是怎么回事！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F约修亚，这个是……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F那个时候的黑光……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#100F什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T3106._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x34E8
@scena.Code('func_0C_34E8')
def func_0C_34E8():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(34700, -1000, 10700, 0)
    ChrSetPos(0x0008, 34400, -1000, 8900, 0)
    ChrSetPos(0x0107, 32299, -1000, 10400, 0)
    ChrSetPos(0x0101, 23400, 0, 100, 0)
    ChrSetPos(0x0102, 23400, 0, 100, 0)

    ChrTalk(
        0x0101,
        (
            '#005F夜晚以拉赛尔工房为起点\n',
            '照明依次熄灭。（※假定）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F爷爷，\n',
            '不能再继续了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070967V ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#100F唔，还不能停！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070969V再一会就能发现点什么了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, 30300, -1000, 900, 13000, 0x00)
    ChrWalkTo(0x0101, 33400, -1000, 6400, 10000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#000F等一下！\n',
            '城镇里的照明都灭了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 800)

    ChrTalk(
        0x0107,
        (
            '#060F哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 800)

    ChrTalk(
        0x0008,
        (
            '#100F什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '唔，没办法了！\n',
            '实验到此结束！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3695')
    def lambda_3695():
        ChrSetDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_3695)

    ChrSetDirection(0x0008, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#000F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070975V恢复原样了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#060F呼～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#100F记录器呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070978V不行，什么都没记录下来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070979V这么看来，『黑色导力器』\n',
            '上安装的本体是有生命的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070980V接下来全部的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3788')
    def lambda_3788():
        CameraMove(33400, -1000, 10200, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3788)

    ChrWalkTo(0x0102, 30300, -1000, 900, 13000, 0x00)
    ChrWalkTo(0x0102, 31300, -1000, 4800, 6000, 0x00)

    ChrTalk(
        0x0102,
        (
            '#010F太好了……\n',
            '实验好像中止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_37EE')
    def lambda_37EE():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_37EE)

    @scena.Lambda('lambda_37FC')
    def lambda_37FC():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_37FC)

    @scena.Lambda('lambda_380A')
    def lambda_380A():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_380A')

    DispatchAsync2(0x0101, 0x0001, lambda_380A)

    ChrTalk(
        0x0101,
        (
            '#000F啊，约修亚，\n',
            '外面的情况怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0102, 31500, -1000, 6100, 3000, 0x00)

    ChrTalk(
        0x0102,
        (
            '#0020070983V#010F嗯……\n',
            '照明应该都恢复了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070984V只不过大家都还没从骚动里恢复过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '但，这到底\n',
            '是怎么一回事呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#100F是呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '硬要说的话，\n',
            '只能说这是『导力停止现象』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F『导力停止现象』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F就是说导力器内部\n',
            '运作的导力停止工作了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070890002V#060F果然是那个\n',
            '『黑色导力器』的原因……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#100F嗯，不会错的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '但竟能停止这么\n',
            '广范围的导力器呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540070994V呵呵呵呵……\n',
            '这真是出乎意料的东西呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '有趣，实在是太有趣了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F我想现在不是\n',
            '说有趣的情况吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 23400, 0, 100, 0)

    NpcTalk(
        0x0009,
        '男性的声音',
        (
            '混蛋！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3A96')
    def lambda_3A96():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_3A96')

    DispatchAsync2(0x0101, 0x0001, lambda_3A96)

    @scena.Lambda('lambda_3AA7')
    def lambda_3AA7():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_3AA7')

    DispatchAsync2(0x0107, 0x0001, lambda_3AA7)

    @scena.Lambda('lambda_3AB8')
    def lambda_3AB8():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_3AB8')

    DispatchAsync2(0x0102, 0x0001, lambda_3AB8)

    @scena.Lambda('lambda_3AC9')
    def lambda_3AC9():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_3AC9')

    DispatchAsync2(0x0008, 0x0001, lambda_3AC9)

    ChrWalkTo(0x0009, 30300, -1000, 900, 6000, 0x00)
    ChrWalkTo(0x0009, 30500, -1000, 7200, 6000, 0x00)
    ChrWalkTo(0x0009, 32600, -1000, 7800, 6000, 0x00)
    ChrTurnDirection(0x0009, 0x0008, 0)

    ChrTalk(
        0x0008,
        (
            '#100F哦，玛多克，\n',
            '你来的真巧呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#800F一点也不巧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550071000V三番两次了，每次你\n',
            '有新发明都要引起点骚动！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550071001V这次你做了什么，\n',
            '竟把城镇里的照明都弄灭了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3BCC')
    def lambda_3BCC():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3BCC)

    @scena.Lambda('lambda_3BDA')
    def lambda_3BDA():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_3BDA)

    @scena.Lambda('lambda_3BE8')
    def lambda_3BE8():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_3BE8')

    DispatchAsync2(0x0102, 0x0001, lambda_3BE8)

    ChrTalk(
        0x0008,
        (
            '#100F真是失礼呀，\n',
            '这次骚动可和我没关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071003V这是放在那边的\n',
            '『黑色导力器』的杰作哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3C5C')
    def lambda_3C5C():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3C5C)

    @scena.Lambda('lambda_3C6A')
    def lambda_3C6A():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_3C6A)

    @scena.Lambda('lambda_3C78')
    def lambda_3C78():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_3C78')

    DispatchAsync2(0x0102, 0x0001, lambda_3C78)

    ChrTalk(
        0x0009,
        (
            '#800F那，那个就是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '原来如此，那个就是\n',
            '原因的话那这次异常事态就算了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0551250002V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#800F这个怎么可能\n',
            '和你没关系嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3D23')
    def lambda_3D23():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3D23)

    @scena.Lambda('lambda_3D31')
    def lambda_3D31():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_3D31)

    @scena.Lambda('lambda_3D3F')
    def lambda_3D3F():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_3D3F')

    DispatchAsync2(0x0102, 0x0001, lambda_3D3F)

    ChrTalk(
        0x0008,
        (
            '#100F切，识破了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F两个人好像\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F感觉已经经常这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070890003V#060F啊……好丢人呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()

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
    SetScenaFlags(ScenaFlag(0x00A2, 1, 0x511))
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T3100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x3E69
@scena.Code('func_0D_3E69')
def func_0D_3E69():
    EventBegin(0x00)
    CameraMove(-2860, 0, 35210, 0)
    ChrSetFlags(0x0102, 0x0004)
    ChrSetPos(0x0102, -2950, 0, 35300, 225)
    ChrSetPos(0x0101, -4360, 0, 33690, 45)
    ChrSetPos(0x0107, -5900, -2000, 39200, 0)
    ChrSetFlags(0x0107, 0x0080)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010071013V#006F#6P哎呀～\n',
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
            '#0020071015V#019F#5P哈哈，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071016V#013F话说回来，\n',
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
            '#0010071018V#002F#6P嗯……',
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
            '#0070071020V#2P早上好。\n',
            '艾丝蒂尔姐姐、约修亚哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0107, 400)
    ChrClearFlags(0x0107, 0x0080)

    @scena.Lambda('lambda_405B')
    def lambda_405B():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_405B')

    DispatchAsync2(0x0101, 0x0001, lambda_405B)

    @scena.Lambda('lambda_406C')
    def lambda_406C():
        ChrTurnDirection(0x00FE, 0x0107, 0)
        Yield()

        Jump('lambda_406C')

    DispatchAsync2(0x0102, 0x0001, lambda_406C)

    @scena.Lambda('lambda_407D')
    def lambda_407D():
        CameraMove(-2280, 0, 36270, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_407D)

    ChrWalkTo(0x0107, -1800, 0, 39000, 3000, 0x00)
    ChrWalkTo(0x0107, -2250, 0, 36930, 2000, 0x00)
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#0010071021V#501F#6P啊，早啊～\n',
            '提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071022V#019F#4P早上好，\n',
            '昨天真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070071023V#067F嘿嘿，是呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071024V#560F艾丝蒂尔姐姐\n',
            '你们昨晚睡得还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071025V#001F#6P嗯，睡得超饱哦㈱',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071026V#000F说到这个，\n',
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
            '#0070071028V#061F他还对我说\n',
            '『一定要找出黑色导力器的秘密』呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071029V#505F#6P哎呀哎呀～\n',
            '昨晚被工房长先生那样训斥，\n',
            '还是不吸取教训啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071030V#015F#4P很感谢他能帮忙调查那个导力器，\n',
            '但是要这么麻烦他，\n',
            '我们还真是有点过意不去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070071031V#067F啊哈哈，请别介意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071032V爷爷他呢，\n',
            '是自己想调查才会去调查的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071033V#560F啊～对了，\n',
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
            '#0010071035V#006F#6P当然是跟你一起去啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071036V我也想知道那个导力器的真面目。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071037V#010F#4P是啊。\n',
            '我们也希望能帮上点忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070071038V#061F哇，太好了～\n',
            '那我们这就出门吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070071039V#065F啊，不好！\n',
            '汤还在火上呢～！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071040V#067F早饭马上就要做好了，\n',
            '请姐姐你们再稍等一下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0107, 0, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x0107, -1800, 0, 39000, 5000, 0x00)
    ChrWalkTo(0x0107, -5900, -2000, 39200, 5000, 0x00)
    ChrSetFlags(0x0107, 0x0080)
    CameraMove(-2860, 0, 35210, 1000)
    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010071041V#008F#6P那孩子真可爱……',
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
            '#0020071043V#018F#5P艾丝蒂尔，别像个大叔一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T3100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x4627
@scena.Code('func_0E_4627')
def func_0E_4627():
    MapClearFlags(0x10000000)
    EventBegin(0x00)
    CameraMove(-1580, 0, -710, 0)
    ChrSetPos(0x0107, -1130, 0, -1640, 0)
    ChrSetPos(0x0102, -2660, 0, -2900, 0)
    ChrSetPos(0x0101, -2530, 0, -1500, 0)
    ChrSetPos(0x0106, -1330, 0, -3040, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010090426V#006F#5P好了……\n',
            '开始找那个装置吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090427V会放在哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_46E4')
    def lambda_46E4():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_46E4)

    @scena.Lambda('lambda_46F2')
    def lambda_46F2():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_46F2)

    @scena.Lambda('lambda_4700')
    def lambda_4700():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_4700)

    ChrTurnDirection(0x0107, 0x0102, 400)

    ChrTalk(
        0x0107,
        (
            '#0070090428V#560F#2P我想也许是在研究室的角落\n',
            '或者是二楼的书房里吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090429V因为爷爷总是把刚发明的东西\n',
            '随意地丢在一边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090430V#051F听起来是个很奇怪的老爷子嘛。\n',
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

# id: 0x000F offset: 0x47FF
@scena.Code('func_0F_47FF')
def func_0F_47FF():
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00AB, 7, 0x55F))
    OP_28(0x0043, 0x01, 0x0100)

    ChrTalk(
        0x0101,
        (
            '#0010090432V#006F找到啦找到啦⊙',
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
            '#0070090435V#560F嗯……没问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070090436V一切顺利的话，\n',
            '能完全瞒过生命感应器哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x000B, 0x0080)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '感应妨碍器',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(0x0362, 1)

    ChrTalk(
        0x0106,
        (
            '#0050090437V#051F好了，快点回协会吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090438V雾香应该也准备好\n',
            '有关雷斯顿要塞的资料了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_64(0x00, 0x0001)
    EventEnd(0x01)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
