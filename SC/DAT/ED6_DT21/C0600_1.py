import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0600_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0600_1 ._SN')

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/C0600_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x10D2
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
    SetChrPos(0x0101, 0, 0, -6000, 0)
    SetChrPos(0x00F7, -1300, 0, -6990, 0)
    SetChrPos(0x00F8, -500, 0, -7670, 0)
    SetChrPos(0x00F9, 950, 0, -6790, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11D',
    )

    SetChrPos(0x00F9, -500, 0, -7670, 0)
    SetChrPos(0x00F8, 750, 0, -6790, 0)

    def _loc_11D(): pass

    label('loc_11D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14C',
    )

    SetChrPos(0x00F9, -500, 0, -7670, 0)
    SetChrPos(0x00F8, 750, 0, -6790, 0)

    def _loc_14C(): pass

    label('loc_14C')

    OP_6D(1300, 0, -3480, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010471197V#1011F#1P嗯……\n',
            '还以为有什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471198V#1015F放眼望去都是垃圾嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_01F8')
    def lambda_01F8():
        OP_90(0x00FE, 0, 0, 2000, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_01F8)

    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080471199V#076F#8A艾丝蒂尔、等等！',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2EB')

    def _loc_24C(): pass

    label('loc_24C')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_286',
    )

    ChrTalk(
        0x0106,
        (
            '#0050471200V#054F#8A艾丝蒂尔、等等！',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2EB')

    def _loc_286(): pass

    label('loc_286')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2C2',
    )

    ChrTalk(
        0x0104,
        (
            '#0040471201V#530F#8A艾丝蒂尔、等一下！',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2EB')

    def _loc_2C2(): pass

    label('loc_2C2')

    ChrTalk(
        0x0103,
        (
            '#0030471202V#024F#8A艾丝蒂尔、等等！',
            TxtCtl.Enter,
        ),
    )

    def _loc_2EB(): pass

    label('loc_2EB')

    Sleep(500)

    TerminateThread(0x0101, 0x01)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(200)

    @scena.Lambda('lambda_0316')
    def lambda_0316():
        OP_96(0x00FE, 0x00000000, 0x00000000, 0xFFFFE890, 0x000001F4, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0316)

    SetChrChipByIndex(0x0101, 9)
    SetChrSubChip(0x0101, 0)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x0008, 0, 0, 2200, 180)
    SetChrPos(0x0009, 2200, 0, 2200, 180)
    SetChrPos(0x000A, -2200, 0, 2200, 180)
    OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0009, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x000A, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_20(0x000007D0)
    OP_22(0x026D, 0x00, 0x64)
    OP_82(0x80, 0x02)
    OP_79(0x00, 0x0002)
    OP_7B()
    OP_77(0xE0, 0xE0, 0xE0, 0x00, 0x00000320)
    Sleep(1000)

    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7A(0x00, 0x0002)
    OP_7B()
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000190)
    Sleep(1000)

    OP_22(0x026D, 0x00, 0x64)
    OP_82(0x80, 0x02)
    OP_79(0x00, 0x0002)
    OP_7B()
    OP_77(0xC0, 0xC0, 0xC0, 0x00, 0x000007D0)
    Sleep(1000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFlags(0x0008, 0x0800)
    SetChrFlags(0x0009, 0x0800)
    SetChrFlags(0x000A, 0x0800)
    OP_22(0x028C, 0x00, 0x64)
    CreateThread(0x0008, 0x02, 0x01, 0x0002)

    @scena.Lambda('lambda_0448')
    def lambda_0448():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0448)

    Sleep(200)

    CreateThread(0x0009, 0x02, 0x01, 0x0002)

    @scena.Lambda('lambda_0466')
    def lambda_0466():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0466)

    Sleep(100)

    CreateThread(0x000A, 0x02, 0x01, 0x0002)

    @scena.Lambda('lambda_0484')
    def lambda_0484():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000007D0)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0484)

    Sleep(2000)

    OP_22(0x00D5, 0x00, 0x64)
    SetChrChipByIndex(0x0103, 3)

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4B2',
    )

    SetChrChipByIndex(0x0104, 4)

    def _loc_4B2(): pass

    label('loc_4B2')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4C5',
    )

    SetChrChipByIndex(0x0105, 5)

    def _loc_4C5(): pass

    label('loc_4C5')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4D8',
    )

    SetChrChipByIndex(0x0106, 6)

    def _loc_4D8(): pass

    label('loc_4D8')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4EB',
    )

    SetChrChipByIndex(0x0107, 7)

    def _loc_4EB(): pass

    label('loc_4EB')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4FE',
    )

    SetChrChipByIndex(0x0108, 8)

    def _loc_4FE(): pass

    label('loc_4FE')

    Sleep(200)

    OP_22(0x00D5, 0x00, 0x64)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(200)

    SetChrChipByIndex(0x0101, 2)
    OP_22(0x00D5, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0002)
    WaitForThreadExit(0x0009, 0x0002)
    WaitForThreadExit(0x000A, 0x0002)

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_56C',
    )

    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0107,
        (
            '#0070471203V#065F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_56C(): pass

    label('loc_56C')

    ChrTalk(
        0x0101,
        (
            '#0010471204V#1005F#1P这、这些家伙是什么啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030471205V#024F待会儿再问吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030471206V必须先击退才行！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_05F1')
    def lambda_05F1():
        OP_95(0x00FE, 0x00000000, 0x00000000, 0xFFFFF060, 0x00000258, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_05F1)

    @scena.Lambda('lambda_060F')
    def lambda_060F():
        OP_95(0x00FE, 0x00000000, 0x00000000, 0xFFFFF060, 0x00000258, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_060F)

    @scena.Lambda('lambda_062D')
    def lambda_062D():
        OP_95(0x00FE, 0x00000000, 0x00000000, 0xFFFFF060, 0x00000258, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_062D)

    SetChrChipByIndex(0x0008, 0)
    SetChrChipByIndex(0x0009, 0)
    SetChrChipByIndex(0x000A, 0)
    Sleep(200)

    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x00000CE4, 0x00000000, 0x00, 0x0000, 0xFF)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_687'),
        (-1, 'loc_68A'),
    )

    def _loc_687(): pass

    label('loc_687')

    OP_B4(0x00)

    Return()

    def _loc_68A(): pass

    label('loc_68A')

    FadeOut(0, 0, -1)
    OP_82(0x80, 0x00)
    EventBegin(0x00)
    OP_6D(1300, 0, -2480, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 0, 0, -3000, 0)
    SetChrPos(0x00F7, -1500, 0, -4190, 270)
    SetChrPos(0x00F8, -500, 0, -5670, 180)
    SetChrPos(0x00F9, 1150, 0, -4090, 90)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_749',
    )

    SetChrPos(0x00F9, -500, 0, -5670, 180)
    SetChrPos(0x00F8, 750, 0, -4790, 90)

    def _loc_749(): pass

    label('loc_749')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_778',
    )

    SetChrPos(0x00F9, -500, 0, -5670, 180)
    SetChrPos(0x00F8, 750, 0, -4790, 90)

    def _loc_778(): pass

    label('loc_778')

    SetChrChipByIndex(0x0101, 2)
    SetChrChipByIndex(0x0103, 3)

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_795',
    )

    SetChrChipByIndex(0x0104, 4)

    def _loc_795(): pass

    label('loc_795')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7A8',
    )

    SetChrChipByIndex(0x0105, 5)

    def _loc_7A8(): pass

    label('loc_7A8')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7BB',
    )

    SetChrChipByIndex(0x0106, 6)

    def _loc_7BB(): pass

    label('loc_7BB')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7CE',
    )

    SetChrChipByIndex(0x0107, 7)

    def _loc_7CE(): pass

    label('loc_7CE')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7E1',
    )

    SetChrChipByIndex(0x0108, 8)

    def _loc_7E1(): pass

    label('loc_7E1')

    TerminateThread(0x0008, 0x00)
    TerminateThread(0x0009, 0x00)
    TerminateThread(0x000A, 0x00)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    OP_79(0x00, 0x0002)
    OP_7B()
    OP_77(0xC0, 0xC0, 0xC0, 0x00, 0x00000000)
    OP_6D(240, 0, -3900, 0)
    SetChrPos(0x000B, 0, 0, -3900, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010471207V#1002F呼…………',
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
        'loc_88C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080471208V#070F看来收拾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_929')

    def _loc_88C(): pass

    label('loc_88C')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8C0',
    )

    ChrTalk(
        0x0106,
        (
            '#0050471209V#050F看来解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_929')

    def _loc_8C0(): pass

    label('loc_8C0')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8F6',
    )

    ChrTalk(
        0x0104,
        (
            '#0040471210V#030F看来收拾了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_929')

    def _loc_8F6(): pass

    label('loc_8F6')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_929',
    )

    ChrTalk(
        0x0105,
        (
            '#0060471211V#042F看来击退了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_929(): pass

    label('loc_929')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_961',
    )

    ChrTalk(
        0x0107,
        (
            '#0070471212V#561F……吓、吓死了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9F4')

    def _loc_961(): pass

    label('loc_961')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_993',
    )

    ChrTalk(
        0x0105,
        (
            '#0060471213V#042F……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9F4')

    def _loc_993(): pass

    label('loc_993')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9C5',
    )

    ChrTalk(
        0x0104,
        (
            '#0040471214V#031F……是吧⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9F4')

    def _loc_9C5(): pass

    label('loc_9C5')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9F4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050471215V#051F……是吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9F4(): pass

    label('loc_9F4')

    OP_22(0x0086, 0x00, 0x64)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7A(0x00, 0x0002)
    OP_7B()
    Sleep(400)

    OP_82(0x80, 0x02)
    OP_79(0x00, 0x0002)
    OP_7B()
    Sleep(800)

    OP_22(0x0086, 0x00, 0x64)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7A(0x00, 0x0002)
    OP_7B()
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)
    Sleep(500)

    SetChrChipByIndex(0x0101, 65535)

    @scena.Lambda('lambda_0A9D')
    def lambda_0A9D():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0A9D)

    OP_22(0x00D5, 0x00, 0x64)
    Sleep(200)

    SetChrChipByIndex(0x0103, 65535)

    @scena.Lambda('lambda_0ABA')
    def lambda_0ABA():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0003, lambda_0ABA)

    Sleep(200)

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_ADA',
    )

    SetChrChipByIndex(0x0104, 65535)

    def _loc_ADA(): pass

    label('loc_ADA')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AED',
    )

    SetChrChipByIndex(0x0105, 65535)

    def _loc_AED(): pass

    label('loc_AED')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B00',
    )

    SetChrChipByIndex(0x0106, 65535)

    def _loc_B00(): pass

    label('loc_B00')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B13',
    )

    SetChrChipByIndex(0x0107, 65535)

    def _loc_B13(): pass

    label('loc_B13')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B26',
    )

    SetChrChipByIndex(0x0108, 65535)

    def _loc_B26(): pass

    label('loc_B26')

    @scena.Lambda('lambda_0B2C')
    def lambda_0B2C():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x00F8, 0x0003, lambda_0B2C)

    @scena.Lambda('lambda_0B3A')
    def lambda_0B3A():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0003, lambda_0B3A)

    OP_22(0x00D5, 0x00, 0x64)
    WaitForThreadExit(0x0101, 0x0003)
    WaitForThreadExit(0x0103, 0x0003)
    WaitForThreadExit(0x00F8, 0x0003)
    WaitForThreadExit(0x00F9, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010471216V#1007F呼～害我紧张了一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471217V那种东西突然\n',
            '涌出来嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030471218V#027F这一带\n',
            '没见过的魔兽……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030471219V……这算是怪盗绅士流\n',
            '打招呼的方式吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C78',
    )

    ChrTalk(
        0x0104,
        (
            '#0040471220V#030F唔，大概是吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040471221V不过，看来这个\n',
            '好象是最后的障碍了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DB5')

    def _loc_C78(): pass

    label('loc_C78')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CE1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050471222V#050F啊啊，大概吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050471223V不过，看来这个\n',
            '好象是最后的障碍呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DB5')

    def _loc_CE1(): pass

    label('loc_CE1')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D4A',
    )

    ChrTalk(
        0x0108,
        (
            '#0080471224V#070F啊啊，恐怕是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080471225V不过，看来这个\n',
            '好象是最后的障碍哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DB5')

    def _loc_D4A(): pass

    label('loc_D4A')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DB5',
    )

    ChrTalk(
        0x0105,
        (
            '#0060471226V#047F嗯嗯，恐怕是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060471227V#040F不过，看来这个\n',
            '好象是最后的障碍了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DB5(): pass

    label('loc_DB5')

    ChrTalk(
        0x0103,
        (
            '#0030471228V#020F嗯嗯，接下来\n',
            '只剩取回委任书了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030471229V找找看吧。\n',
            '应该在这个房间里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010471230V#1015F啊，\n',
            '这可不能忘了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0077, 0x01, 0x4000)
    OP_65(0x02, 0x0001)
    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0xE50
@scena.Code('Init')
def Init():
    EventBegin(0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#16I矿山的委任书',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0101,
        (
            '#0010471231V#1018F好，回收完毕了！',
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
        'loc_F27',
    )

    ChrTalk(
        0x0107,
        (
            '#0070471232V#060F赶快还回去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070471233V叔叔……\n',
            '一定等得很着急吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1057')

    def _loc_F27(): pass

    label('loc_F27')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F91',
    )

    ChrTalk(
        0x0105,
        (
            '#0060471234V#040F那么，现在立刻\n',
            '回去还给他吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060471235V矿山长一定\n',
            '也非常担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1057')

    def _loc_F91(): pass

    label('loc_F91')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FF7',
    )

    ChrTalk(
        0x0104,
        (
            '#0040471236V#031F唔，那么赶快\n',
            '送还回去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040471237V老大一定\n',
            '十分的担心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1057')

    def _loc_FF7(): pass

    label('loc_FF7')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1057',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430383V#051F哦，那就早点还回去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050471238V大叔一定\n',
            '也在担心了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1057(): pass

    label('loc_1057')

    ChrTalk(
        0x0103,
        (
            '#0030471239V#021F呵呵，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010471240V#1006F嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T0111._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x0002 offset: 0x10B5
@scena.Code('ReInit')
def ReInit():
    OP_94(0x01, 0x00FE, 0x0000, 0x00001770, 0x000007D0, 0x00)
    CreateThread(0x00FE, 0x00, 0x00, 0x0002)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
