import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R3403_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R3403   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '鲁迪'),
    TXT(0x02, '安东尼'),
    TXT(0x03, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'R3403.x'
    header.mapIndex       = 1
    header.bgm            = 30
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/R3403._SN', 'ED6_DT01/R3403_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x18A7
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
        ('ED6_DT07/CH01500._CH', 'ED6_DT07/CH01500P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
    ]

# id: 0x10002 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 612030,
            z                   = -50,
            y                   = -62600,
            direction           = 359,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
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
    )

# id: 0x10003 offset: 0xFA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xFA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 602300,
            y           = -1000,
            z           = -48740,
            range       = 599000,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFF13E8,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000007,
        ),
    )

# id: 0x10005 offset: 0x11A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x11A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_129',
    )

    Jump('loc_156')

    def _loc_129(): pass

    label('loc_129')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_141',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x52),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_156')

    def _loc_141(): pass

    label('loc_141')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_156',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_156(): pass

    label('loc_156')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_166'),
        (0x00000065, 'loc_178'),
        (-1, 'loc_198'),
    )

    def _loc_166(): pass

    label('loc_166')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 7, 0x507)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_175',
    )

    SetScenaFlags(ScenaFlag(0x00A0, 7, 0x507))
    Event(0, 0x0005)

    def _loc_175(): pass

    label('loc_175')

    Jump('loc_198')

    def _loc_178(): pass

    label('loc_178')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 4, 0x534)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_195',
    )

    SetMapFlags(0x10000000)
    SetScenaFlags(ScenaFlag(0x00A6, 4, 0x534))
    Event(0, 0x0006)

    def _loc_195(): pass

    label('loc_195')

    Jump('loc_198')

    def _loc_198(): pass

    label('loc_198')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_1A7',
    )

    ClearChrFlags(0x0008, 0x0080)

    Jump('loc_207')

    def _loc_1A7(): pass

    label('loc_1A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_1B1',
    )

    Jump('loc_207')

    def _loc_1B1(): pass

    label('loc_1B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1BB',
    )

    Jump('loc_207')

    def _loc_1BB(): pass

    label('loc_1BB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1DB',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 610200, -40, -62060, 180)

    Jump('loc_207')

    def _loc_1DB(): pass

    label('loc_1DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_1E5',
    )

    Jump('loc_207')

    def _loc_1E5(): pass

    label('loc_1E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_207',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0010)
    SetChrPos(0x0008, 618600, -10, -47550, 46)

    def _loc_207(): pass

    label('loc_207')

    Return()

# id: 0x0001 offset: 0x208
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, 487000, -180000, 196666)

    Return()

# id: 0x0002 offset: 0x21B
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_230',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_230(): pass

    label('loc_230')

    Return()

# id: 0x0003 offset: 0x231
@scena.Code('func_03_231')
def func_03_231():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_29E',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '从工房船回来之后，\n',
            '菲前辈还是没什么精神啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '难、难道说，\n',
            '她和原男友的关系又有变化了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_540')

    def _loc_29E(): pass

    label('loc_29E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_4C6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_338',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '再见了，\n',
            '你们也要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为库存已经所剩不多了，\n',
            '所以你们一定要送到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼…………\n',
            '我也要打起精神来，\n',
            '好好工作才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C3')

    def _loc_338(): pass

    label('loc_338')

    If(
        (
            (Expr.Eval, "OP_29(0x0029, 0x01, 0x0008)"),
            (Expr.Eval, "OP_29(0x0029, 0x01, 0x0010)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_353',
    )

    Call(1, 0x0002)

    Jump('loc_4C3')

    def _loc_353(): pass

    label('loc_353')

    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_40A',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才在工作的时候\n',
            '又被菲前辈骂了一顿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '肯定是因为前辈\n',
            '认为我是个没用的家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜呜，\n',
            '好不容易前辈和男友分手，\n',
            '我以为会有机会的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉～我真是没用啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C3')

    def _loc_40A(): pass

    label('loc_40A')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '唉～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚才在工作的时候\n',
            '又被菲前辈骂了一顿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '肯定是因为前辈\n',
            '认为我是个没用的家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呜呜，\n',
            '好不容易前辈和男友分手，\n',
            '我以为会有机会的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉～我真是没用啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C3(): pass

    label('loc_4C3')

    Jump('loc_540')

    def _loc_4C6(): pass

    label('loc_4C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_540',
    )

    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '唔，\n',
            '加上这罐的话总共就有８罐了………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，和清单上的一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么，\n',
            '接下来就交给工场那边检查吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_540(): pass

    label('loc_540')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x544
@scena.Code('func_04_544')
def func_04_544():
    ClearMapFlags(0x00000800)
    OP_1B(0x00, 0x00, 0xFFFF)

    Return()

# id: 0x0005 offset: 0x54F
@scena.Code('func_05_54F')
def func_05_54F():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(600200, 0, -54800, 0)
    OP_6C(0, 0)
    SetChrPos(0x0101, 596400, 0, -54800, 90)
    SetChrPos(0x0102, 595000, 0, -53500, 90)
    SetChrPos(0x0107, 595000, 0, -55200, 90)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010070485V#004F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_05CD')
    def lambda_05CD():
        ChrWalkTo(0x00FE, 616400, 0, -54800, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_05CD)

    Sleep(200)

    @scena.Lambda('lambda_05ED')
    def lambda_05ED():
        ChrWalkTo(0x00FE, 615000, 0, -54400, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_05ED)

    Sleep(500)

    @scena.Lambda('lambda_060D')
    def lambda_060D():
        ChrWalkTo(0x00FE, 615100, 0, -55900, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_060D)

    @scena.Lambda('lambda_0628')
    def lambda_0628():
        CameraMove(618500, 0, -53800, 3500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0628)

    @scena.Lambda('lambda_0640')
    def lambda_0640():
        OP_6C(45000, 3300)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0640)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010070486V#501F到隧道的尽头了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070487V这么说……\n',
            '这里就是蔡斯市的入口了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0107, 0x0001)
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070070488V#060F嗯，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070489V准确地来说，\n',
            '是到了中央工房的地下区域了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0704')
    def lambda_0704():
        CameraMove(615770, -90, -54810, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0704)

    SetChrDirection(0x0101, 270, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010070490V#006F中央工房是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0102, 135, 400)

    ChrTalk(
        0x0102,
        (
            '#0020070491V#015F『中央工房』——\n',
            '顾名思义就是工房都市蔡斯\n',
            '引以为傲的导力器技术殿堂对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020070492V#010F以前就听说这里是\n',
            '一座极为庞大的建筑物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070493V#061F那当然了～\n',
            '而且这里不是一般的大呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070494V很多客人第一次来这里\n',
            '都免不得会迷路一番的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070495V#004F哇……\n',
            '那可真是太大了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010070496V#007F看来我开始担心\n',
            '能不能平安到达游击士协会了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070070497V#560F没问题的。\n',
            '上了一楼就有通往城镇的入口呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070070498V我来为姐姐你们带路吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010070499V#001F谢谢，那就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020070500V#010F那我们进去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x94E
@scena.Code('func_06_94E')
def func_06_94E():
    EventBegin(0x00)
    CameraMove(619220, 250, -53680, 0)
    SetChrPos(0x0106, 618640, 0, -54820, 270)
    SetChrPos(0x0101, 619650, 750, -54420, 270)
    SetChrPos(0x0102, 619020, 250, -55970, 270)
    SetChrPos(0x0107, 620220, 1000, -55430, 270)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010080919V#002F那些家伙们，\n',
            '是往这边逃走了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050080920V#552F不，应该不是……\n',
            '没有看到新的脚印。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080921V#012F而且也没有事先作伪装的时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080922V#065F也就是说……他们到一楼去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080923V#005F嗯，赶快！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearMapFlags(0x10000000)
    NewScene('ED6_DT01/T3111._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0xA9C
@scena.Code('func_07_A9C')
def func_07_A9C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 4, 0x604)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B32',
    )

    EventBegin(0x01)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020101078V#010F首先我们要去飞艇坪\n',
            '把搭乘手续取消掉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101079V如果不取消的话，\n',
            '售票员会很困扰的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_1896')

    def _loc_B32(): pass

    label('loc_B32')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 3, 0x603)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C55',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BD4',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020101073V#010F这边是卡鲁迪亚隧道啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101074V为了不耽误乘坐定期船，\n',
            '还是不要跑得太远吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010101075V#000F啊，对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C37')

    def _loc_BD4(): pass

    label('loc_BD4')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020101076V#010F这边是卡鲁迪亚隧道啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020101077V为了不耽误乘坐定期船，\n',
            '还是不要跑得太远吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C37(): pass

    label('loc_C37')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_1896')

    def _loc_C55(): pass

    label('loc_C55')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 2, 0x55A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E5A',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D84',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D20',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020091521V#017F艾丝蒂尔，你要去哪儿？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091522V去雷斯顿要塞的话，\n',
            '要从城东门出去啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010091523V#004F啊？\n',
            '是、是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091524V#018F……真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D81')

    def _loc_D20(): pass

    label('loc_D20')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020091525V#017F去雷斯顿要塞的话，\n',
            '要从城东门出去才行啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091526V你刚才不是记下来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D81(): pass

    label('loc_D81')

    Jump('loc_E3C')

    def _loc_D84(): pass

    label('loc_D84')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DE6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0102,
        (
            '#0020091527V#012F这边是卡鲁迪亚隧道啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091528V去雷斯顿要塞的话，\n',
            '要从城东门出去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E3C')

    def _loc_DE6(): pass

    label('loc_DE6')

    ChrTalk(
        0x0102,
        (
            '#0020091529V#012F这边是卡鲁迪亚隧道啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091530V去雷斯顿要塞的话，\n',
            '要从城东门出去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E3C(): pass

    label('loc_E3C')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_1896')

    def _loc_E5A(): pass

    label('loc_E5A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 2, 0x55A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1089',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F66',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F0C',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010091496V#000F啊，\n',
            '总之现在要先回协会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091497V在没有情报的情况下\n',
            '是不能随便行动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020091498V#010F是啊。\n',
            '赶快走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F63')

    def _loc_F0C(): pass

    label('loc_F0C')

    ChrTalk(
        0x0101,
        (
            '#0010091499V#000F总之，\n',
            '现在要先回协会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091500V在没有情报的情况下\n',
            '是不能随便行动的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F63(): pass

    label('loc_F63')

    Jump('loc_106B')

    def _loc_F66(): pass

    label('loc_F66')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1001',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020091501V#010F总之现在先回协会\n',
            '听听雾香小姐怎么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091502V说不定能发现什么有价值的线索呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010091503V#000F嗯，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_106B')

    def _loc_1001(): pass

    label('loc_1001')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020091504V#010F总之现在先回协会\n',
            '听听雾香小姐怎么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091505V说不定能发现什么有价值的线索呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_106B(): pass

    label('loc_106B')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_1896')

    def _loc_1089(): pass

    label('loc_1089')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 1, 0x551)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 2, 0x552)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_12E2',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_115C',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020091506V#012F艾丝蒂尔，等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091507V首先还是回协会\n',
            '调查一下以前的记录吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091508V关于『塞姆里亚苔藓』的情报\n',
            '我们还知道得太少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010091509V#002F啊，说得也对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12C4')

    def _loc_115C(): pass

    label('loc_115C')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1225',
    )

    ChrTurnDirection(0x0102, 0x0107, 400)

    ChrTalk(
        0x0102,
        (
            '#0020091510V#012F提妲，先等一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091511V首先还是回协会\n',
            '调查一下以前的记录吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091512V关于『塞姆里亚苔藓』的情报\n',
            '我们还知道得太少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0102, 400)

    ChrTalk(
        0x0107,
        (
            '#0070091513V#060F啊……嗯，我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12C4')

    def _loc_1225(): pass

    label('loc_1225')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12C4',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1247',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    Jump('loc_124E')

    def _loc_1247(): pass

    label('loc_1247')

    ChrTurnDirection(0x0102, 0x0000, 400)

    def _loc_124E(): pass

    label('loc_124E')

    ChrTalk(
        0x0102,
        (
            '#0020091514V#012F教区长也说了，\n',
            '首先还是回协会\n',
            '调查一下以前的记录吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091515V关于『塞姆里亚苔藓』\n',
            '要多收集一些情报。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12C4(): pass

    label('loc_12C4')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_1896')

    def _loc_12E2(): pass

    label('loc_12E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 1, 0x551)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1464',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_133E',
    )

    ChrTalk(
        0x0101,
        (
            '#0010091516V#002F（啊，这边是隧道……\n',
            '　现在要赶快去礼拜堂。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1446')

    def _loc_133E(): pass

    label('loc_133E')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1388',
    )

    ChrTalk(
        0x0102,
        (
            '#0020091517V#012F（这边是隧道……\n',
            '　现在要赶快去礼拜堂。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1446')

    def _loc_1388(): pass

    label('loc_1388')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13D6',
    )

    ChrTalk(
        0x0107,
        (
            '#0070091518V#062F（啊，这边是出口……\n',
            '　要赶快去礼拜堂才行。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1446')

    def _loc_13D6(): pass

    label('loc_13D6')

    ChrTalk(
        0x0108,
        (
            '#0080091519V#070F（唔，这边是隧道的入口吗。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080091520V（虽然是个不错的修行场所，\n',
            '　不过现在要紧的是去礼拜堂。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1446(): pass

    label('loc_1446')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_1896')

    def _loc_1464(): pass

    label('loc_1464')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 0, 0x538)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1591',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_151B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14D6',
    )

    ChrTalk(
        0x0106,
        (
            '#0050091491V#050F嘁……\n',
            '现在再追也不会有线索的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091492V总之先回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1518')

    def _loc_14D6(): pass

    label('loc_14D6')

    ChrTurnDirection(0x0106, 0x0000, 400)

    ChrTalk(
        0x0106,
        (
            '#0050091493V#050F喂，你们去哪儿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091494V赶快回协会去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1518(): pass

    label('loc_1518')

    Jump('loc_1573')

    def _loc_151B(): pass

    label('loc_151B')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1531',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_1538')

    def _loc_1531(): pass

    label('loc_1531')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_1538(): pass

    label('loc_1538')

    ChrTalk(
        0x0106,
        (
            '#0050091495V#050F往那边追也不会有线索的。\n',
            '总之先回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1573(): pass

    label('loc_1573')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_1896')

    def _loc_1591(): pass

    label('loc_1591')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_16DF',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_165F',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0102,
        (
            '#0020091483V#010F博士要的东西还没有送过去呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091484V……委托的事情，\n',
            '你有没有好好记下来啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010091485V#009F真、真讨厌～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091486V这不是清清楚楚地记下来了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16C1')

    def _loc_165F(): pass

    label('loc_165F')

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020091487V#010F博士要的东西还没有送过去呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091488V总之现在要帮忙工作机械的改造。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16C1(): pass

    label('loc_16C1')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_1896')

    def _loc_16DF(): pass

    label('loc_16DF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1773',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1703',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    Jump('loc_170A')

    def _loc_1703(): pass

    label('loc_1703')

    ChrTurnDirection(0x0102, 0x0000, 400)

    def _loc_170A(): pass

    label('loc_170A')

    ChrTalk(
        0x0102,
        (
            '#0020091489V#010F这边是卡鲁迪亚隧道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091490V现在我们还是快去博士那里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Jump('loc_1896')

    def _loc_1773(): pass

    label('loc_1773')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1896',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17CD',
    )

    ChrTalk(
        0x0101,
        (
            '#0010091479V#006F（这边是回隧道的路。\n',
            '　现在要先去提妲家。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_187B')

    def _loc_17CD(): pass

    label('loc_17CD')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1819',
    )

    ChrTalk(
        0x0102,
        (
            '#0020091480V#010F（这边是卡鲁迪亚隧道。\n',
            '　先到提妲家去吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_187B')

    def _loc_1819(): pass

    label('loc_1819')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_187B',
    )

    ChrTalk(
        0x0107,
        (
            '#0070091481V#065F（不行……\n',
            '　这边是卡鲁迪亚隧道。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070091482V（先招待他们去我家吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_187B(): pass

    label('loc_187B')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_1896(): pass

    label('loc_1896')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
