import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0013_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0013_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/E0013_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1A3E
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
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    EventBegin(0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x72),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_289',
    )

    SetChrPos(0x0101, 87360, 0, -6520, 0)
    SetChrPos(0x0103, 86500, 100, -7110, 0)
    SetChrPos(0x00F8, 87360, 100, -7640, 0)
    SetChrPos(0x00F9, 86500, 100, -8410, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_129',
    )

    SetChrPos(0x00F9, 87360, 100, -7640, 0)
    SetChrPos(0x00F8, 86500, 100, -8410, 0)

    def _loc_129(): pass

    label('loc_129')

    OP_6D(87000, 0, 4940, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_0175')
    def lambda_0175():
        OP_6D(87000, 0, -2480, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0175)

    Sleep(400)

    @scena.Lambda('lambda_0192')
    def lambda_0192():
        OP_8E(0x00FE, 87360, 0, -1880, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0192)

    Sleep(1000)

    @scena.Lambda('lambda_01B2')
    def lambda_01B2():
        OP_8E(0x00FE, 86500, 0, -2970, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0000, lambda_01B2)

    Sleep(600)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F7',
    )

    @scena.Lambda('lambda_01DF')
    def lambda_01DF():
        OP_8E(0x00FE, 86500, 0, -4440, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_01DF)

    Jump('loc_212')

    def _loc_1F7(): pass

    label('loc_1F7')

    @scena.Lambda('lambda_01FD')
    def lambda_01FD():
        OP_8E(0x00FE, 87360, 0, -3550, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_01FD)

    def _loc_212(): pass

    label('loc_212')

    Sleep(200)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_242',
    )

    @scena.Lambda('lambda_022A')
    def lambda_022A():
        OP_8E(0x00FE, 87360, 0, -3550, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_022A)

    Jump('loc_25D')

    def _loc_242(): pass

    label('loc_242')

    @scena.Lambda('lambda_0248')
    def lambda_0248():
        OP_8E(0x00FE, 86500, 0, -4440, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_0248)

    def _loc_25D(): pass

    label('loc_25D')

    WaitForThreadExit(0x0101, 0x0000)
    Sleep(400)

    OP_8C(0x0101, 90, 400)
    Sleep(400)

    OP_8C(0x0101, 315, 400)
    Sleep(800)

    OP_8C(0x0101, 0, 400)

    Jump('loc_3FE')

    def _loc_289(): pass

    label('loc_289')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x71),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34B',
    )

    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0103, 0x0080)
    SetChrFlags(0x00F8, 0x0080)
    SetChrFlags(0x00F9, 0x0080)
    OP_6D(96680, 0, 3000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(312, 0)
    OP_6F(0x0002, 59)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_02FC')
    def lambda_02FC():
        OP_6D(87190, 0, 2230, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_02FC)

    Sleep(1500)

    Sleep(400)

    CreateThread(0x0101, 0x00, 0x01, 0x0001)
    Sleep(1000)

    CreateThread(0x0103, 0x00, 0x01, 0x0002)
    Sleep(1000)

    CreateThread(0x00F8, 0x00, 0x01, 0x0003)
    Sleep(600)

    CreateThread(0x00F9, 0x00, 0x01, 0x0004)
    WaitForThreadExit(0x0101, 0x0000)

    Jump('loc_3FE')

    def _loc_34B(): pass

    label('loc_34B')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x70),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3FE',
    )

    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0103, 0x0080)
    SetChrFlags(0x00F8, 0x0080)
    SetChrFlags(0x00F9, 0x0080)
    OP_6D(82680, 0, 3000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(312, 0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_03B7')
    def lambda_03B7():
        OP_6D(87180, 0, 3000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_03B7)

    Sleep(3000)

    CreateThread(0x0101, 0x00, 0x01, 0x0005)
    Sleep(1000)

    CreateThread(0x0103, 0x00, 0x01, 0x0006)
    Sleep(1000)

    CreateThread(0x00F8, 0x00, 0x01, 0x0007)
    Sleep(600)

    CreateThread(0x00F9, 0x00, 0x01, 0x0008)
    WaitForThreadExit(0x0101, 0x0000)

    def _loc_3FE(): pass

    label('loc_3FE')

    ChrTalk(
        0x0101,
        (
            '#0010461266V#1004F哇……\n',
            '真是好暗啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_468',
    )

    ChrTalk(
        0x0107,
        (
            '#0070461267V#060F嗯……\n',
            '导力灯也熄灭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_536')

    def _loc_468(): pass

    label('loc_468')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4AB',
    )

    ChrTalk(
        0x0105,
        (
            '#0060461268V#040F嗯，灯光也都\n',
            '完全熄灭了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_536')

    def _loc_4AB(): pass

    label('loc_4AB')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4F8',
    )

    ChrTalk(
        0x0108,
        (
            '#0080461269V#070F嗯，没有导力灯，\n',
            '而且今晚也没有月光。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_536')

    def _loc_4F8(): pass

    label('loc_4F8')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_536',
    )

    ChrTalk(
        0x0104,
        (
            '#0040461270V#030F嗯，灯光也都\n',
            '完全熄灭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_536(): pass

    label('loc_536')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5B4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050461271V#552F不过，这无人的\n',
            '座位给人感觉真不舒服。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050461272V现在好像都还能\n',
            '听见说话的声音一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6C1')

    def _loc_5B4(): pass

    label('loc_5B4')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_605',
    )

    ChrTalk(
        0x0104,
        (
            '#0040461273V#030F不过，现在好像都还能\n',
            '听见乘客的声音一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6C1')

    def _loc_605(): pass

    label('loc_605')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_656',
    )

    ChrTalk(
        0x0108,
        (
            '#0080461274V#070F不过，现在好像都还能\n',
            '听见乘客的声音一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6C1')

    def _loc_656(): pass

    label('loc_656')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6C1',
    )

    ChrTalk(
        0x0105,
        (
            '#0060461275V#040F不过，白天的喧闹\n',
            '好像还残留着呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060461276V让人回忆起\n',
            '夜间的校舍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6C1(): pass

    label('loc_6C1')

    ChrTalk(
        0x0103,
        (
            '#0030461277V#026F嗯，让人有点不舒服。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030461278V感觉会有什么鬼怪跳出来似的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    OP_9E(0x0101, 0x0000000A, 0x00000000, 0x000001F4, 0x00000BB8)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010461279V#1019F唔…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_7A8',
    )

    ChrTalk(
        0x0103,
        (
            '#0030461280V#023F咦，你现在还怕\n',
            '那种事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7DC')

    def _loc_7A8(): pass

    label('loc_7A8')

    ChrTalk(
        0x0103,
        (
            '#0030461281V#023F咦，你还没克服\n',
            '幽灵恐惧症吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7DC(): pass

    label('loc_7DC')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x72),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7F2',
    )

    OP_8C(0x0101, 180, 400)

    Jump('loc_7F9')

    def _loc_7F2(): pass

    label('loc_7F2')

    OP_8C(0x0101, 0, 400)

    def _loc_7F9(): pass

    label('loc_7F9')

    ChrTalk(
        0x0101,
        (
            '#0010461282V#1022F啊，先别说这个了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010461283V#1005F好了，赶快找到猫，\n',
            '然后从这里撤退吧。',
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
        'loc_89F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080461284V#070F说得也是……\n',
            '那么就开工吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_976')

    def _loc_89F(): pass

    label('loc_89F')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8E0',
    )

    ChrTalk(
        0x0106,
        (
            '#0050461285V#050F嗯，是啊。\n',
            '那么就开工吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_976')

    def _loc_8E0(): pass

    label('loc_8E0')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_93F',
    )

    ChrTalk(
        0x0104,
        (
            '#0040461286V#030F那么，赶快开始吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040461287V维修员也在\n',
            '等着我们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_976')

    def _loc_93F(): pass

    label('loc_93F')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_976',
    )

    ChrTalk(
        0x0105,
        (
            '#0060461288V#040F嗯，那么就开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_976(): pass

    label('loc_976')

    OP_28(0x0074, 0x01, 0x4000)
    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0x97F
@scena.Code('Init')
def Init():
    SetChrPos(0x00FE, 90790, 100, 2860, 270)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 87970, 0, 2860, 2000, 0x00)
    OP_8E(0x00FE, 86990, 0, 1830, 2000, 0x00)
    OP_8C(0x00FE, 180, 400)
    Sleep(1000)

    Sleep(400)

    OP_8C(0x0101, 270, 400)
    Sleep(800)

    OP_8C(0x0101, 135, 400)
    Sleep(800)

    OP_8C(0x0101, 180, 400)
    Sleep(1000)

    Return()

# id: 0x0002 offset: 0x9F3
@scena.Code('ReInit')
def ReInit():
    SetChrPos(0x00FE, 90790, 100, 2860, 270)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 86300, 0, 2860, 2000, 0x00)
    OP_8C(0x00FE, 180, 400)

    Return()

# id: 0x0003 offset: 0xA25
@scena.Code('func_03_A25')
def func_03_A25():
    SetChrPos(0x00FE, 90790, 100, 2860, 270)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 87760, 0, 2860, 2000, 0x00)
    OP_8C(0x00FE, 180, 400)

    Return()

# id: 0x0004 offset: 0xA57
@scena.Code('func_04_A57')
def func_04_A57():
    SetChrPos(0x00FE, 90790, 100, 2860, 270)
    ClearChrFlags(0x00FE, 0x0080)
    OP_8E(0x00FE, 89140, 0, 2860, 2000, 0x00)
    OP_8C(0x00FE, 90, 400)
    OP_72(0x0002, 0x0800)
    OP_70(0x0002, 0x00000000)
    OP_22(0x0007, 0x00, 0x64)
    OP_73(0x0002)
    Sleep(1000)

    OP_71(0x0002, 0x0800)
    OP_8C(0x00FE, 180, 400)

    Return()

# id: 0x0005 offset: 0xAAE
@scena.Code('func_05_AAE')
def func_05_AAE():
    SetChrPos(0x00FE, 82560, 100, 2860, 270)
    ClearChrFlags(0x00FE, 0x0080)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    @scena.Lambda('lambda_0AD5')
    def lambda_0AD5():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0AD5)

    OP_8E(0x00FE, 85970, 0, 2860, 2000, 0x00)
    OP_8E(0x00FE, 86990, 0, 1830, 2000, 0x00)
    OP_8C(0x00FE, 180, 400)
    Sleep(1000)

    Sleep(400)

    OP_8C(0x0101, 270, 400)
    Sleep(800)

    OP_8C(0x0101, 135, 400)
    Sleep(800)

    OP_8C(0x0101, 180, 400)
    Sleep(1000)

    Return()

# id: 0x0006 offset: 0xB3F
@scena.Code('func_06_B3F')
def func_06_B3F():
    SetChrPos(0x00FE, 82560, 100, 2860, 270)
    ClearChrFlags(0x00FE, 0x0080)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    @scena.Lambda('lambda_0B66')
    def lambda_0B66():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0B66)

    OP_8E(0x00FE, 87700, 0, 2860, 2000, 0x00)
    OP_8C(0x00FE, 180, 400)

    Return()

# id: 0x0007 offset: 0xB8E
@scena.Code('func_07_B8E')
def func_07_B8E():
    SetChrPos(0x00FE, 82560, 100, 2860, 270)
    ClearChrFlags(0x00FE, 0x0080)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    @scena.Lambda('lambda_0BB5')
    def lambda_0BB5():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0BB5)

    OP_8E(0x00FE, 86260, 0, 2860, 2000, 0x00)
    OP_8C(0x00FE, 180, 400)

    Return()

# id: 0x0008 offset: 0xBDD
@scena.Code('func_08_BDD')
def func_08_BDD():
    SetChrPos(0x00FE, 82560, 100, 2860, 270)
    ClearChrFlags(0x00FE, 0x0080)
    OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    @scena.Lambda('lambda_0C04')
    def lambda_0C04():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000190)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0C04)

    OP_8E(0x00FE, 84620, 0, 2860, 2000, 0x00)
    OP_8C(0x00FE, 270, 400)
    OP_22(0x0007, 0x00, 0x64)
    Sleep(1000)

    OP_8C(0x00FE, 180, 400)

    Return()

# id: 0x0009 offset: 0xC3D
@scena.Code('func_09_C3D')
def func_09_C3D():
    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x00, 0x08)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0074, 0x00, 0x10)"),
            Expr.Or,
            (Expr.Eval, "OP_29(0x0074, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_C57',
    )

    Return()

    def _loc_C57(): pass

    label('loc_C57')

    EventBegin(0x00)
    OP_26(348)
    Fade(1000)
    OP_6D(30000, 0, 7620, 0)
    OP_67(0, 10620, -10000, 0)
    SetChrPos(0x0101, 30000, 0, 5860, 0)
    SetChrPos(0x00F7, 29320, 0, 4760, 0)
    SetChrPos(0x00F8, 30680, 0, 4760, 0)
    SetChrPos(0x00F9, 30000, 0, 3770, 0)
    OP_6D(30270, 0, 6020, 0)
    OP_67(0, 10620, -10000, 0)
    OP_6B(2160, 0)
    OP_6C(59000, 0)
    OP_6E(262, 0)
    OP_0D()
    SetChrPos(0x0008, 27420, 400, 10420, 90)
    OP_22(0x0192, 0x00, 0x64)

    NpcTalk(
        0x0008,
        '鸣叫声',
        (
            '#1100461289V#6P喵～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010461290V#1004F#2P啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DB7',
    )

    ChrTalk(
        0x0107,
        (
            '#0070461291V#064F刚、刚才的叫声是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E60')

    def _loc_DB7(): pass

    label('loc_DB7')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DED',
    )

    ChrTalk(
        0x0105,
        (
            '#0060461292V#044F刚才的叫声……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E60')

    def _loc_DED(): pass

    label('loc_DED')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E29',
    )

    ChrTalk(
        0x0104,
        (
            '#0040461293V#033F哎呀，刚才的叫声……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E60')

    def _loc_E29(): pass

    label('loc_E29')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E60',
    )

    ChrTalk(
        0x0106,
        (
            '#0050461294V#052F刚才有叫声传过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E60(): pass

    label('loc_E60')

    @scena.Lambda('lambda_0E66')
    def lambda_0E66():
        OP_6D(30000, 0, 7620, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0E66)

    @scena.Lambda('lambda_0E7E')
    def lambda_0E7E():
        OP_6C(40000, 2000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0003, lambda_0E7E)

    @scena.Lambda('lambda_0E8E')
    def lambda_0E8E():
        OP_67(0, 10620, -10000, 2000)

        ExitThread()

    DispatchAsync(0x00F8, 0x0003, lambda_0E8E)

    CreateThread(0x0008, 0x00, 0x01, 0x000A)

    @scena.Lambda('lambda_0EAD')
    def lambda_0EAD():
        OP_94(0x01, 0x0101, 0x0000, 0x000003E8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0EAD)

    Sleep(150)

    @scena.Lambda('lambda_0EC8')
    def lambda_0EC8():
        OP_94(0x01, 0x00F7, 0x0000, 0x000003E8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0EC8)

    Sleep(150)

    @scena.Lambda('lambda_0EE3')
    def lambda_0EE3():
        OP_94(0x01, 0x00F8, 0x0000, 0x000003E8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0EE3)

    Sleep(150)

    @scena.Lambda('lambda_0EFE')
    def lambda_0EFE():
        OP_94(0x01, 0x00F9, 0x0000, 0x000003E8, 0x000003E8, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0EFE)

    WaitForThreadExit(0x0008, 0x0000)
    OP_22(0x0192, 0x00, 0x64)

    ChrTalk(
        0x0008,
        (
            '#1100461295V喵～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x0101, 2)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_29(0x0009, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_F4D',
    )

    OP_A2(0x0001)

    def _loc_F4D(): pass

    label('loc_F4D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FCD',
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
        100,
        0,
        (
            TXT(0x00, '【◇完成过【小猫的搜索】】\n'),
            TXT(0x01, '【◇没完成过【小猫的搜索】】\n'),
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
        (0x00000000, 'loc_FC1'),
        (0x00000001, 'loc_FC7'),
        (-1, 'loc_FCD'),
    )

    def _loc_FC1(): pass

    label('loc_FC1')

    OP_A2(0x0001)

    Jump('loc_FCD')

    def _loc_FC7(): pass

    label('loc_FC7')

    OP_A3(0x0001)

    Jump('loc_FCD')

    def _loc_FCD(): pass

    label('loc_FCD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1026',
    )

    ChrTalk(
        0x0101,
        (
            '#0010461296V#1016F#2P找到你了，安莉尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010461297V你还是一样地调皮呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1070')

    def _loc_1026(): pass

    label('loc_1026')

    ChrTalk(
        0x0101,
        (
            '#0010461298V#1001F#2P终于找到了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010461299V她大概就是\n',
            '安莉尔吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1070(): pass

    label('loc_1070')

    ChrTalk(
        0x0103,
        (
            '#0030461300V#020F#3P和委托人描述的一样，\n',
            '是褐色的毛色……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030461301V应该是这只猫了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_110E',
    )

    ChrTalk(
        0x0105,
        (
            '#0060461302V#048F太好了……\n',
            '顺利找到了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_120B')

    def _loc_110E(): pass

    label('loc_110E')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1153',
    )

    ChrTalk(
        0x0107,
        (
            '#0070461303V#561F太、太好了……\n',
            '顺利找到了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_120B')

    def _loc_1153(): pass

    label('loc_1153')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11AD',
    )

    ChrTalk(
        0x0104,
        (
            '#0040461304V#030F看来确实如此呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040461305V她能没事真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_120B')

    def _loc_11AD(): pass

    label('loc_11AD')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_120B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050461306V#051F看来的确是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050461307V真是的……\n',
            '终于找到了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_120B(): pass

    label('loc_120B')

    ChrTalk(
        0x0101,
        (
            '#0010461308V#1015F#2P都是你害我们\n',
            '走了那么多路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010461309V你躲在这里\n',
            '到底要干什么啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 0, 400)
    OP_22(0x0192, 0x00, 0x64)

    ChrTalk(
        0x0008,
        (
            '#1100461310V喵～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0009, 27420, 400, 10420, 90)
    SetChrPos(0x000A, 27420, 400, 10420, 90)
    SetChrPos(0x000B, 27420, 400, 10420, 90)
    OP_22(0x015C, 0x00, 0x64)

    ChrTalk(
        0x0009,
        (
            '#3450461311V咪～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x015C, 0x00, 0x64)

    ChrTalk(
        0x000A,
        (
            '#3450461312V咪咪～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461313V#1011F#2P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1320')
    def lambda_1320():
        OP_6D(30000, 0, 7000, 2000)

        ExitThread()

    DispatchAsync(0x00F6, 0x0003, lambda_1320)

    @scena.Lambda('lambda_1338')
    def lambda_1338():
        OP_6B(2350, 2000)

        ExitThread()

    DispatchAsync(0x00F9, 0x0003, lambda_1338)

    @scena.Lambda('lambda_1348')
    def lambda_1348():
        OP_6C(0, 2000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0003, lambda_1348)

    @scena.Lambda('lambda_1358')
    def lambda_1358():
        OP_67(0, 10680, -10000, 2000)

        ExitThread()

    DispatchAsync(0x00F8, 0x0003, lambda_1358)

    CreateThread(0x0009, 0x00, 0x01, 0x000B)
    CreateThread(0x000A, 0x00, 0x01, 0x000C)
    CreateThread(0x000B, 0x00, 0x01, 0x000D)
    Sleep(3000)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13D9',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_1417')

    def _loc_13D9(): pass

    label('loc_13D9')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1400',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_1417')

    def _loc_1400(): pass

    label('loc_1400')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_1417(): pass

    label('loc_1417')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_143E',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_147C')

    def _loc_143E(): pass

    label('loc_143E')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1465',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_147C')

    def _loc_1465(): pass

    label('loc_1465')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_147C(): pass

    label('loc_147C')

    ChrTalk(
        0x0101,
        (
            '#0010461314V#1004F#1P啊啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14D7',
    )

    ChrTalk(
        0x0107,
        (
            '#0070461315V#065F小、小猫……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1576')

    def _loc_14D7(): pass

    label('loc_14D7')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_150B',
    )

    ChrTalk(
        0x0105,
        (
            '#0060461316V#044F小猫……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1576')

    def _loc_150B(): pass

    label('loc_150B')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1545',
    )

    ChrTalk(
        0x0104,
        (
            '#0040461317V#031F哟，这可不得了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1576')

    def _loc_1545(): pass

    label('loc_1545')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1576',
    )

    ChrTalk(
        0x0106,
        (
            '#0050461318V#052F真让人吃惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1576(): pass

    label('loc_1576')

    WaitForThreadExit(0x000B, 0x0000)

    ChrTalk(
        0x0103,
        (
            '#0030461319V#021F呵呵，好可爱㈱\n',
            '好像是刚出生的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010461320V#1015F那、那么……\n',
            '就是说是在这里出生的吗？',
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
        'loc_1682',
    )

    ChrTalk(
        0x0108,
        (
            '#0080461321V#070F嗯，有可能是为了\n',
            '产仔才潜入了这里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080461322V虽然说是为了找个安全的地方，\n',
            '不过母亲的伟大真令人佩服……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1808')

    def _loc_1682(): pass

    label('loc_1682')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1706',
    )

    ChrTalk(
        0x0106,
        (
            '#0050461323V#051F嗯，有可能是为了\n',
            '产仔才来这里的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050461324V不知道是不是动物的本能，\n',
            '不过母亲真是伟大啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1808')

    def _loc_1706(): pass

    label('loc_1706')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1784',
    )

    ChrTalk(
        0x0105,
        (
            '#0060461325V#047F嗯，有可能是为了\n',
            '产仔才潜入了这里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060461326V为了寻找对孩子们来说\n',
            '最安全的地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1808')

    def _loc_1784(): pass

    label('loc_1784')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1808',
    )

    ChrTalk(
        0x0107,
        (
            '#0070461327V#060F有可能是为了\n',
            '产仔才潜入了这里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070461328V#067F嘿嘿，这么这么小却又\n',
            '是个非常伟大的妈妈呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1808(): pass

    label('loc_1808')

    ChrTalk(
        0x0101,
        (
            '#0010461329V#1007F#2P呼，不过也没必要\n',
            '跑到飞船上吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010461330V#1000F好了，算了。\n',
            '现在得回去报告。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030461331V#021F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030461332V想必阿姨也会\n',
            '吓一跳吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T0136._SN', 104, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x18D5
@scena.Code('func_0A_18D5')
def func_0A_18D5():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0004)
    OP_8E(0x00FE, 29260, 200, 10420, 3000, 0x00)
    OP_8E(0x00FE, 30000, 0, 9420, 3000, 0x00)
    OP_8E(0x00FE, 30000, 0, 8020, 1000, 0x00)
    OP_8C(0x00FE, 180, 400)
    ClearChrFlags(0x00FE, 0x0004)

    Return()

# id: 0x000B offset: 0x1928
@scena.Code('func_0B_1928')
def func_0B_1928():
    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0004)
    OP_8E(0x00FE, 29260, 200, 10420, 1000, 0x00)
    OP_8E(0x00FE, 30330, 0, 8930, 1000, 0x00)
    CreateThread(0x0009, 0x02, 0x00, 0x0002)
    ChrTurnDirection(0x00FE, 0x0008, 400)
    ClearChrFlags(0x00FE, 0x0004)
    OP_A6(0x0000)
    CreateThread(0x0009, 0x01, 0x00, 0x0003)

    Return()

# id: 0x000C offset: 0x1978
@scena.Code('func_0C_1978')
def func_0C_1978():
    Sleep(1500)

    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0004)
    OP_8E(0x00FE, 29260, 200, 10420, 1000, 0x00)
    OP_8E(0x00FE, 29670, 0, 9180, 1000, 0x00)
    CreateThread(0x000A, 0x02, 0x00, 0x0002)
    ChrTurnDirection(0x00FE, 0x0008, 400)
    ClearChrFlags(0x00FE, 0x0004)
    OP_A6(0x0000)
    CreateThread(0x000A, 0x01, 0x00, 0x0003)

    Return()

# id: 0x000D offset: 0x19CD
@scena.Code('func_0D_19CD')
def func_0D_19CD():
    Sleep(3000)

    ClearChrFlags(0x00FE, 0x0080)
    SetChrFlags(0x00FE, 0x0004)
    OP_8E(0x00FE, 29260, 200, 10420, 1000, 0x00)
    OP_8E(0x00FE, 29980, 0, 9720, 1000, 0x00)
    CreateThread(0x000B, 0x02, 0x00, 0x0002)
    ChrTurnDirection(0x00FE, 0x0008, 400)
    ClearChrFlags(0x00FE, 0x0004)
    OP_A2(0x0000)
    CreateThread(0x000B, 0x01, 0x00, 0x0003)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
