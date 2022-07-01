import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4133_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4133   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '管事福利兹'),
    TXT(0x02, '提妲'),
    TXT(0x03, '玲'),
    TXT(0x04, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4133.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1C36
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
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT27/CH03510._CH', 'ED6_DT27/CH03510P._CP'),
    ]

# id: 0x10002 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 7410,
            z                   = 0,
            y                   = 3300,
            direction           = 180,
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
    )

# id: 0x10005 offset: 0x122
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 7200,
            triggerZ            = 0,
            triggerY            = 1690,
            triggerRange        = 800,
            actorX              = 7410,
            actorZ              = 1500,
            actorY              = 3300,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 7000,
            triggerZ            = 0,
            triggerY            = 4890,
            triggerRange        = 800,
            actorX              = 7000,
            actorZ              = 1000,
            actorY              = 4890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x16A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_17D',
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x0005)

    def _loc_17D(): pass

    label('loc_17D')

    Return()

# id: 0x0001 offset: 0x17E
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x17F
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A4',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_2E6')

    def _loc_1A4(): pass

    label('loc_1A4')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BD',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_2E6')

    def _loc_1BD(): pass

    label('loc_1BD')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D6',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_2E6')

    def _loc_1D6(): pass

    label('loc_1D6')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1EF',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_2E6')

    def _loc_1EF(): pass

    label('loc_1EF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_208',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_2E6')

    def _loc_208(): pass

    label('loc_208')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_221',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_2E6')

    def _loc_221(): pass

    label('loc_221')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_23A',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_2E6')

    def _loc_23A(): pass

    label('loc_23A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_253',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_2E6')

    def _loc_253(): pass

    label('loc_253')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_26C',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_2E6')

    def _loc_26C(): pass

    label('loc_26C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_285',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_2E6')

    def _loc_285(): pass

    label('loc_285')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29E',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_2E6')

    def _loc_29E(): pass

    label('loc_29E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B7',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_2E6')

    def _loc_2B7(): pass

    label('loc_2B7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D0',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_2E6')

    def _loc_2D0(): pass

    label('loc_2D0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E6',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_2E6(): pass

    label('loc_2E6')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2FB',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_2E6')

    def _loc_2FB(): pass

    label('loc_2FB')

    Return()

# id: 0x0003 offset: 0x2FC
@scena.Code('func_03_2FC')
def func_03_2FC():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x301
@scena.Code('func_04_301')
def func_04_301():
    TalkBegin(0x0008)

    ChrTalk(
        0x0008,
        (
            '◆没有台词。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x31A
@scena.Code('func_05_31A')
def func_05_31A():
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
        'loc_32D',
    )

    Call(0, 0x0006)

    def _loc_32D(): pass

    label('loc_32D')

    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x0101, 6950, 0, 1690, 0)
    SetChrPos(0x00F7, 8109, 0, 1700, 0)
    SetChrPos(0x000A, 7130, 0, 450, 0)
    SetChrPos(0x0009, 8039, 0, 590, 0)
    OP_6D(7310, 0, 2300, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(309000, 0)
    OP_6E(262, 0)
    OP_4A(0x0008, 255)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#2230251549V你们是游击士协会的吧？\n',
            '我已经收到联络了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2230251550V不巧，没有\n',
            '４人房了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2230251551V能不能请你们分住\n',
            '两间双人房？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_510',
    )

    ChrTalk(
        0x0101,
        (
            '#0010190450V#1004F#6P哦，这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 90, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010251553V#1015F#5P阿加特。\n',
            '那么怎么分呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050251554V#051F#4P我无所谓。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050251555V你们来\n',
            '决定吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5C1')

    def _loc_510(): pass

    label('loc_510')

    ChrTalk(
        0x0101,
        (
            '#0010190450V#1004F#6P哦，这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 90, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010251557V#1015F#5P雪拉姐。\n',
            '那么怎么分呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030251558V#027F#4P我怎么住都行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030251559V你们来\n',
            '决定吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5C1(): pass

    label('loc_5C1')

    ChrTalk(
        0x000A,
        (
            '#0220251560V#265F#6P那玲就和姐姐\n',
            '一起吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251561V姐姐成天工作，\n',
            '也没办法好好聊聊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0625')
    def lambda_0625():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0625)

    @scena.Lambda('lambda_0633')
    def lambda_0633():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0633)

    ChrTurnDirection(0x0101, 0x000A, 400)
    OP_62(0x0009, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(300)

    ChrTalk(
        0x0009,
        (
            '#0070251562V#065F#6P啊，小玲好狡猾。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070251563V我也想和姐姐\n',
            '一个房间……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0009, 400)

    ChrTalk(
        0x000A,
        (
            '#0220251564V#263F#5P哼哼，先到先得哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251565V#260F那么你跟我\n',
            '挤一张床？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070251566V#061F#6P嘿嘿，我逗你的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070251567V今晚就把姐姐\n',
            '让给小玲了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220251568V#261F#5P呵呵。\n',
            '谢谢你，提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010251569V#1016F#5P嗯……\n',
            '我被让出去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_889',
    )

    ChrTalk(
        0x0106,
        (
            '#0050251570V#051F#2P那么我和\n',
            '小不点一起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050251571V哈哈，让我想起和老爷子\n',
            '还有你潜伏时的情景。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0009, 0, 400)

    ChrTalk(
        0x0009,
        (
            '#0070251572V#560F#6P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070251573V#067F嘿嘿，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_935')

    def _loc_889(): pass

    label('loc_889')

    ChrTalk(
        0x0103,
        (
            '#0030251574V#021F#2P呵呵，你还真受欢迎。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030251575V#027F那么我就和\n',
            '提妲一起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030251576V我们在睡前\n',
            '用塔罗牌做游戏吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0009, 0, 400)

    ChrTalk(
        0x0009,
        (
            '#0070251577V#061F#6P嗯，好啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_935(): pass

    label('loc_935')

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrPos(0x0101, 35000, 0, 106370, 0)
    SetChrPos(0x000A, 35000, 0, 106370, 0)
    OP_6D(35000, 0, 113130, 0)
    OP_67(0, 6110, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(239, 0)
    OP_6B(1890, 0)
    OP_6C(315000, 0)
    OP_6E(437, 0)
    OP_9F(0x0101, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x000A, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(1000, 0)
    OP_22(0x0006, 0x00, 0x64)
    Sleep(500)

    ClearChrFlags(0x000A, 0x0080)

    @scena.Lambda('lambda_0A03')
    def lambda_0A03():
        OP_6D(34540, 0, 115470, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0A03)

    @scena.Lambda('lambda_0A1B')
    def lambda_0A1B():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_0A1B)

    @scena.Lambda('lambda_0A2D')
    def lambda_0A2D():
        OP_8E(0x00FE, 34420, 0, 114010, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0A2D)

    Sleep(600)

    ClearChrFlags(0x0101, 0x0080)

    @scena.Lambda('lambda_0A52')
    def lambda_0A52():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0A52)

    @scena.Lambda('lambda_0A64')
    def lambda_0A64():
        OP_8E(0x00FE, 35770, 0, 114090, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A64)

    WaitForThreadExit(0x000A, 0x0001)
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x000A,
        (
            '#0220251578V#265F#5P哇，这跟我和爸爸妈妈\n',
            '一起住的房间不一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000A, 45, 400)
    Sleep(500)

    OP_8C(0x000A, 0, 400)
    OP_8C(0x000A, 270, 400)
    Sleep(500)

    OP_8C(0x000A, 0, 400)

    ChrTalk(
        0x000A,
        (
            '#0220251579V#261F#5P从前面的窗户还能\n',
            '看见高大的建筑物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251580V#1026F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_AD(0x002400C2, 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    Sleep(2000)

    OP_AE(0x000001F4)
    Sleep(1500)

    ChrTurnDirection(0x000A, 0x0101, 400)

    ChrTalk(
        0x000A,
        (
            '#0220251581V#264F#5P怎么了？姐姐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000A, 400)

    ChrTalk(
        0x0101,
        (
            '#0010251582V#1016F#6P啊，嗯，有点出神了',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251583V#1025F话说回来……\n',
            '小玲，对不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251584V一直没能找到\n',
            '你的爸爸妈妈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220251585V#260F#5P不，没关系的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251586V因为爸爸妈妈\n',
            '说好一定会\n',
            '来接玲的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251587V姐姐你们不用\n',
            '勉强找他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251588V#1026F#6P可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220251589V#263F#5P玲的爸爸妈妈\n',
            '捉迷藏很拿手的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251590V虽然比不上玲那样擅长。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251591V所以没那么容易\n',
            '找到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251592V#1016F#6P哈哈，是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251593V#1006F那我们就不勉强了，\n',
            '仔细地慢慢找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220251594V#261F#5P嗯，这就对了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251595V#260F不过……\n',
            '玲有两个愿望\n',
            '要姐姐满足。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251596V#1004F#6P愿望？　是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220251597V#1306F#5P哎呀，不可以。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251598V在说好答应我\n',
            '之前我不能说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251599V#1016F#6P给我来这一手……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251600V#1006F只要我办得到就都\n',
            '满足你，行了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220251601V#261F#5P真的？　太好了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251602V#260F第一个愿望是……\n',
            '叫我玲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251603V#1015F#6P？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251604V#1004F啊……！\n',
            '不再叫你小玲？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220251605V#260F#5P嗯，没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251606V#266F你明明对提妲直呼其名，\n',
            '却总是叫我『小玲』，\n',
            '这可有点不公平。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251607V#1016F#6P哈哈……是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251608V#1011F嗯，这个不难……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251609V那么你能不能也\n',
            '叫我艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220251610V#264F#5P叫姐姐你？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251611V#267F艾丝蒂尔……艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251612V#261F嗯，好像也不坏⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251613V#1016F#6P啊哈哈……\n',
            '那就这么定了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251614V#1006F今后请多关照，玲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220251615V#265F#5P彼此彼此，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251616V#261F呵呵……真开心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251617V#1017F#6P呵呵，那就好那就好',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251618V那么玲的\n',
            '另一个愿望是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220251619V#267F#5P嗯，是这样的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251620V能不能告诉我，你刚才\n',
            '进房间时为什么会感到吃惊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251621V#1026F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220251622V#268F#5P艾丝蒂尔那时有一种\n',
            '悲伤的表情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251623V所以我挺在意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251624V#1003F#6P……是这个啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251625V#1025F以前，我曾和一个人\n',
            '同住过这间房间。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251626V刚才有点回忆起\n',
            '那个人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220251627V#265F#5P哇！\n',
            '肯定是恋人吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251628V#1017F#6P呵呵……\n',
            '很遗憾，不是这样的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251629V他和我在一个家庭中长大，\n',
            '像我的兄弟一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251630V虽然现在不在\n',
            '我身边……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220251631V#264F#5P这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251632V#265F那个哥哥是个\n',
            '什么样的人呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251633V名字叫什么？　长相如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251634V#1025F#6P啊，嗯……\n',
            '他叫约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251635V黑发、琥珀色的眼睛，\n',
            '应该算相当英俊吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251636V#1015F嗯～比起英俊这种形容法，\n',
            '可能更应该说他是个美人吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220251637V#264F#5P美人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251638V#1016F#6P呵呵，因为他还在戏里\n',
            '演过公主呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251639V而且我跟你说，那叫\n',
            '一个像啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220251640V#261F#5P哇，好厉害～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251641V玲也好想\n',
            '见到他。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251642V我说我说，什么时候能见他？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251643V#1025F#6P啊，嗯……\n',
            '这就不好说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220251644V#267F#5P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251645V你是不是因为不知道\n',
            '什么时候能见到他才感到悲伤？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251646V#1006F#6P……不，这倒没有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251647V因为不管用多少年的时间，\n',
            '我都要带他回家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220251648V#264F#5P那么是因为什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251649V#1025F#6P因为我想约修亚\n',
            '现在一定在勉强自己……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251650V#1003F可是……\n',
            '可我却不能在他身边支持他，\n',
            '……就有点悲伤。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220251651V#262F#5P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251652V#1016F#6P哈哈，抱歉抱歉',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251653V#1025F这些对不了解情况的玲来说\n',
            '一定是很没意思吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220251654V#263F#5P不，完全没有。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251655V#260F那个叫约修亚的\n',
            '哥哥一定是个很棒的人吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251656V#1007F#6P很棒的人吗……\n',
            '我倒是觉得他很过分。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251657V#1013F用了那样自说自话的道别方式，\n',
            '……我、我的第一次就那么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220251658V#264F#5P？　第一次？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251659V#1004F#6P啊，没什么的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251660V#1016F今天我们都累了，\n',
            '准备睡觉吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220251661V#1301F#5P啊，不许蒙混过关！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251662V#266F讨厌，在你全部招供之前\n',
            '我绝对不睡！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251663V#1015F#6P呜呜，糟糕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '后来，艾丝蒂尔她们在上床以后\n',
            '又聊了很多无关紧要的内容。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '玲逐渐地在恍惚间\n',
            '发出了平稳的鼾声……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '劳累的艾丝蒂尔也很快\n',
            '失去了意识。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(200)

    OP_A2(0x10F0)
    NewScene('ED6_DT21/R1504._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x1B33
@scena.Code('func_06_1B33')
def func_06_1B33():
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
        (0x00000000, 'loc_1BAD'),
        (0x00000001, 'loc_1BB3'),
        (-1, 'loc_1BB9'),
    )

    def _loc_1BAD(): pass

    label('loc_1BAD')

    OP_A2(0x1200)

    Jump('loc_1BB9')

    def _loc_1BB3(): pass

    label('loc_1BB3')

    OP_A2(0x1201)

    Jump('loc_1BB9')

    def _loc_1BB9(): pass

    label('loc_1BB9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1BC7',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_1BCB')

    def _loc_1BC7(): pass

    label('loc_1BC7')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_1BCB(): pass

    label('loc_1BCB')

    Return()

# id: 0x0007 offset: 0x1BCC
@scena.Code('func_07_1BCC')
def func_07_1BCC():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　　　　　事务室\n',
            '※无关人员请勿入内',
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
