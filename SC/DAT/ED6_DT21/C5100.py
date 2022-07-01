import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5100   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '暴动钢臂（黑）'),
    TXT(0x02, '地震控制用假人'),
    TXT(0x03, '中枢塔入口'),
    TXT(0x04, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5100.x'
    header.mapIndex       = 1
    header.bgm            = 62
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1747
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
        ('ED6_DT29/CH12520._CH', 'ED6_DT29/CH12520P._CP'),
        ('ED6_DT29/CH12521._CH', 'ED6_DT29/CH12521P._CP'),
    ]

# id: 0x10002 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -30,
            z                   = 4000,
            y                   = 47660,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
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
            x                   = 310,
            z                   = 4000,
            y                   = 82310,
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

# id: 0x10003 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x11A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 0,
            y           = 6000,
            z           = -135000,
            range       = 2000,
            dword_10    = 0x000003E8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x0000000C,
        ),
        ScenaEventData(
            x           = -7000,
            y           = 4000,
            z           = -59610,
            range       = 7130,
            dword_10    = 0x00001388,
            dword_14    = 0xFFFF0C54,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000010,
        ),
    )

# id: 0x10005 offset: 0x15A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -27960,
            triggerZ            = 4000,
            triggerY            = -101880,
            triggerRange        = 800,
            actorX              = -27560,
            actorZ              = 5000,
            actorY              = -101880,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -26160,
            triggerZ            = 4000,
            triggerY            = -102500,
            triggerRange        = 800,
            actorX              = -26140,
            actorZ              = 6000,
            actorY              = -102180,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1A2
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_1B3',
    )

    OP_A3(0x10F0)
    Event(0, 0x000D)

    Jump('loc_1E1')

    def _loc_1B3(): pass

    label('loc_1B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_1C4',
    )

    OP_A3(0x10F1)
    Event(0, 0x0009)

    Jump('loc_1E1')

    def _loc_1C4(): pass

    label('loc_1C4')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x65),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1E1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 0, 0x2230)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E1',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0004)

    def _loc_1E1(): pass

    label('loc_1E1')

    Return()

# id: 0x0001 offset: 0x1E2
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFE0C00, 0xFFFD92E8, 0x00230071)
    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_6F(0x0000, 0)
    OP_71(0x0003, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 6, 0x223E)),
            Expr.Return,
        ),
        'loc_255',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x42),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_10(0x02, 0x01)
    OP_64(0x00, 0x0001)
    OP_71(0x0004, 0x0004)
    OP_72(0x0001, 0x0010)
    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0008)
    OP_6F(0x0001, 30)
    CreateThread(0x0009, 0x03, 0x00, 0x0003)
    SetMapFlags(0x02000000)
    SetMapFlags(0x00100000)
    OP_22(0x0085, 0x01, 0x46)

    Jump('loc_262')

    def _loc_255(): pass

    label('loc_255')

    OP_10(0x02, 0x00)
    OP_71(0x0001, 0x0004)
    OP_22(0x01C7, 0x00, 0x64)

    def _loc_262(): pass

    label('loc_262')

    Return()

# id: 0x0002 offset: 0x263
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_278',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_278(): pass

    label('loc_278')

    Return()

# id: 0x0003 offset: 0x279
@scena.Code('func_03_279')
def func_03_279():
    OP_C4(0x00, 0x00000020)
    def _loc_27F(): pass

    label('loc_27F')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2A1',
    )

    OP_7C(0x0000003C, 0x0000003C, 0x000003E8, 0x00000384)
    Sleep(1000)

    Jump('loc_27F')

    def _loc_2A1(): pass

    label('loc_2A1')

    Return()

# id: 0x0004 offset: 0x2A2
@scena.Code('func_04_2A2')
def func_04_2A2():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2B9',
    )

    Call(0, 0x000E)
    Call(0, 0x000F)

    def _loc_2B9(): pass

    label('loc_2B9')

    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    OP_6D(26370, 4000, -100180, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    Sleep(500)

    OP_6F(0x0002, 0)
    OP_70(0x0002, 0x0000001E)
    OP_22(0x006D, 0x00, 0x64)
    OP_73(0x0002)
    CreateThread(0x0101, 0x01, 0x00, 0x0005)
    Sleep(800)

    LoadEffect(0x00, 'map\\mp096_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 25500, 9000, -106000, -20, 0, 25, 800, 800, 800, 0x00FF, 0, 0, 0, 0)
    CreateThread(0x0102, 0x01, 0x00, 0x0006)
    Sleep(800)

    CreateThread(0x00F8, 0x01, 0x00, 0x0007)
    Sleep(800)

    CreateThread(0x00F9, 0x01, 0x00, 0x0008)

    @scena.Lambda('lambda_03AC')
    def lambda_03AC():
        OP_6D(26630, 4000, -104390, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_03AC)

    @scena.Lambda('lambda_03C4')
    def lambda_03C4():
        OP_67(0, 5830, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_03C4)

    @scena.Lambda('lambda_03DC')
    def lambda_03DC():
        OP_6B(3650, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_03DC)

    WaitForThreadExit(0x0102, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    OP_6F(0x0002, 30)
    OP_70(0x0002, 0x00000000)

    ChrTalk(
        0x0101,
        (
            '#0010401012V#1007F#5P好、好刺眼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010401013V#1004F咦，这里是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x0102, 315, 400)

    ChrTalk(
        0x0102,
        (
            '#0020401014V#1042F#6P艾丝蒂尔……那个！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_DB()
    Sleep(100)

    Fade(500)
    OP_6D(13060, 4000, -109970, 0)
    OP_67(0, 6220, -10000, 0)
    OP_6B(8560, 0)
    OP_6C(348000, 0)
    OP_6E(262, 0)
    OP_6D(11490, 4000, -99590, 0)
    OP_67(0, 6540, -10000, 0)
    OP_6B(7760, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_0524')
    def lambda_0524():
        OP_6D(50, 4000, 33050, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0524)

    @scena.Lambda('lambda_053C')
    def lambda_053C():
        OP_67(0, 3780, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_053C)

    @scena.Lambda('lambda_0554')
    def lambda_0554():
        OP_6B(4190, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0554)

    @scena.Lambda('lambda_0564')
    def lambda_0564():
        OP_6C(0, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0564)

    @scena.Lambda('lambda_0574')
    def lambda_0574():
        OP_6E(412, 10000)

        ExitThread()

    DispatchAsync(0x00F8, 0x0002, lambda_0574)

    @scena.Lambda('lambda_0584')
    def lambda_0584():
        OP_8C(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0584)

    Sleep(50)

    @scena.Lambda('lambda_0597')
    def lambda_0597():
        OP_8C(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0597)

    Sleep(50)

    @scena.Lambda('lambda_05AA')
    def lambda_05AA():
        OP_8C(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_05AA)

    Sleep(9000)

    FadeOut(1000, 0, -1)
    OP_0D()
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0101, 0x03)
    OP_A2(0x10F1)
    NewScene('ED6_DT21/C5101._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x5D7
@scena.Code('func_05_5D7')
def func_05_5D7():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 27960, 4000, -98520, 180)
    OP_8E(0x00FE, 27960, 4000, -106620, 2000, 0x00)

    Return()

# id: 0x0006 offset: 0x602
@scena.Code('func_06_602')
def func_06_602():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 27960, 4000, -98520, 180)
    OP_8E(0x00FE, 27960, 4000, -102640, 2000, 0x00)
    OP_8E(0x00FE, 26470, 4000, -105260, 2000, 0x00)
    OP_8C(0x00FE, 180, 400)

    Return()

# id: 0x0007 offset: 0x648
@scena.Code('func_07_648')
def func_07_648():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 27960, 4000, -98520, 180)
    OP_8E(0x00FE, 27960, 4000, -102640, 2000, 0x00)
    OP_8E(0x00FE, 29260, 4000, -105880, 2000, 0x00)
    OP_8C(0x00FE, 135, 400)

    Return()

# id: 0x0008 offset: 0x68E
@scena.Code('func_08_68E')
def func_08_68E():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrPos(0x00FE, 27960, 4000, -98520, 180)
    OP_8E(0x00FE, 27590, 4000, -104340, 2000, 0x00)

    Return()

# id: 0x0009 offset: 0x6B9
@scena.Code('func_09_6B9')
def func_09_6B9():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_6D0',
    )

    Call(0, 0x000E)
    Call(0, 0x000F)

    def _loc_6D0(): pass

    label('loc_6D0')

    OP_6D(18100, 4000, -99210, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3820, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 17390, 4000, -98710, 0)
    SetChrPos(0x0102, 18670, 4000, -98620, 0)
    SetChrPos(0x00F8, 18060, 4000, -100190, 0)
    SetChrPos(0x00F9, 19290, 4000, -100050, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7A1',
    )

    ChrTalk(
        0x0108,
        (
            '#0080401015V#072F#6P那就是『中枢塔』吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_927')

    def _loc_7A1(): pass

    label('loc_7A1')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7E2',
    )

    ChrTalk(
        0x0106,
        (
            '#0050401016V#057F#6P那就是『中枢塔』吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_927')

    def _loc_7E2(): pass

    label('loc_7E2')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_824',
    )

    ChrTalk(
        0x0109,
        (
            '#0180401017V#1063F#6P那就是『中枢塔』吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_927')

    def _loc_824(): pass

    label('loc_824')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_86A',
    )

    ChrTalk(
        0x0104,
        (
            '#0040401018V#030F#6P嗯……\n',
            '那就是『中枢塔』吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_927')

    def _loc_86A(): pass

    label('loc_86A')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8AB',
    )

    ChrTalk(
        0x0103,
        (
            '#0030401019V#022F#6P那就是『中枢塔』吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_927')

    def _loc_8AB(): pass

    label('loc_8AB')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8EB',
    )

    ChrTalk(
        0x0105,
        (
            '#0060401020V#1162F#6P那就是『中枢塔』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_927')

    def _loc_8EB(): pass

    label('loc_8EB')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_927',
    )

    ChrTalk(
        0x0107,
        (
            '#0070401021V#065F#6P那就是『中枢塔』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_927(): pass

    label('loc_927')

    If(
        (
            (Expr.Eval, "OP_42(0x0A)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_999',
    )

    ChrTalk(
        0x010B,
        (
            '#0090401022V#212F#6P……坠落以来，\n',
            '一直看着那个塔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090401023V没想到是这么高大的塔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C72')

    def _loc_999(): pass

    label('loc_999')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A09',
    )

    ChrTalk(
        0x0107,
        (
            '#0070401024V#065F#6P远、远看虽然\n',
            '也觉得很高大……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070401025V但没想到是如此巨大的塔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C72')

    def _loc_A09(): pass

    label('loc_A09')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A74',
    )

    ChrTalk(
        0x0105,
        (
            '#0060401026V#1162F#6P远看也觉得\n',
            '相当的大……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060401027V没想到竟是这么大的塔啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C72')

    def _loc_A74(): pass

    label('loc_A74')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AF6',
    )

    ChrTalk(
        0x0103,
        (
            '#0030401028V#025F#6P……远看也觉得\n',
            '相当的大……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030401029V#022F但这样近距离仰望之下\n',
            '还真是超乎想象啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C72')

    def _loc_AF6(): pass

    label('loc_AF6')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B76',
    )

    ChrTalk(
        0x0104,
        (
            '#0040401030V#035F#6P呀呀，远看\n',
            '也觉得是很大的建筑物……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040401031V#030F却没想到是这么\n',
            '高层的建筑物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C72')

    def _loc_B76(): pass

    label('loc_B76')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C06',
    )

    ChrTalk(
        0x0109,
        (
            '#0180401032V#1065F#6P即使在远处看也觉得\n',
            '是座非常高的塔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180401033V#1063F但这样近距离仰望之下\n',
            '还真是超乎预想的大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C72')

    def _loc_C06(): pass

    label('loc_C06')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C72',
    )

    ChrTalk(
        0x0106,
        (
            '#0050401034V#052F#6P远眺之下\n',
            '觉得是座很大的塔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050401035V#057F但没想到竟然这么大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C72(): pass

    label('loc_C72')

    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0101)
    Sleep(500)

    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010401036V#1025F#5P……对了，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010401037V莱维和教授\n',
            '他们在那里吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020401038V#1043F#4P……我认为可能性很高。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020401039V#1042F看起来像是掌控\n',
            '都市中枢的地方。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020401040V说不定也会有\n',
            '『辉之环』的线索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010360573V#1010F#5P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010401042V#1002F……怎么办？\n',
            '就这样冲进去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020401043V#1035F#4P……如果莱维他们在，\n',
            '我想可能会遭遇到\n',
            '前所未有的严酷战斗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020401044V#1040F先回『埃尔赛尤』\n',
            '做好万全的准备才是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020401045V<FIXME>#1040Fユリア大尉にも探索状況を\n',
            '報告しておきたいしね。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010401046V#1006F#5P嗯……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F25',
    )

    ChrTalk(
        0x0108,
        (
            '#0080401047V#070F#6P好，那么\n',
            '赶快寻找站点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10AC')

    def _loc_F25(): pass

    label('loc_F25')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F69',
    )

    ChrTalk(
        0x0106,
        (
            '#0050401048V#051F#6P好，那么\n',
            '赶快寻找站点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10AC')

    def _loc_F69(): pass

    label('loc_F69')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FAA',
    )

    ChrTalk(
        0x0109,
        (
            '#0180401049V#1060F#6P那就赶快\n',
            '寻找站点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10AC')

    def _loc_FAA(): pass

    label('loc_FAA')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FEE',
    )

    ChrTalk(
        0x0104,
        (
            '#0040401050V#035F#6P呼，那就赶快\n',
            '寻找站点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10AC')

    def _loc_FEE(): pass

    label('loc_FEE')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_102E',
    )

    ChrTalk(
        0x0103,
        (
            '#0030401051V#027F#6P那就赶快\n',
            '寻找站点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10AC')

    def _loc_102E(): pass

    label('loc_102E')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_106F',
    )

    ChrTalk(
        0x0105,
        (
            '#0060401052V#1160F#6P那就赶快\n',
            '寻找站点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10AC')

    def _loc_106F(): pass

    label('loc_106F')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10AC',
    )

    ChrTalk(
        0x0107,
        (
            '#0070401053V#061F#6P那就赶快\n',
            '寻找站点吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10AC(): pass

    label('loc_10AC')

    OP_A2(0x2230)
    OP_28(0x009E, 0x01, 0x0800)
    OP_28(0x009E, 0x01, 0x1000)
    OP_28(0x009F, 0x04, 0x02)
    OP_28(0x009F, 0x04, 0x08)
    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x10C8
@scena.Code('func_0A_10C8')
def func_0A_10C8():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门牢牢地锁着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x000B offset: 0x10F5
@scena.Code('func_0B_10F5')
def func_0B_10F5():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '【紧急避难通道】\n',
            '中枢塔≌ 卡尔玛丽',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '只有在来自『中枢塔』的\n',
            '导力供给产生异常的情况下\n',
            '才会自动解除锁定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '此外，门边\n',
            '禁止放置会\n',
            '妨碍避难的物体。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x000C offset: 0x11C0
@scena.Code('func_0C_11C0')
def func_0C_11C0():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 6, 0x223E)),
            Expr.Return,
        ),
        'loc_11C8',
    )

    Return()

    def _loc_11C8(): pass

    label('loc_11C8')

    EventBegin(0x00)
    Fade(1000)
    OP_6D(-290, 6000, -134740, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0101, 0, 6000, -134000, 0)
    OP_89(0x0102, -1000, 6000, -135000, 0)
    OP_89(0x00F8, 1000, 6000, -135000, 0)
    OP_89(0x00F9, 0, 6000, -136000, 0)
    OP_0D()
    Sleep(100)

    SetMapFlags(0x00100000)
    OP_22(0x00EB, 0x00, 0x64)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 0x00000258)

    @scena.Lambda('lambda_1274')
    def lambda_1274():
        OP_6D(-290, 55000, -134740, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1274)

    @scena.Lambda('lambda_128C')
    def lambda_128C():
        OP_67(0, 10570, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_128C)

    @scena.Lambda('lambda_12A4')
    def lambda_12A4():
        OP_6C(320000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_12A4)

    Sleep(2000)

    Sleep(1500)

    Sleep(1500)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene('ED6_DT21/C6003._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000D offset: 0x12D5
@scena.Code('func_0D_12D5')
def func_0D_12D5():
    EventBegin(0x00)
    OP_6D(-290, 45000, -134740, 0)
    OP_67(0, 10570, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(320000, 0)
    OP_6E(262, 0)
    OP_6F(0x0000, 500)
    Yield()
    OP_89(0x0101, 0, 70000, -134000, 0)
    OP_89(0x0102, -1000, 70000, -135000, 0)
    OP_89(0x00F8, 1000, 70000, -135000, 0)
    OP_89(0x00F9, 0, 70000, -136000, 0)
    OP_22(0x00EB, 0x00, 0x64)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_1374')
    def lambda_1374():
        OP_6D(-290, 6000, -134740, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1374)

    @scena.Lambda('lambda_138C')
    def lambda_138C():
        OP_67(0, 6500, -10000, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_138C)

    @scena.Lambda('lambda_13A4')
    def lambda_13A4():
        OP_6C(315000, 9000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_13A4)

    OP_70(0x0000, 0x00000000)
    OP_73(0x0000)
    OP_23(0x00EB)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(200)

    Fade(500)
    OP_6D(240, 6010, -133220, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 240, 6010, -133220, 0)
    SetChrPos(0x0001, 240, 6010, -133220, 0)
    SetChrPos(0x0002, 240, 6010, -133220, 0)
    SetChrPos(0x0003, 240, 6010, -133220, 0)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x000E offset: 0x144F
@scena.Code('func_0E_144F')
def func_0E_144F():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_14C9'),
        (0x00000001, 'loc_14CF'),
        (-1, 'loc_14D5'),
    )

    def _loc_14C9(): pass

    label('loc_14C9')

    OP_A2(0x1200)

    Jump('loc_14D5')

    def _loc_14CF(): pass

    label('loc_14CF')

    OP_A2(0x1201)

    Jump('loc_14D5')

    def _loc_14D5(): pass

    label('loc_14D5')

    Return()

# id: 0x000F offset: 0x14D6
@scena.Code('func_0F_14D6')
def func_0F_14D6():
    FadeOut(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            0x0000,
            0x0001,
            0x00FF,
            0x00FF,
        ),
        (
            0x0005,
            0x0002,
            0x0004,
            0x0003,
            0x0006,
            0x0007,
            0x0008,
            0x000A,
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0x00000000)

    Return()

# id: 0x0010 offset: 0x1569
@scena.Code('func_10_1569')
def func_10_1569():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 6, 0x223E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1572',
    )

    Return()

    def _loc_1572(): pass

    label('loc_1572')

    EventBegin(0x02)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1612',
    )

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_158B'),
        (0x00000001, 'loc_15CD'),
        (-1, 'loc_160F'),
    )

    def _loc_158B(): pass

    label('loc_158B')

    ChrTalk(
        0x0101,
        (
            '#0010421092V#1002F这里是『中枢塔』吧。\n',
            '……必须回去才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_160F')

    def _loc_15CD(): pass

    label('loc_15CD')

    ChrTalk(
        0x0102,
        (
            '#0020421093V#1042F这里是『中枢塔』了。\n',
            '……必须回去才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_160F')

    def _loc_160F(): pass

    label('loc_160F')

    Jump('loc_16FF')

    def _loc_1612(): pass

    label('loc_1612')

    Switch(
        (
            (Expr.PushValueByIndex, 0xA),
            Expr.Return,
        ),
        (0x00000000, 'loc_1622'),
        (0x00000001, 'loc_1663'),
        (-1, 'loc_1698'),
    )

    def _loc_1622(): pass

    label('loc_1622')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020421094V#1042F艾丝蒂尔！\n',
            '那边是『中枢塔』哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1698')

    def _loc_1663(): pass

    label('loc_1663')

    ChrTalk(
        0x0102,
        (
            '#0020421095V#1042F不是！　这边是『中枢塔』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1698')

    def _loc_1698(): pass

    label('loc_1698')

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010421096V#1002F……避难通道在前面啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020421097V#1042F啊啊……赶快吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)
    def _loc_16FF(): pass

    label('loc_16FF')

    OP_90(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)
    SetMapFlags(0x02000000)
    SetMapFlags(0x00100000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
