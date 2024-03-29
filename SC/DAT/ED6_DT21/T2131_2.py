import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2131_2_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2131_2 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2131.x'
    header.mapIndex       = 1
    header.bgm            = 12
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
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('Init')
def Init():
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
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
        1,
        (
            TXT(0x00, '阿加特第１战\n'),
            TXT(0x01, '雪拉扎德第２战\n'),
            TXT(0x02, '雪拉扎德第１战SD\n'),
            TXT(0x03, '共通 第２战\n'),
            TXT(0x04, '共通 第２战\n'),
            TXT(0x05, '阿加特第３战\n'),
            TXT(0x06, '菲利奥ＲＳＦ\n'),
            TXT(0x07, '雪拉扎德第３战\n'),
            TXT(0x08, '第３战艾丝蒂尔败SD\n'),
            TXT(0x09, '第３战雪拉败SD\n'),
            TXT(0x0A, '第３战ＲＳＦ胜SD\n'),
        ),
    )

    MenuEnd(0x0003)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19D',
    )

    Call(2, 0x0003)

    Jump('loc_265')

    def _loc_19D(): pass

    label('loc_19D')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B1',
    )

    Call(2, 0x0006)

    Jump('loc_265')

    def _loc_1B1(): pass

    label('loc_1B1')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C5',
    )

    Call(2, 0x0008)

    Jump('loc_265')

    def _loc_1C5(): pass

    label('loc_1C5')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1D9',
    )

    Call(2, 0x0009)

    Jump('loc_265')

    def _loc_1D9(): pass

    label('loc_1D9')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1ED',
    )

    Call(2, 0x0014)

    Jump('loc_265')

    def _loc_1ED(): pass

    label('loc_1ED')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_201',
    )

    Call(2, 0x000B)

    Jump('loc_265')

    def _loc_201(): pass

    label('loc_201')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_215',
    )

    Call(2, 0x0013)

    Jump('loc_265')

    def _loc_215(): pass

    label('loc_215')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_229',
    )

    Call(2, 0x000E)

    Jump('loc_265')

    def _loc_229(): pass

    label('loc_229')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_23D',
    )

    Call(2, 0x0010)

    Jump('loc_265')

    def _loc_23D(): pass

    label('loc_23D')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_251',
    )

    Call(2, 0x0011)

    Jump('loc_265')

    def _loc_251(): pass

    label('loc_251')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_265',
    )

    Call(2, 0x0012)

    Jump('loc_265')

    def _loc_265(): pass

    label('loc_265')

    Return()

# id: 0x0001 offset: 0x266
@scena.Code('func_01_266')
def func_01_266():
    OP_26(18)

    ChrTalk(
        0x00FE,
        (
            '卡片分配测试哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    OP_C5(0x05, 0, 0, 100, 160, 113, 152, 512, 512, 400, 0, 500, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x06, 0, 0, 100, 160, 193, 154, 512, 512, 0, 320, 100, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x07, 0, 0, 100, 160, 273, 156, 512, 512, 200, 320, 300, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, 0, 0, 100, 160, 353, 158, 512, 512, 100, 0, 200, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, 0, 0, 100, 160, 433, 160, 512, 512, 100, 320, 200, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C6(0x05, 0x03, -1, 0, 0)
    OP_C6(0x06, 0x03, -1, 0, 0)
    OP_C6(0x07, 0x03, -1, 0, 0)
    OP_C6(0x08, 0x03, -1, 0, 0)
    OP_C6(0x09, 0x03, -1, 0, 0)

    ChrTalk(
        0x00FE,
        (
            '要翻开看……是明天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_C7(0x01, 0xFF, 0x00)
    FadeIn(300, 0)

    Return()

# id: 0x0002 offset: 0x3D8
@scena.Code('func_02_3D8')
def func_02_3D8():
    OP_26(254)
    OP_C5(0x00, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x01, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x02, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x03, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x04, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C6(0x00, 0x02, 125000, 0, 0)
    OP_C6(0x01, 0x02, 125000, 0, 0)
    OP_C6(0x02, 0x02, 125000, 0, 0)
    OP_C6(0x03, 0x02, 125000, 0, 0)
    OP_C6(0x04, 0x02, 125000, 0, 0)
    OP_C6(0x00, 0x03, -1, 0, 0)
    OP_C6(0x01, 0x03, -1, 0, 0)
    OP_C6(0x02, 0x03, -1, 0, 0)
    OP_C6(0x03, 0x03, -1, 0, 0)
    OP_C6(0x04, 0x03, -1, 0, 0)
    OP_C6(0x00, 0x02, 0, 500, 0)
    OP_C6(0x00, 0x00, 483000, 240000, 500)
    Sleep(48)

    OP_C6(0x01, 0x02, 0, 500, 0)
    OP_C6(0x01, 0x00, 481000, 238000, 500)
    Sleep(48)

    OP_C6(0x02, 0x02, 0, 500, 0)
    OP_C6(0x02, 0x00, 479000, 236000, 500)
    Sleep(48)

    OP_C6(0x03, 0x02, 0, 500, 0)
    OP_C6(0x03, 0x00, 477000, 234000, 500)
    Sleep(48)

    OP_C6(0x04, 0x02, 0, 500, 0)
    OP_C6(0x04, 0x00, 475000, 232000, 500)
    PlaySE(254, 0x00, 0x64)
    OP_C7(0x00, 0x00, 0x00)
    OP_C7(0x00, 0x01, 0x00)
    OP_C7(0x00, 0x02, 0x00)
    OP_C7(0x00, 0x03, 0x00)
    OP_C7(0x00, 0x04, 0x00)
    Sleep(256)

    OP_C6(0x00, 0x00, 163000, 232000, 400)
    OP_C6(0x01, 0x00, 161000, 230000, 400)
    OP_C6(0x02, 0x00, 159000, 228000, 400)
    OP_C6(0x03, 0x00, 157000, 226000, 400)
    OP_C6(0x04, 0x00, 155000, 224000, 400)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x01, 0x00, 243000, 234000, 50)
    OP_C6(0x02, 0x00, 241000, 232000, 50)
    OP_C6(0x03, 0x00, 239000, 230000, 50)
    OP_C6(0x04, 0x00, 237000, 228000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x02, 0x00, 323000, 236000, 50)
    OP_C6(0x03, 0x00, 321000, 234000, 50)
    OP_C6(0x04, 0x00, 319000, 232000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x03, 0x00, 403000, 238000, 50)
    OP_C6(0x04, 0x00, 401000, 236000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x04, 0x00, 483000, 240000, 50)
    OP_C7(0x00, 0x04, 0x00)

    Return()

# id: 0x0003 offset: 0x70B
@scena.Code('func_03_70B')
def func_03_70B():
    FadeOut(300, 0, 100)
    Call(2, 0x0002)
    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 400, 0, 500, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 0, 320, 100, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 200, 320, 300, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 100, 0, 200, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 100, 320, 200, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    CreateThread(0x0019, 0x01, 0x02, 0x001D)
    Sleep(100)

    CreateThread(0x0019, 0x02, 0x02, 0x001E)
    Sleep(100)

    CreateThread(0x0019, 0x03, 0x02, 0x001F)
    Sleep(100)

    CreateThread(0x001A, 0x01, 0x02, 0x0020)
    Sleep(100)

    CreateThread(0x001A, 0x02, 0x02, 0x0021)
    WaitForThreadExit(0x001A, 0x0002)
    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050440691V#050F（呼……\n',
            '　这可真是的。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440692V（目标放在４，５，６，７，８的\n',
            '　顺子倒也能行……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440693V（说实话，希望相当渺茫啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)

    Return()

# id: 0x0004 offset: 0x98C
@scena.Code('func_04_98C')
def func_04_98C():
    FadeOut(300, 0, 100)
    OP_C5(0x00, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x01, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x02, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x03, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x04, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 400, 0, 500, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 0, 320, 100, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 200, 320, 300, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 100, 0, 200, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 100, 320, 200, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C6(0x05, 0x04, 0, 0, 0)
    OP_C6(0x06, 0x04, 0, 0, 0)
    OP_C6(0x07, 0x04, 0, 0, 0)
    OP_C6(0x08, 0x04, 0, 0, 0)
    OP_C6(0x09, 0x04, 0, 0, 0)
    OP_C6(0x05, 0x03, -1, 400, 0)
    OP_C6(0x06, 0x03, -1, 400, 0)
    OP_C6(0x07, 0x03, -1, 400, 0)
    OP_C6(0x08, 0x03, -1, 400, 0)
    OP_C6(0x09, 0x03, -1, 400, 0)
    Sleep(1000)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F37',
    )

    OP_C6(0x09, 0x00, 1048000, 240000, 500)
    Sleep(24)

    PlaySE(254, 0x00, 0x64)
    OP_C6(0x08, 0x00, 1003000, 238000, 500)
    Sleep(24)

    OP_C6(0x06, 0x00, 843000, 234000, 500)
    Sleep(24)

    OP_C6(0x05, 0x00, 763000, 232000, 500)
    Sleep(24)

    OP_C7(0x00, 0x05, 0x00)
    OP_C7(0x00, 0x06, 0x00)
    OP_C7(0x00, 0x08, 0x00)
    OP_C7(0x00, 0x09, 0x00)
    OP_C7(0x01, 0x09, 0x00)
    OP_C7(0x01, 0x08, 0x00)
    OP_C7(0x01, 0x06, 0x00)
    OP_C7(0x01, 0x05, 0x00)
    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 300, 0, 400, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 200, 0, 300, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 100, 320, 200, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 300, 320, 400, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C6(0x00, 0x00, 163000, -160000, 0)
    OP_C6(0x01, 0x00, 243000, -160000, 0)
    OP_C6(0x03, 0x00, 403000, -160000, 0)
    OP_C6(0x04, 0x00, 483000, -160000, 0)
    OP_C6(0x00, 0x01, 1000, 1000, 0)
    OP_C6(0x01, 0x01, 1000, 1000, 0)
    OP_C6(0x03, 0x01, 1000, 1000, 0)
    OP_C6(0x04, 0x01, 1000, 1000, 0)
    OP_C6(0x00, 0x03, -1, 0, 0)
    OP_C6(0x01, 0x03, -1, 0, 0)
    OP_C6(0x03, 0x03, -1, 0, 0)
    OP_C6(0x04, 0x03, -1, 0, 0)
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x01, 0x04, 0, 0, 0)
    OP_C6(0x07, 0x04, 0, 0, 0)
    OP_C6(0x03, 0x04, 0, 0, 0)
    OP_C6(0x04, 0x04, 0, 0, 0)
    Sleep(400)

    OP_C6(0x00, 0x00, 163000, 232000, 200)
    Sleep(124)

    PlaySE(254, 0x00, 0x64)
    OP_C6(0x01, 0x00, 243000, 234000, 200)
    Sleep(124)

    OP_C6(0x03, 0x00, 403000, 238000, 200)
    Sleep(124)

    OP_C6(0x04, 0x00, 483000, 240000, 200)
    Sleep(124)

    OP_C7(0x00, 0x04, 0x00)
    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050440694V#050F（那么……怎么办？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    CreateThread(0x0019, 0x01, 0x02, 0x001D)
    Sleep(100)

    OP_C6(0x05, 0x04, 0, 0, 0)
    CreateThread(0x0019, 0x02, 0x02, 0x001E)
    Sleep(100)

    OP_C6(0x06, 0x04, 0, 0, 0)
    OP_C6(0x07, 0x04, 0, 0, 0)
    CreateThread(0x001A, 0x01, 0x02, 0x0020)
    Sleep(100)

    OP_C6(0x08, 0x04, 0, 0, 0)
    CreateThread(0x001A, 0x02, 0x02, 0x0021)
    Sleep(100)

    OP_C6(0x09, 0x04, 0, 0, 0)
    WaitForThreadExit(0x001A, 0x0002)

    Jump('loc_1128')

    def _loc_F37(): pass

    label('loc_F37')

    OP_C6(0x09, 0x00, 1048000, 240000, 500)
    Sleep(24)

    PlaySE(254, 0x00, 0x64)
    OP_C6(0x07, 0x00, 923000, 236000, 500)
    Sleep(24)

    OP_C7(0x00, 0x07, 0x00)
    OP_C7(0x00, 0x09, 0x00)
    OP_C7(0x01, 0x09, 0x00)
    OP_C7(0x01, 0x07, 0x00)
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 300, 0, 400, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 400, 160, 500, 320, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C6(0x02, 0x00, 323000, -160000, 0)
    OP_C6(0x04, 0x00, 483000, -160000, 0)
    OP_C6(0x02, 0x01, 1000, 1000, 0)
    OP_C6(0x04, 0x01, 1000, 1000, 0)
    OP_C6(0x02, 0x03, -1, 0, 0)
    OP_C6(0x04, 0x03, -1, 0, 0)
    OP_C6(0x05, 0x04, 0, 0, 0)
    OP_C6(0x06, 0x04, 0, 0, 0)
    OP_C6(0x02, 0x04, 0, 0, 0)
    OP_C6(0x08, 0x04, 0, 0, 0)
    OP_C6(0x04, 0x04, 0, 0, 0)
    OP_C6(0x02, 0x00, 323000, 236000, 200)
    Sleep(124)

    PlaySE(254, 0x00, 0x64)
    OP_C6(0x04, 0x00, 483000, 240000, 200)
    Sleep(124)

    OP_C7(0x00, 0x04, 0x00)
    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050440695V#050F（那么……怎么办？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    CreateThread(0x0019, 0x03, 0x02, 0x001F)
    Sleep(100)

    OP_C6(0x07, 0x04, 0, 0, 0)
    OP_C6(0x08, 0x04, 0, 0, 0)
    CreateThread(0x001A, 0x02, 0x02, 0x0021)
    Sleep(100)

    OP_C6(0x09, 0x04, 0, 0, 0)
    WaitForThreadExit(0x001A, 0x0002)

    def _loc_1128(): pass

    label('loc_1128')

    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050440696V#050F（可恶……\n',
            '　结果没法凑牌吗。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)

    Return()

# id: 0x0005 offset: 0x121C
@scena.Code('func_05_121C')
def func_05_121C():
    FadeOut(300, 0, 100)
    OP_C5(0x00, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x01, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x02, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x03, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x04, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13EE',
    )

    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 300, 0, 400, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 200, 0, 300, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 200, 320, 300, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 100, 320, 200, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 300, 320, 400, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')

    Jump('loc_14CA')

    def _loc_13EE(): pass

    label('loc_13EE')

    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 400, 0, 500, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 0, 320, 100, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 300, 0, 400, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 100, 0, 200, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 400, 160, 500, 320, 0x00FFFFFF, 0x00, 'C_VIS228._CH')

    def _loc_14CA(): pass

    label('loc_14CA')

    OP_C6(0x05, 0x03, -1, 400, 0)
    OP_C6(0x06, 0x03, -1, 400, 0)
    OP_C6(0x07, 0x03, -1, 400, 0)
    OP_C6(0x08, 0x03, -1, 400, 0)
    OP_C6(0x09, 0x03, -1, 400, 0)
    Sleep(1000)

    ChrSetDirection(0x000D, 90, 0)
    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050440697V#050F（没办法了……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440698V（也就是说，如果对方\n',
            '　要求比牌就一定输了。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440699V（进还是退……\n',
            '好了，押哪个？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
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
            TXT(0x00, '【比牌】\n'),
            TXT(0x01, '【放弃】\n'),
        ),
    )

    MenuEnd(0x0003)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_167B',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050440700V#053F（……才刚刚开始。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440701V（现在逞强\n',
            '　输了就无法挽回了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_16E4')

    def _loc_167B(): pass

    label('loc_167B')

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            '#0050440702V#053F（呵呵……投降……吗？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050440703V#050F（我怎么可能选这个。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_16E4(): pass

    label('loc_16E4')

    OP_59()
    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)

    Return()

# id: 0x0006 offset: 0x178D
@scena.Code('func_06_178D')
def func_06_178D():
    FadeOut(300, 0, 100)
    Call(2, 0x0002)
    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 0, 160, 100, 320, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 100, 320, 200, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 300, 160, 400, 320, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 300, 0, 400, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 300, 0, 400, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    CreateThread(0x0019, 0x01, 0x02, 0x001D)
    Sleep(100)

    CreateThread(0x0019, 0x02, 0x02, 0x001E)
    Sleep(100)

    CreateThread(0x0019, 0x03, 0x02, 0x001F)
    Sleep(100)

    CreateThread(0x001A, 0x01, 0x02, 0x0020)
    Sleep(100)

    CreateThread(0x001A, 0x02, 0x02, 0x0021)
    WaitForThreadExit(0x001A, 0x0002)
    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010440704V#1018F（啊，有一对⊙）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440705V#1006F（呼呼呼，不错哦～）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440706V（虽然也可以凑同花，\n',
            '　但是不是难了点？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)

    Return()

# id: 0x0007 offset: 0x19FA
@scena.Code('func_07_19FA')
def func_07_19FA():
    FadeOut(300, 0, 100)
    OP_C5(0x00, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x01, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x02, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x03, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x04, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 0, 160, 100, 320, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 100, 320, 200, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 300, 160, 400, 320, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 300, 0, 400, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 300, 0, 400, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C6(0x05, 0x03, -1, 400, 0)
    OP_C6(0x06, 0x03, -1, 400, 0)
    OP_C6(0x07, 0x03, -1, 400, 0)
    OP_C6(0x08, 0x03, -1, 400, 0)
    OP_C6(0x09, 0x03, -1, 400, 0)
    Sleep(1000)

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1F25',
    )

    OP_C6(0x09, 0x00, 1048000, 240000, 500)
    Sleep(24)

    PlaySE(254, 0x00, 0x64)
    OP_C6(0x08, 0x00, 1003000, 238000, 500)
    Sleep(24)

    OP_C6(0x07, 0x00, 923000, 236000, 500)
    Sleep(24)

    OP_C7(0x00, 0x07, 0x00)
    OP_C7(0x00, 0x08, 0x00)
    OP_C7(0x00, 0x09, 0x00)
    OP_C7(0x01, 0x09, 0x00)
    OP_C7(0x01, 0x08, 0x00)
    OP_C7(0x01, 0x07, 0x00)
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 100, 0, 200, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 200, 320, 300, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 400, 0, 500, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C6(0x02, 0x00, 323000, -160000, 0)
    OP_C6(0x03, 0x00, 403000, -160000, 0)
    OP_C6(0x04, 0x00, 483000, -160000, 0)
    OP_C6(0x02, 0x01, 1000, 1000, 0)
    OP_C6(0x03, 0x01, 1000, 1000, 0)
    OP_C6(0x04, 0x01, 1000, 1000, 0)
    OP_C6(0x02, 0x03, -1, 0, 0)
    OP_C6(0x03, 0x03, -1, 0, 0)
    OP_C6(0x04, 0x03, -1, 0, 0)
    OP_C6(0x05, 0x04, 0, 0, 0)
    OP_C6(0x06, 0x04, 0, 0, 0)
    OP_C6(0x02, 0x04, 0, 0, 0)
    OP_C6(0x03, 0x04, 0, 0, 0)
    OP_C6(0x04, 0x04, 0, 0, 0)
    Sleep(400)

    OP_C6(0x02, 0x00, 323000, 236000, 200)
    Sleep(124)

    PlaySE(254, 0x00, 0x64)
    OP_C6(0x03, 0x00, 403000, 238000, 200)
    Sleep(124)

    OP_C6(0x04, 0x00, 483000, 240000, 200)
    Sleep(124)

    OP_C7(0x00, 0x04, 0x00)
    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010440707V#1006F（拜托快来我想要的牌～）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    CreateThread(0x0019, 0x03, 0x02, 0x001F)
    Sleep(100)

    OP_C6(0x07, 0x04, 0, 0, 0)
    CreateThread(0x001A, 0x01, 0x02, 0x0020)
    Sleep(100)

    OP_C6(0x08, 0x04, 0, 0, 0)
    CreateThread(0x001A, 0x02, 0x02, 0x0021)
    Sleep(100)

    OP_C6(0x09, 0x04, 0, 0, 0)
    WaitForThreadExit(0x001A, 0x0002)
    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010440708V#1015F（嗯～几乎没什么变化。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440709V（算了，有一对\n',
            '　就还算可以了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_21B6')

    def _loc_1F25(): pass

    label('loc_1F25')

    OP_C6(0x08, 0x00, 1003000, 238000, 500)
    Sleep(24)

    PlaySE(254, 0x00, 0x64)
    OP_C6(0x06, 0x00, 843000, 234000, 500)
    Sleep(24)

    OP_C7(0x00, 0x06, 0x00)
    OP_C7(0x00, 0x08, 0x00)
    OP_C7(0x01, 0x08, 0x00)
    OP_C7(0x01, 0x06, 0x00)
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 200, 0, 300, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 200, 320, 300, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C6(0x01, 0x00, 243000, -160000, 0)
    OP_C6(0x03, 0x00, 403000, -160000, 0)
    OP_C6(0x01, 0x01, 1000, 1000, 0)
    OP_C6(0x03, 0x01, 1000, 1000, 0)
    OP_C6(0x01, 0x03, -1, 0, 0)
    OP_C6(0x03, 0x03, -1, 0, 0)
    OP_C6(0x05, 0x04, 0, 0, 0)
    OP_C6(0x01, 0x04, 0, 0, 0)
    OP_C6(0x07, 0x04, 0, 0, 0)
    OP_C6(0x03, 0x04, 0, 0, 0)
    OP_C6(0x09, 0x04, 0, 0, 0)
    OP_C6(0x01, 0x00, 243000, 234000, 200)
    Sleep(124)

    PlaySE(254, 0x00, 0x64)
    OP_C6(0x03, 0x00, 403000, 238000, 200)
    Sleep(124)

    OP_C7(0x00, 0x03, 0x00)
    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010440710V#1006F（拜托快来我想要的牌～）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    CreateThread(0x0019, 0x02, 0x02, 0x001E)
    Sleep(100)

    OP_C6(0x06, 0x04, 0, 0, 0)
    OP_C6(0x07, 0x04, 0, 0, 0)
    CreateThread(0x001A, 0x01, 0x02, 0x0020)
    Sleep(100)

    OP_C6(0x08, 0x04, 0, 0, 0)
    OP_C6(0x09, 0x04, 0, 0, 0)
    WaitForThreadExit(0x001A, 0x0002)
    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010440711V#1020F（啊啊！？\n',
            '好、好可惜……！！）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440712V（虽然可惜……\n',
            '　但这下不是没牌组了吗～！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_21B6(): pass

    label('loc_21B6')

    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)

    Return()

# id: 0x0008 offset: 0x225E
@scena.Code('func_08_225E')
def func_08_225E():
    FadeOut(300, 0, 100)
    OP_C5(0x00, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x01, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x02, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x03, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x04, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2430',
    )

    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 0, 160, 100, 320, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 100, 320, 200, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 100, 0, 200, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 200, 320, 300, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 400, 0, 500, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')

    Jump('loc_250C')

    def _loc_2430(): pass

    label('loc_2430')

    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 0, 160, 100, 320, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 200, 0, 300, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 300, 160, 400, 320, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 200, 320, 300, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 300, 0, 400, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')

    def _loc_250C(): pass

    label('loc_250C')

    OP_C6(0x05, 0x03, -1, 400, 0)
    OP_C6(0x06, 0x03, -1, 400, 0)
    OP_C6(0x07, 0x03, -1, 400, 0)
    OP_C6(0x08, 0x03, -1, 400, 0)
    OP_C6(0x09, 0x03, -1, 400, 0)
    Sleep(1000)

    ChrSetDirection(0x000D, 90, 0)

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_25F8',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010440713V#1002F（虽然如此，\n',
            '但能不能赢还是看对手了。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440714V（放弃还是比牌……\n',
            '  好了，押哪个？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_26B5')

    def _loc_25F8(): pass

    label('loc_25F8')

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010440715V#1003F（嗯～现在手上没什么好牌……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440716V（现在就算比牌，\n',
            '　万一对方接受了就真输了。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440717V#1002F（放弃还是比牌……\n',
            '  好了，押哪个？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_26B5(): pass

    label('loc_26B5')

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
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
            TXT(0x00, '【比牌】\n'),
            TXT(0x01, '【放弃】\n'),
        ),
    )

    MenuEnd(0x0003)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_277E',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010440718V#1007F（……呼，现在才刚刚第一回合。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440719V（现在逞强\n',
            '　输了就无法挽回了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_27F4')

    def _loc_277E(): pass

    label('loc_277E')

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010440720V#1009F（放弃的话\n',
            '  不就等于是认输吗？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440721V（这种时候意气用事也没用。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_27F4(): pass

    label('loc_27F4')

    OP_59()
    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)

    Return()

# id: 0x0009 offset: 0x289D
@scena.Code('func_09_289D')
def func_09_289D():
    FadeOut(300, 0, 100)
    Call(2, 0x0002)
    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 0, 320, 100, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 200, 0, 300, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 400, 0, 500, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 100, 0, 200, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 200, 320, 300, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    CreateThread(0x0019, 0x01, 0x02, 0x001D)
    Sleep(100)

    CreateThread(0x0019, 0x02, 0x02, 0x001E)
    Sleep(100)

    CreateThread(0x0019, 0x03, 0x02, 0x001F)
    Sleep(100)

    CreateThread(0x001A, 0x01, 0x02, 0x0020)
    Sleep(100)

    CreateThread(0x001A, 0x02, 0x02, 0x0021)
    WaitForThreadExit(0x001A, 0x0002)
    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('奥利维尔')

    Talk(
        (
            '#0040440722V#030F（呼，是一对４吗……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440723V（不过，只有这个\n',
            '  有点靠不住。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)

    Return()

# id: 0x000A offset: 0x2ADF
@scena.Code('func_0A_2ADF')
def func_0A_2ADF():
    FadeOut(300, 0, 100)
    OP_C5(0x00, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x01, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x02, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x03, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x04, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 0, 320, 100, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 200, 0, 300, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 400, 0, 500, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 100, 0, 200, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 200, 320, 300, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C6(0x05, 0x03, -1, 400, 0)
    OP_C6(0x06, 0x03, -1, 400, 0)
    OP_C6(0x07, 0x03, -1, 400, 0)
    OP_C6(0x08, 0x03, -1, 400, 0)
    OP_C6(0x09, 0x03, -1, 400, 0)
    Sleep(1000)

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FEF',
    )

    OP_C6(0x09, 0x00, 1048000, 240000, 500)
    Sleep(24)

    PlaySE(254, 0x00, 0x64)
    OP_C6(0x08, 0x00, 1003000, 238000, 500)
    Sleep(24)

    OP_C6(0x07, 0x00, 923000, 236000, 500)
    Sleep(24)

    OP_C7(0x00, 0x07, 0x00)
    OP_C7(0x00, 0x08, 0x00)
    OP_C7(0x00, 0x09, 0x00)
    OP_C7(0x01, 0x09, 0x00)
    OP_C7(0x01, 0x08, 0x00)
    OP_C7(0x01, 0x07, 0x00)
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 300, 0, 400, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 200, 0, 300, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 100, 0, 200, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C6(0x02, 0x00, 323000, -160000, 0)
    OP_C6(0x03, 0x00, 403000, -160000, 0)
    OP_C6(0x04, 0x00, 483000, -160000, 0)
    OP_C6(0x02, 0x01, 1000, 1000, 0)
    OP_C6(0x03, 0x01, 1000, 1000, 0)
    OP_C6(0x04, 0x01, 1000, 1000, 0)
    OP_C6(0x02, 0x03, -1, 0, 0)
    OP_C6(0x03, 0x03, -1, 0, 0)
    OP_C6(0x04, 0x03, -1, 0, 0)
    OP_C6(0x05, 0x04, 0, 0, 0)
    OP_C6(0x06, 0x04, 0, 0, 0)
    OP_C6(0x02, 0x04, 0, 0, 0)
    OP_C6(0x03, 0x04, 0, 0, 0)
    OP_C6(0x04, 0x04, 0, 0, 0)
    Sleep(400)

    OP_C6(0x02, 0x00, 323000, 236000, 200)
    Sleep(124)

    PlaySE(254, 0x00, 0x64)
    OP_C6(0x03, 0x00, 403000, 238000, 200)
    Sleep(124)

    OP_C6(0x04, 0x00, 483000, 240000, 200)
    Sleep(124)

    OP_C7(0x00, 0x04, 0x00)
    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('奥利维尔')

    Talk(
        (
            '#0040440724V#030F（那么，怎么办呢？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    CreateThread(0x0019, 0x03, 0x02, 0x001F)
    Sleep(100)

    OP_C6(0x07, 0x04, 0, 0, 0)
    CreateThread(0x001A, 0x01, 0x02, 0x0020)
    Sleep(100)

    OP_C6(0x08, 0x04, 0, 0, 0)
    CreateThread(0x001A, 0x02, 0x02, 0x0021)
    Sleep(100)

    OP_C6(0x09, 0x04, 0, 0, 0)
    WaitForThreadExit(0x001A, 0x0002)
    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('奥利维尔')

    Talk(
        (
            '#0040440725V#030F（呼，出来了吗？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440726V（这牌足够比了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_319F')

    def _loc_2FEF(): pass

    label('loc_2FEF')

    OP_C6(0x09, 0x00, 1048000, 240000, 500)
    Sleep(24)

    PlaySE(254, 0x00, 0x64)
    OP_C7(0x00, 0x09, 0x00)
    OP_C7(0x01, 0x09, 0x00)
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 300, 0, 400, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C6(0x04, 0x00, 483000, -160000, 0)
    OP_C6(0x04, 0x01, 1000, 1000, 0)
    OP_C6(0x04, 0x03, -1, 0, 0)
    OP_C6(0x05, 0x04, 0, 0, 0)
    OP_C6(0x06, 0x04, 0, 0, 0)
    OP_C6(0x07, 0x04, 0, 0, 0)
    OP_C6(0x08, 0x04, 0, 0, 0)
    OP_C6(0x04, 0x04, 0, 0, 0)
    OP_C6(0x04, 0x00, 483000, 240000, 200)
    Sleep(124)

    PlaySE(254, 0x00, 0x64)
    OP_C7(0x00, 0x04, 0x00)
    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('奥利维尔')

    Talk(
        (
            '#0040440727V#030F（那么，怎么办呢？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    CreateThread(0x001A, 0x02, 0x02, 0x0021)
    Sleep(100)

    OP_C6(0x09, 0x04, 0, 0, 0)
    WaitForThreadExit(0x001A, 0x0002)
    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('奥利维尔')

    Talk(
        (
            '#0040440728V#030F（……不变吗～？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440729V（既然如此，\n',
            '  之后就看对方了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_319F(): pass

    label('loc_319F')

    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)

    Return()

# id: 0x000B offset: 0x3247
@scena.Code('func_0B_3247')
def func_0B_3247():
    FadeOut(300, 0, 100)
    Call(2, 0x0002)
    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 400, 0, 500, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 0, 160, 100, 320, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 300, 0, 400, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 100, 320, 200, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 200, 0, 300, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    CreateThread(0x0019, 0x01, 0x02, 0x001D)
    Sleep(100)

    CreateThread(0x0019, 0x02, 0x02, 0x001E)
    Sleep(100)

    CreateThread(0x0019, 0x03, 0x02, 0x001F)
    Sleep(100)

    CreateThread(0x001A, 0x01, 0x02, 0x0020)
    Sleep(100)

    CreateThread(0x001A, 0x02, 0x02, 0x0021)
    WaitForThreadExit(0x001A, 0x0002)
    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010440730V#1002F（嗯～很微妙啊。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440731V（虽然现在没对牌可组合，\n',
            '  但同花似乎凑得出来。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)

    Return()

# id: 0x000C offset: 0x3496
@scena.Code('func_0C_3496')
def func_0C_3496():
    FadeOut(300, 0, 100)
    OP_C5(0x00, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x01, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x02, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x03, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x04, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 400, 0, 500, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 0, 160, 100, 320, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 300, 0, 400, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 100, 320, 200, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 200, 0, 300, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C6(0x05, 0x03, -1, 400, 0)
    OP_C6(0x06, 0x03, -1, 400, 0)
    OP_C6(0x07, 0x03, -1, 400, 0)
    OP_C6(0x08, 0x03, -1, 400, 0)
    OP_C6(0x09, 0x03, -1, 400, 0)
    Sleep(1000)

    OP_C6(0x09, 0x00, 1048000, 240000, 500)
    Sleep(24)

    PlaySE(254, 0x00, 0x64)
    OP_C6(0x08, 0x00, 1003000, 238000, 500)
    Sleep(24)

    OP_C7(0x00, 0x08, 0x00)
    OP_C7(0x00, 0x09, 0x00)
    OP_C7(0x01, 0x09, 0x00)
    OP_C7(0x01, 0x08, 0x00)
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 100, 0, 200, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C6(0x03, 0x00, 403000, -160000, 0)
    OP_C6(0x04, 0x00, 483000, -160000, 0)
    OP_C6(0x03, 0x01, 1000, 1000, 0)
    OP_C6(0x04, 0x01, 1000, 1000, 0)
    OP_C6(0x03, 0x03, -1, 0, 0)
    OP_C6(0x04, 0x03, -1, 0, 0)
    OP_C6(0x05, 0x04, 0, 0, 0)
    OP_C6(0x06, 0x04, 0, 0, 0)
    OP_C6(0x07, 0x04, 0, 0, 0)
    OP_C6(0x03, 0x04, 0, 0, 0)
    OP_C6(0x04, 0x04, 0, 0, 0)
    Sleep(400)

    OP_C6(0x03, 0x00, 403000, 238000, 200)
    Sleep(124)

    PlaySE(254, 0x00, 0x64)
    OP_C6(0x04, 0x00, 483000, 240000, 200)
    Sleep(124)

    OP_C7(0x00, 0x04, 0x00)
    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010440732V#1006F（拜托快来我想要的牌～）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    CreateThread(0x001A, 0x01, 0x02, 0x0020)
    Sleep(100)

    OP_C6(0x08, 0x04, 0, 0, 0)
    CreateThread(0x001A, 0x02, 0x02, 0x0021)
    Sleep(100)

    OP_C6(0x09, 0x04, 0, 0, 0)
    WaitForThreadExit(0x001A, 0x0002)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010440733V#1018F（来、来了～～～～～～～！）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010440734V（来得好顺！\n',
            '　好，同花完成啦！！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)

    Return()

# id: 0x000D offset: 0x39D2
@scena.Code('func_0D_39D2')
def func_0D_39D2():
    FadeOut(300, 0, 100)
    OP_C5(0x00, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x01, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x02, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x03, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x04, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 400, 0, 500, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 0, 160, 100, 320, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 300, 0, 400, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 100, 320, 200, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 200, 0, 300, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C6(0x05, 0x03, -1, 400, 0)
    OP_C6(0x06, 0x03, -1, 400, 0)
    OP_C6(0x07, 0x03, -1, 400, 0)
    OP_C6(0x08, 0x03, -1, 400, 0)
    OP_C6(0x09, 0x03, -1, 400, 0)
    Sleep(1000)

    OP_C6(0x09, 0x00, 1048000, 240000, 500)
    Sleep(24)

    PlaySE(254, 0x00, 0x64)
    OP_C6(0x08, 0x00, 1003000, 238000, 500)
    Sleep(24)

    OP_C6(0x07, 0x00, 923000, 236000, 500)
    Sleep(24)

    OP_C6(0x06, 0x00, 843000, 234000, 500)
    Sleep(24)

    OP_C6(0x05, 0x00, 763000, 232000, 500)
    Sleep(24)

    OP_C7(0x00, 0x05, 0x00)
    OP_C7(0x01, 0x09, 0x00)
    OP_C7(0x01, 0x08, 0x00)
    OP_C7(0x01, 0x07, 0x00)
    OP_C7(0x01, 0x06, 0x00)
    OP_C7(0x01, 0x05, 0x00)
    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 400, 320, 500, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 100, 320, 200, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 0, 320, 100, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 200, 320, 300, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 300, 320, 400, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C6(0x00, 0x00, 163000, -160000, 0)
    OP_C6(0x01, 0x00, 243000, -160000, 0)
    OP_C6(0x02, 0x00, 323000, -160000, 0)
    OP_C6(0x03, 0x00, 403000, -160000, 0)
    OP_C6(0x04, 0x00, 483000, -160000, 0)
    OP_C6(0x00, 0x01, 1000, 1000, 0)
    OP_C6(0x01, 0x01, 1000, 1000, 0)
    OP_C6(0x02, 0x01, 1000, 1000, 0)
    OP_C6(0x03, 0x01, 1000, 1000, 0)
    OP_C6(0x04, 0x01, 1000, 1000, 0)
    OP_C6(0x00, 0x03, -1, 0, 0)
    OP_C6(0x01, 0x03, -1, 0, 0)
    OP_C6(0x02, 0x03, -1, 0, 0)
    OP_C6(0x03, 0x03, -1, 0, 0)
    OP_C6(0x04, 0x03, -1, 0, 0)
    OP_C6(0x04, 0x04, 0, 0, 0)
    OP_C6(0x03, 0x04, 0, 0, 0)
    OP_C6(0x02, 0x04, 0, 0, 0)
    OP_C6(0x01, 0x04, 0, 0, 0)
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x00, 0x00, 163000, 232000, 200)
    Sleep(124)

    PlaySE(254, 0x00, 0x64)
    OP_C6(0x01, 0x00, 243000, 234000, 200)
    Sleep(124)

    OP_C6(0x02, 0x00, 323000, 236000, 200)
    Sleep(124)

    OP_C6(0x03, 0x00, 403000, 238000, 200)
    Sleep(124)

    OP_C6(0x04, 0x00, 483000, 240000, 200)
    Sleep(124)

    OP_C7(0x00, 0x04, 0x00)

    ChrTalk(
        0x00FE,
        (
            '要翻开看……是明天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_C6(0x09, 0x04, 0, 0, 0)
    OP_C6(0x08, 0x04, 0, 0, 0)
    OP_C6(0x07, 0x04, 0, 0, 0)
    OP_C6(0x06, 0x04, 0, 0, 0)
    OP_C6(0x05, 0x04, 0, 0, 0)
    CreateThread(0x0019, 0x01, 0x02, 0x001D)
    Sleep(100)

    CreateThread(0x0019, 0x02, 0x02, 0x001E)
    Sleep(100)

    CreateThread(0x0019, 0x03, 0x02, 0x001F)
    Sleep(100)

    CreateThread(0x001A, 0x01, 0x02, 0x0020)
    Sleep(100)

    CreateThread(0x001A, 0x02, 0x02, 0x0021)
    WaitForThreadExit(0x001A, 0x0002)

    ChrTalk(
        0x00FE,
        (
            '要翻开看……是明天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)

    Return()

# id: 0x000E offset: 0x403D
@scena.Code('func_0E_403D')
def func_0E_403D():
    FadeOut(300, 0, 100)
    Call(2, 0x0002)
    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 100, 320, 200, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 400, 320, 500, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 100, 0, 200, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 0, 320, 100, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 300, 0, 400, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    CreateThread(0x0019, 0x01, 0x02, 0x001D)
    Sleep(100)

    CreateThread(0x0019, 0x02, 0x02, 0x001E)
    Sleep(100)

    CreateThread(0x0019, 0x03, 0x02, 0x001F)
    Sleep(100)

    CreateThread(0x001A, 0x01, 0x02, 0x0020)
    Sleep(100)

    CreateThread(0x001A, 0x02, 0x02, 0x0021)
    WaitForThreadExit(0x001A, 0x0002)
    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('雪拉扎德')

    Talk(
        (
            '#0030440735V#027F（呼～来了吗……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440736V（是要我放手一搏\n',
            '追求最强的牌组吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)

    Return()

# id: 0x000F offset: 0x427F
@scena.Code('func_0F_427F')
def func_0F_427F():
    FadeOut(300, 0, 100)
    OP_C5(0x00, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x01, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x02, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x03, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x04, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 100, 320, 200, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 400, 320, 500, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 100, 0, 200, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 0, 320, 100, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 300, 0, 400, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C6(0x05, 0x03, -1, 400, 0)
    OP_C6(0x06, 0x03, -1, 400, 0)
    OP_C6(0x07, 0x03, -1, 400, 0)
    OP_C6(0x08, 0x03, -1, 400, 0)
    OP_C6(0x09, 0x03, -1, 400, 0)
    Sleep(1000)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4804',
    )

    OP_C6(0x09, 0x00, 1048000, 240000, 500)
    Sleep(24)

    PlaySE(254, 0x00, 0x64)
    OP_C6(0x06, 0x00, 843000, 234000, 500)
    Sleep(24)

    OP_C6(0x05, 0x00, 763000, 232000, 500)
    Sleep(24)

    OP_C7(0x00, 0x05, 0x00)
    OP_C7(0x00, 0x06, 0x00)
    OP_C7(0x00, 0x09, 0x00)
    OP_C7(0x01, 0x05, 0x00)
    OP_C7(0x01, 0x06, 0x00)
    OP_C7(0x01, 0x09, 0x00)
    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 200, 320, 300, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 400, 0, 500, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 200, 320, 300, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C6(0x00, 0x00, 163000, -160000, 0)
    OP_C6(0x01, 0x00, 243000, -160000, 0)
    OP_C6(0x04, 0x00, 483000, -160000, 0)
    OP_C6(0x00, 0x01, 1000, 1000, 0)
    OP_C6(0x01, 0x01, 1000, 1000, 0)
    OP_C6(0x04, 0x01, 1000, 1000, 0)
    OP_C6(0x00, 0x03, -1, 0, 0)
    OP_C6(0x01, 0x03, -1, 0, 0)
    OP_C6(0x04, 0x03, -1, 0, 0)
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x01, 0x04, 0, 0, 0)
    OP_C6(0x07, 0x04, 0, 0, 0)
    OP_C6(0x08, 0x04, 0, 0, 0)
    OP_C6(0x04, 0x04, 0, 0, 0)
    Sleep(400)

    OP_C6(0x00, 0x00, 163000, 232000, 200)
    Sleep(124)

    PlaySE(254, 0x00, 0x64)
    OP_C6(0x01, 0x00, 243000, 234000, 200)
    Sleep(124)

    OP_C6(0x04, 0x00, 483000, 240000, 200)
    Sleep(124)

    OP_C7(0x00, 0x04, 0x00)
    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('雪拉扎德')

    Talk(
        (
            '#0030440737V#022F（……怎么办？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    CreateThread(0x0019, 0x01, 0x02, 0x001D)
    Sleep(100)

    OP_C6(0x05, 0x04, 0, 0, 0)
    CreateThread(0x0019, 0x02, 0x02, 0x001E)
    Sleep(100)

    OP_C6(0x06, 0x04, 0, 0, 0)
    OP_C6(0x07, 0x04, 0, 0, 0)
    OP_C6(0x08, 0x04, 0, 0, 0)
    CreateThread(0x001A, 0x02, 0x02, 0x0021)
    Sleep(100)

    OP_C6(0x09, 0x04, 0, 0, 0)
    WaitForThreadExit(0x001A, 0x0002)
    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('雪拉扎德')

    Talk(
        (
            '#0030440738V#026F（……要停止吗。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440739V#022F（就算用秘技，\n',
            '这里开始凑成３条已经是极限了。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440740V（能不能取胜，\n',
            '之后就看对方的手牌了吧……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_4A88')

    def _loc_4804(): pass

    label('loc_4804')

    OP_C6(0x09, 0x00, 1048000, 240000, 500)
    Sleep(24)

    PlaySE(254, 0x00, 0x64)
    OP_C6(0x07, 0x00, 923000, 236000, 500)
    Sleep(24)

    OP_C7(0x00, 0x07, 0x00)
    OP_C7(0x01, 0x09, 0x00)
    OP_C7(0x01, 0x07, 0x00)
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 200, 320, 300, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 400, 0, 500, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C6(0x02, 0x00, 323000, -160000, 0)
    OP_C6(0x04, 0x00, 483000, -160000, 0)
    OP_C6(0x02, 0x01, 1000, 1000, 0)
    OP_C6(0x04, 0x01, 1000, 1000, 0)
    OP_C6(0x02, 0x03, -1, 0, 0)
    OP_C6(0x04, 0x03, -1, 0, 0)
    OP_C6(0x05, 0x04, 0, 0, 0)
    OP_C6(0x06, 0x04, 0, 0, 0)
    OP_C6(0x02, 0x04, 0, 0, 0)
    OP_C6(0x08, 0x04, 0, 0, 0)
    OP_C6(0x04, 0x04, 0, 0, 0)
    OP_C6(0x02, 0x00, 323000, 236000, 200)
    Sleep(124)

    PlaySE(254, 0x00, 0x64)
    OP_C6(0x04, 0x00, 483000, 240000, 200)
    Sleep(124)

    OP_C7(0x00, 0x04, 0x00)
    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('雪拉扎德')

    Talk(
        (
            '#0030440741V#022F（……怎么办？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    CreateThread(0x0019, 0x03, 0x02, 0x001F)
    Sleep(100)

    OP_C6(0x07, 0x04, 0, 0, 0)
    OP_C6(0x08, 0x04, 0, 0, 0)
    CreateThread(0x001A, 0x02, 0x02, 0x0021)
    Sleep(100)

    OP_C6(0x09, 0x04, 0, 0, 0)
    WaitForThreadExit(0x001A, 0x0002)
    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('雪拉扎德')

    Talk(
        (
            '#0030440742V#022F（……好，就这样。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440743V#026F（还需要１张……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440744V（呼，就祈祷手指\n',
            '的感觉没衰退吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_4A88(): pass

    label('loc_4A88')

    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)

    Return()

# id: 0x0010 offset: 0x4B30
@scena.Code('func_10_4B30')
def func_10_4B30():
    FadeOut(300, 0, 100)
    OP_C5(0x00, -50, -80, 50, 80, 483, 240, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x01, -50, -80, 50, 80, 481, 238, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x02, -50, -80, 50, 80, 479, 236, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x03, -50, -80, 50, 80, 477, 234, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x04, -50, -80, 50, 80, 475, 232, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C6(0x00, 0x03, -1, 400, 0)
    OP_C6(0x01, 0x03, -1, 400, 0)
    OP_C6(0x02, 0x03, -1, 400, 0)
    OP_C6(0x03, 0x03, -1, 400, 0)
    OP_C6(0x04, 0x03, -1, 400, 0)
    OP_C7(0x00, 0x04, 0x03)
    OP_C6(0x00, 0x00, 163000, 232000, 400)
    OP_C6(0x01, 0x00, 161000, 230000, 400)
    OP_C6(0x02, 0x00, 159000, 228000, 400)
    OP_C6(0x03, 0x00, 157000, 226000, 400)
    OP_C6(0x04, 0x00, 155000, 224000, 400)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x01, 0x00, 243000, 234000, 50)
    OP_C6(0x02, 0x00, 241000, 232000, 50)
    OP_C6(0x03, 0x00, 239000, 230000, 50)
    OP_C6(0x04, 0x00, 237000, 228000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x02, 0x00, 323000, 236000, 50)
    OP_C6(0x03, 0x00, 321000, 234000, 50)
    OP_C6(0x04, 0x00, 319000, 232000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x03, 0x00, 403000, 238000, 50)
    OP_C6(0x04, 0x00, 401000, 236000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x04, 0x00, 483000, 240000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 400, 0, 500, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 0, 160, 100, 320, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 300, 0, 400, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 100, 0, 200, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    CreateThread(0x0019, 0x01, 0x02, 0x001D)
    Sleep(100)

    CreateThread(0x0019, 0x02, 0x02, 0x001E)
    Sleep(100)

    CreateThread(0x0019, 0x03, 0x02, 0x001F)
    Sleep(100)

    CreateThread(0x001A, 0x01, 0x02, 0x0020)
    Sleep(100)

    CreateThread(0x001A, 0x02, 0x02, 0x0021)
    WaitForThreadExit(0x001A, 0x0002)
    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010440745V#1007F如你所见……\n',
            '是方块同花哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)

    Return()

# id: 0x0011 offset: 0x4F65
@scena.Code('func_11_4F65')
def func_11_4F65():
    FadeOut(300, 0, 100)
    OP_C5(0x00, -50, -80, 50, 80, 483, 240, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x01, -50, -80, 50, 80, 481, 238, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x02, -50, -80, 50, 80, 479, 236, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x03, -50, -80, 50, 80, 477, 234, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x04, -50, -80, 50, 80, 475, 232, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C6(0x00, 0x03, -1, 400, 0)
    OP_C6(0x01, 0x03, -1, 400, 0)
    OP_C6(0x02, 0x03, -1, 400, 0)
    OP_C6(0x03, 0x03, -1, 400, 0)
    OP_C6(0x04, 0x03, -1, 400, 0)
    OP_C7(0x00, 0x04, 0x03)
    OP_C6(0x00, 0x00, 163000, 232000, 400)
    OP_C6(0x01, 0x00, 161000, 230000, 400)
    OP_C6(0x02, 0x00, 159000, 228000, 400)
    OP_C6(0x03, 0x00, 157000, 226000, 400)
    OP_C6(0x04, 0x00, 155000, 224000, 400)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x01, 0x00, 243000, 234000, 50)
    OP_C6(0x02, 0x00, 241000, 232000, 50)
    OP_C6(0x03, 0x00, 239000, 230000, 50)
    OP_C6(0x04, 0x00, 237000, 228000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x02, 0x00, 323000, 236000, 50)
    OP_C6(0x03, 0x00, 321000, 234000, 50)
    OP_C6(0x04, 0x00, 319000, 232000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x03, 0x00, 403000, 238000, 50)
    OP_C6(0x04, 0x00, 401000, 236000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x04, 0x00, 483000, 240000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 200, 320, 300, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 400, 0, 500, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 100, 0, 200, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 0, 320, 100, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 200, 320, 300, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    CreateThread(0x0019, 0x01, 0x02, 0x001D)
    Sleep(100)

    CreateThread(0x0019, 0x02, 0x02, 0x001E)
    Sleep(100)

    CreateThread(0x0019, 0x03, 0x02, 0x001F)
    Sleep(100)

    CreateThread(0x001A, 0x01, 0x02, 0x0020)
    Sleep(100)

    CreateThread(0x001A, 0x02, 0x02, 0x0021)
    WaitForThreadExit(0x001A, 0x0002)
    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('雪拉扎德')

    Talk(
        (
            '#0030440746V#026F我这里Ａ一对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)

    Return()

# id: 0x0012 offset: 0x538C
@scena.Code('func_12_538C')
def func_12_538C():
    FadeOut(300, 0, 100)
    OP_C5(0x00, -50, -80, 50, 80, 483, 240, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x01, -50, -80, 50, 80, 481, 238, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x02, -50, -80, 50, 80, 479, 236, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x03, -50, -80, 50, 80, 477, 234, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x04, -50, -80, 50, 80, 475, 232, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C6(0x00, 0x03, -1, 400, 0)
    OP_C6(0x01, 0x03, -1, 400, 0)
    OP_C6(0x02, 0x03, -1, 400, 0)
    OP_C6(0x03, 0x03, -1, 400, 0)
    OP_C6(0x04, 0x03, -1, 400, 0)
    OP_C7(0x00, 0x04, 0x03)
    OP_C6(0x00, 0x00, 163000, 232000, 400)
    OP_C6(0x01, 0x00, 161000, 230000, 400)
    OP_C6(0x02, 0x00, 159000, 228000, 400)
    OP_C6(0x03, 0x00, 157000, 226000, 400)
    OP_C6(0x04, 0x00, 155000, 224000, 400)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x01, 0x00, 243000, 234000, 50)
    OP_C6(0x02, 0x00, 241000, 232000, 50)
    OP_C6(0x03, 0x00, 239000, 230000, 50)
    OP_C6(0x04, 0x00, 237000, 228000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x02, 0x00, 323000, 236000, 50)
    OP_C6(0x03, 0x00, 321000, 234000, 50)
    OP_C6(0x04, 0x00, 319000, 232000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x03, 0x00, 403000, 238000, 50)
    OP_C6(0x04, 0x00, 401000, 236000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x04, 0x00, 483000, 240000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 400, 320, 500, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 100, 320, 200, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 0, 320, 100, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 200, 320, 300, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 300, 320, 400, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    CreateThread(0x0019, 0x01, 0x02, 0x001D)
    Sleep(1000)

    CreateThread(0x0019, 0x02, 0x02, 0x001E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5703',
    )

    Sleep(24)

    ChrTurnDirection(0x000D, 0x0101, 0)
    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0030440747V#1011F嘿～竟然\n',
            '来了这么特别的牌……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_5756')

    def _loc_5703(): pass

    label('loc_5703')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_5756',
    )

    Sleep(24)

    ChrTurnDirection(0x000D, 0x0103, 0)
    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('雪拉扎德')

    Talk(
        (
            '#0030440748V#026F我记得……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_5756(): pass

    label('loc_5756')

    OP_59()
    CreateThread(0x0019, 0x03, 0x02, 0x001F)
    Sleep(24)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_57C3',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0030440749V#1015F……………………………\n',
            '……嗯嗯……………？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_5815')

    def _loc_57C3(): pass

    label('loc_57C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_5815',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('雪拉扎德')

    Talk(
        (
            '#0030440750V#027F这次游戏\n',
            '花色的强弱也算在内对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_5815(): pass

    label('loc_5815')

    OP_59()
    CreateThread(0x001A, 0x01, 0x02, 0x0020)
    Sleep(24)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_587E',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0030440751V#1004F这、这个……………\n',
            '难不成……………！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_58D0')

    def _loc_587E(): pass

    label('loc_587E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_58D0',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('雪拉扎德')

    Talk(
        (
            '#0030440752V#027F那么、你的牌组\n',
            '还不能说是最强……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_58D0(): pass

    label('loc_58D0')

    OP_59()
    OP_C6(0x04, 0x01, 100, 1000, 300)
    OP_C7(0x00, 0x04, 0x01)
    PlaySE(256, 0x00, 0x64)
    OP_C6(0x09, 0x01, 100, 1000, 0)
    OP_C6(0x09, 0x03, -1, 0, 0)
    OP_C6(0x09, 0x01, 1000, 1000, 300)
    OP_C6(0x04, 0x03, 16777215, 0, 0)
    OP_C7(0x00, 0x09, 0x01)
    Sleep(1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_599D',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0030440753V#1004F不、不会吧…………！？\n',
            '是黑桃同花大顺哦。',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_5A1D')

    def _loc_599D(): pass

    label('loc_599D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_5A1D',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('雪拉扎德')

    Talk(
        (
            '#0030440754V#026F和这边一样是\n',
            '同花大顺……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030440755V#027F不过黑桃女王……\n',
            '看来是对我微笑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_5A1D(): pass

    label('loc_5A1D')

    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)

    Return()

# id: 0x0013 offset: 0x5AC5
@scena.Code('func_13_5AC5')
def func_13_5AC5():
    FadeOut(300, 0, 100)
    OP_C5(0x00, -50, -80, 50, 80, 483, 240, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x01, -50, -80, 50, 80, 481, 238, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x02, -50, -80, 50, 80, 479, 236, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x03, -50, -80, 50, 80, 477, 234, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x04, -50, -80, 50, 80, 475, 232, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C6(0x00, 0x03, -1, 400, 0)
    OP_C6(0x01, 0x03, -1, 400, 0)
    OP_C6(0x02, 0x03, -1, 400, 0)
    OP_C6(0x03, 0x03, -1, 400, 0)
    OP_C6(0x04, 0x03, -1, 400, 0)
    OP_C7(0x00, 0x04, 0x03)
    OP_C6(0x00, 0x00, 163000, 232000, 400)
    OP_C6(0x01, 0x00, 161000, 230000, 400)
    OP_C6(0x02, 0x00, 159000, 228000, 400)
    OP_C6(0x03, 0x00, 157000, 226000, 400)
    OP_C6(0x04, 0x00, 155000, 224000, 400)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x01, 0x00, 243000, 234000, 50)
    OP_C6(0x02, 0x00, 241000, 232000, 50)
    OP_C6(0x03, 0x00, 239000, 230000, 50)
    OP_C6(0x04, 0x00, 237000, 228000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x02, 0x00, 323000, 236000, 50)
    OP_C6(0x03, 0x00, 321000, 234000, 50)
    OP_C6(0x04, 0x00, 319000, 232000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x03, 0x00, 403000, 238000, 50)
    OP_C6(0x04, 0x00, 401000, 236000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x04, 0x00, 483000, 240000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 100, 160, 200, 320, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 400, 160, 500, 320, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 200, 160, 300, 320, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 300, 160, 400, 320, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 100, 0, 200, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    CreateThread(0x0019, 0x01, 0x02, 0x001D)
    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('菲利奥')

    Talk(
        (
            '#3130440756V咕、咕噜……（吞口水）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    CreateThread(0x0019, 0x02, 0x02, 0x001E)
    Sleep(24)

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('菲利奥')

    Talk(
        (
            '#3130440757V好了～～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    CreateThread(0x0019, 0x03, 0x02, 0x001F)
    Sleep(24)

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('菲利奥')

    Talk(
        (
            '#3130440758V来吧～～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    CreateThread(0x001A, 0x01, 0x02, 0x0020)
    Sleep(24)

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('菲利奥')

    Talk(
        (
            '#3130440759V来、来吧～～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x04, 0x01, 100, 1000, 300)
    OP_C7(0x00, 0x04, 0x01)
    PlaySE(256, 0x00, 0x64)
    OP_C6(0x09, 0x01, 100, 1000, 0)
    OP_C6(0x09, 0x03, -1, 0, 0)
    OP_C6(0x09, 0x01, 1000, 1000, 300)
    OP_C6(0x04, 0x03, 16777215, 0, 0)
    OP_C7(0x00, 0x09, 0x01)
    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('菲利奥')

    Talk(
        (
            '#3130440760V真、真的来了！！！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('菲利奥')

    Talk(
        (
            '#3130440761V看、看啊！\n',
            '是同花大顺！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)

    Return()

# id: 0x0014 offset: 0x604C
@scena.Code('func_14_604C')
def func_14_604C():
    FadeOut(300, 0, 100)
    OP_C5(0x00, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x01, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x02, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x03, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x04, -50, -80, 50, 80, -50, -10, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_621E',
    )

    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 0, 320, 100, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 200, 0, 300, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 300, 0, 400, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 200, 0, 300, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 100, 0, 200, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')

    Jump('loc_62FA')

    def _loc_621E(): pass

    label('loc_621E')

    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 0, 320, 100, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 200, 0, 300, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 400, 0, 500, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 100, 0, 200, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 300, 0, 400, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')

    def _loc_62FA(): pass

    label('loc_62FA')

    OP_C6(0x05, 0x03, -1, 400, 0)
    OP_C6(0x06, 0x03, -1, 400, 0)
    OP_C6(0x07, 0x03, -1, 400, 0)
    OP_C6(0x08, 0x03, -1, 400, 0)
    OP_C6(0x09, 0x03, -1, 400, 0)
    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_29(0x0068, 0x01, 0x0008)"),
            (Expr.Eval, "OP_29(0x0068, 0x01, 0x0040)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_6424',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('奥利维尔')

    Talk(
        (
            '#0040440762V#030F（对手的沉默\n',
            '  实在是令人紧张啊……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440763V（但已经不能放弃了，\n',
            '现在只能孤注一掷比下去了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
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
            TXT(0x00, '【比牌】\n'),
        ),
    )

    MenuEnd(0x0003)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)

    Jump('loc_64E3')

    def _loc_6424(): pass

    label('loc_6424')

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('奥利维尔')

    Talk(
        (
            '#0040440764V#030F（对手的沉默\n',
            '  实在是令人紧张啊……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440765V（唔，那么接下来\n',
            '  应该怎么做呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
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
            TXT(0x00, '【比牌】\n'),
            TXT(0x01, '【放弃】\n'),
        ),
    )

    MenuEnd(0x0003)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)

    def _loc_64E3(): pass

    label('loc_64E3')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6577',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('奥利维尔')

    Talk(
        (
            '#0040440766V#030F（对手放弃过一次，\n',
            '　这次必定要比了。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440767V（追逼负伤的野兽\n',
            '  实在是很危险……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_65FB')

    def _loc_6577(): pass

    label('loc_6577')

    If(
        (
            (Expr.Eval, "OP_29(0x0068, 0x01, 0x0008)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0068, 0x01, 0x0040)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_65FB',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('奥利维尔')

    Talk(
        (
            '#0040440768V#030F（理论上\n',
            '  也可以放弃……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040440769V（不过这里还是顽强进逼吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_65FB(): pass

    label('loc_65FB')

    OP_59()
    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)

    Return()

# id: 0x0015 offset: 0x66A4
@scena.Code('func_15_66A4')
def func_15_66A4():
    FadeOut(300, 0, 100)
    OP_C5(0x00, -50, -80, 50, 80, 483, 240, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x01, -50, -80, 50, 80, 481, 238, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x02, -50, -80, 50, 80, 479, 236, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x03, -50, -80, 50, 80, 477, 234, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x04, -50, -80, 50, 80, 475, 232, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C6(0x00, 0x03, -1, 400, 0)
    OP_C6(0x01, 0x03, -1, 400, 0)
    OP_C6(0x02, 0x03, -1, 400, 0)
    OP_C6(0x03, 0x03, -1, 400, 0)
    OP_C6(0x04, 0x03, -1, 400, 0)
    OP_C7(0x00, 0x04, 0x03)
    OP_C6(0x00, 0x00, 163000, 232000, 400)
    OP_C6(0x01, 0x00, 161000, 230000, 400)
    OP_C6(0x02, 0x00, 159000, 228000, 400)
    OP_C6(0x03, 0x00, 157000, 226000, 400)
    OP_C6(0x04, 0x00, 155000, 224000, 400)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x01, 0x00, 243000, 234000, 50)
    OP_C6(0x02, 0x00, 241000, 232000, 50)
    OP_C6(0x03, 0x00, 239000, 230000, 50)
    OP_C6(0x04, 0x00, 237000, 228000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x02, 0x00, 323000, 236000, 50)
    OP_C6(0x03, 0x00, 321000, 234000, 50)
    OP_C6(0x04, 0x00, 319000, 232000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x03, 0x00, 403000, 238000, 50)
    OP_C6(0x04, 0x00, 401000, 236000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x04, 0x00, 483000, 240000, 50)
    OP_C7(0x00, 0x04, 0x00)

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_69BA',
    )

    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 0, 320, 100, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 200, 0, 300, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 300, 0, 400, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 200, 0, 300, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 100, 0, 200, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')

    Jump('loc_6A96')

    def _loc_69BA(): pass

    label('loc_69BA')

    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 0, 320, 100, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 200, 0, 300, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 400, 0, 500, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 100, 0, 200, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 300, 0, 400, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')

    def _loc_6A96(): pass

    label('loc_6A96')

    CreateThread(0x0019, 0x01, 0x02, 0x001D)
    Sleep(100)

    CreateThread(0x0019, 0x02, 0x02, 0x001E)
    Sleep(100)

    CreateThread(0x0019, 0x03, 0x02, 0x001F)
    Sleep(100)

    CreateThread(0x001A, 0x01, 0x02, 0x0020)
    Sleep(100)

    CreateThread(0x001A, 0x02, 0x02, 0x0021)
    WaitForThreadExit(0x001A, 0x0002)
    Sleep(1000)

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6B1F',
    )

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('奥利维尔')

    Talk(
        (
            '#0040440770V#035F呼、４和６吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Jump('loc_6B53')

    def _loc_6B1F(): pass

    label('loc_6B1F')

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('奥利维尔')

    Talk(
        (
            '#0040440771V#035F呼，４啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_6B53(): pass

    label('loc_6B53')

    OP_59()
    OP_C6(0x00, 0x00, 663000, 240000, 0)
    OP_C6(0x01, 0x00, 763000, 238000, 0)
    OP_C6(0x02, 0x00, 863000, 236000, 0)
    OP_C6(0x03, 0x00, 963000, 234000, 0)
    OP_C6(0x04, 0x00, 1063000, 232000, 0)
    OP_C6(0x00, 0x01, 1000, 1000, 0)
    OP_C6(0x01, 0x01, 1000, 1000, 0)
    OP_C6(0x02, 0x01, 1000, 1000, 0)
    OP_C6(0x03, 0x01, 1000, 1000, 0)
    OP_C6(0x04, 0x01, 1000, 1000, 0)
    OP_C6(0x00, 0x03, -1, 0, 0)
    OP_C6(0x01, 0x03, -1, 0, 0)
    OP_C6(0x02, 0x03, -1, 0, 0)
    OP_C6(0x03, 0x03, -1, 0, 0)
    OP_C6(0x04, 0x03, -1, 0, 0)
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x01, 0x04, 0, 0, 0)
    OP_C6(0x02, 0x04, 0, 0, 0)
    OP_C6(0x03, 0x04, 0, 0, 0)
    OP_C6(0x04, 0x04, 0, 0, 0)
    OP_C6(0x05, 0x00, -443000, 232000, 500)
    OP_C6(0x06, 0x00, -343000, 234000, 500)
    OP_C6(0x07, 0x00, -243000, 236000, 500)
    OP_C6(0x08, 0x00, -143000, 238000, 500)
    OP_C6(0x09, 0x00, -43000, 240000, 500)
    OP_C6(0x00, 0x00, 163000, 232000, 500)
    OP_C6(0x01, 0x00, 243000, 234000, 500)
    OP_C6(0x02, 0x00, 323000, 236000, 500)
    OP_C6(0x03, 0x00, 403000, 238000, 500)
    OP_C6(0x04, 0x00, 483000, 240000, 500)
    OP_C7(0x00, 0x09, 0x00)
    OP_C7(0x00, 0x04, 0x00)
    OP_C7(0x01, 0x09, 0x00)
    OP_C7(0x01, 0x08, 0x00)
    OP_C7(0x01, 0x07, 0x00)
    OP_C7(0x01, 0x06, 0x00)
    OP_C7(0x01, 0x05, 0x00)
    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('菲利奥')

    Talk(
        (
            '#0040440772V嘿嘿，用这种牌决胜\n',
            '实在是鲁莽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 100, 0, 200, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 0, 320, 100, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 100, 320, 200, 480, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 300, 0, 400, 160, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    CreateThread(0x0019, 0x01, 0x02, 0x001D)
    Sleep(100)

    CreateThread(0x0019, 0x02, 0x02, 0x001E)
    Sleep(100)

    CreateThread(0x0019, 0x03, 0x02, 0x001F)
    Sleep(100)

    CreateThread(0x001A, 0x01, 0x02, 0x0020)
    Sleep(100)

    CreateThread(0x001A, 0x02, 0x02, 0x0021)
    WaitForThreadExit(0x001A, 0x0002)
    ChrTurnDirection(0x000B, 0x000D, 0)
    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('菲利奥')

    Talk(
        (
            '#0040440773V三条Ａ……\n',
            '呼呼呼，看来胜负已定了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)

    Return()

# id: 0x0016 offset: 0x6F88
@scena.Code('func_16_6F88')
def func_16_6F88():
    FadeOut(300, 0, 100)
    OP_C5(0x00, -50, -80, 50, 80, 483, 240, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x01, -50, -80, 50, 80, 481, 238, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x02, -50, -80, 50, 80, 479, 236, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x03, -50, -80, 50, 80, 477, 234, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x04, -50, -80, 50, 80, 475, 232, 512, 512, 0, 0, 100, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C6(0x00, 0x03, -1, 400, 0)
    OP_C6(0x01, 0x03, -1, 400, 0)
    OP_C6(0x02, 0x03, -1, 400, 0)
    OP_C6(0x03, 0x03, -1, 400, 0)
    OP_C6(0x04, 0x03, -1, 400, 0)
    OP_C7(0x00, 0x04, 0x03)
    OP_C6(0x00, 0x00, 163000, 232000, 400)
    OP_C6(0x01, 0x00, 161000, 230000, 400)
    OP_C6(0x02, 0x00, 159000, 228000, 400)
    OP_C6(0x03, 0x00, 157000, 226000, 400)
    OP_C6(0x04, 0x00, 155000, 224000, 400)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x01, 0x00, 243000, 234000, 50)
    OP_C6(0x02, 0x00, 241000, 232000, 50)
    OP_C6(0x03, 0x00, 239000, 230000, 50)
    OP_C6(0x04, 0x00, 237000, 228000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x02, 0x00, 323000, 236000, 50)
    OP_C6(0x03, 0x00, 321000, 234000, 50)
    OP_C6(0x04, 0x00, 319000, 232000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x03, 0x00, 403000, 238000, 50)
    OP_C6(0x04, 0x00, 401000, 236000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C6(0x04, 0x00, 483000, 240000, 50)
    OP_C7(0x00, 0x04, 0x00)
    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 0, 160, 100, 320, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 200, 0, 300, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 300, 160, 400, 320, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 200, 320, 300, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 300, 0, 400, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    CreateThread(0x0019, 0x01, 0x02, 0x001D)
    Sleep(100)

    CreateThread(0x0019, 0x02, 0x02, 0x001E)
    Sleep(100)

    CreateThread(0x0019, 0x03, 0x02, 0x001F)
    Sleep(100)

    CreateThread(0x001A, 0x01, 0x02, 0x0020)
    Sleep(100)

    CreateThread(0x001A, 0x02, 0x02, 0x0021)
    WaitForThreadExit(0x001A, 0x0002)
    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('艾丝蒂尔')

    Talk(
        (
            '#0010440774V#1007F呜……我没任何牌型。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_59()
    OP_C6(0x00, 0x00, 663000, 240000, 0)
    OP_C6(0x01, 0x00, 763000, 238000, 0)
    OP_C6(0x02, 0x00, 863000, 236000, 0)
    OP_C6(0x03, 0x00, 963000, 234000, 0)
    OP_C6(0x04, 0x00, 1063000, 232000, 0)
    OP_C6(0x00, 0x01, 1000, 1000, 0)
    OP_C6(0x01, 0x01, 1000, 1000, 0)
    OP_C6(0x02, 0x01, 1000, 1000, 0)
    OP_C6(0x03, 0x01, 1000, 1000, 0)
    OP_C6(0x04, 0x01, 1000, 1000, 0)
    OP_C6(0x00, 0x03, -1, 0, 0)
    OP_C6(0x01, 0x03, -1, 0, 0)
    OP_C6(0x02, 0x03, -1, 0, 0)
    OP_C6(0x03, 0x03, -1, 0, 0)
    OP_C6(0x04, 0x03, -1, 0, 0)
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x01, 0x04, 0, 0, 0)
    OP_C6(0x02, 0x04, 0, 0, 0)
    OP_C6(0x03, 0x04, 0, 0, 0)
    OP_C6(0x04, 0x04, 0, 0, 0)
    OP_C6(0x05, 0x00, -443000, 232000, 500)
    OP_C6(0x06, 0x00, -343000, 234000, 500)
    OP_C6(0x07, 0x00, -243000, 236000, 500)
    OP_C6(0x08, 0x00, -143000, 238000, 500)
    OP_C6(0x09, 0x00, -43000, 240000, 500)
    OP_C6(0x00, 0x00, 163000, 232000, 500)
    OP_C6(0x01, 0x00, 243000, 234000, 500)
    OP_C6(0x02, 0x00, 323000, 236000, 500)
    OP_C6(0x03, 0x00, 403000, 238000, 500)
    OP_C6(0x04, 0x00, 483000, 240000, 500)
    OP_C7(0x00, 0x09, 0x00)
    OP_C7(0x00, 0x04, 0x00)
    OP_C7(0x01, 0x09, 0x00)
    OP_C7(0x01, 0x08, 0x00)
    OP_C7(0x01, 0x07, 0x00)
    OP_C7(0x01, 0x06, 0x00)
    OP_C7(0x01, 0x05, 0x00)
    OP_C5(0x05, -50, -80, 50, 80, 163, 232, 512, 512, 0, 160, 100, 320, 0x00FFFFFF, 0x00, 'C_VIS229._CH')
    OP_C5(0x06, -50, -80, 50, 80, 243, 234, 512, 512, 200, 160, 300, 320, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x07, -50, -80, 50, 80, 323, 236, 512, 512, 100, 320, 200, 480, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x08, -50, -80, 50, 80, 403, 238, 512, 512, 100, 160, 200, 320, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    OP_C5(0x09, -50, -80, 50, 80, 483, 240, 512, 512, 200, 0, 300, 160, 0x00FFFFFF, 0x00, 'C_VIS228._CH')
    CreateThread(0x0019, 0x01, 0x02, 0x001D)
    Sleep(100)

    CreateThread(0x0019, 0x02, 0x02, 0x001E)
    Sleep(100)

    CreateThread(0x0019, 0x03, 0x02, 0x001F)
    Sleep(100)

    CreateThread(0x001A, 0x01, 0x02, 0x0020)
    Sleep(100)

    CreateThread(0x001A, 0x02, 0x02, 0x0021)
    WaitForThreadExit(0x001A, 0x0002)
    Sleep(1000)

    SetMessageWindowPos(-1, 320, -1, -1)
    TalkSetChrName('菲利奥')

    Talk(
        (
            '#0010440775V我的是Ｊ一对。\n',
            '呼～险胜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Call(2, 0x0017)
    OP_C7(0x01, 0xFF, 0x00)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    OP_C6(0x04, 0x06, 0, 0, 0)
    OP_C6(0x05, 0x06, 0, 0, 0)
    OP_C6(0x06, 0x06, 0, 0, 0)
    OP_C6(0x07, 0x06, 0, 0, 0)
    OP_C6(0x08, 0x06, 0, 0, 0)
    OP_C6(0x09, 0x06, 0, 0, 0)
    FadeIn(300, 0)

    Return()

# id: 0x0017 offset: 0x76F0
@scena.Code('func_17_76F0')
def func_17_76F0():
    OP_C6(0x00, 0x00, 163000, 232000, 0)
    OP_C6(0x01, 0x00, 243000, 234000, 0)
    OP_C6(0x02, 0x00, 323000, 236000, 0)
    OP_C6(0x03, 0x00, 403000, 238000, 0)
    OP_C6(0x04, 0x00, 483000, 240000, 0)
    OP_C6(0x00, 0x03, 16777215, 0, 0)
    OP_C6(0x01, 0x03, 16777215, 0, 0)
    OP_C6(0x02, 0x03, 16777215, 0, 0)
    OP_C6(0x03, 0x03, 16777215, 0, 0)
    OP_C6(0x04, 0x03, 16777215, 0, 0)
    OP_C6(0x00, 0x01, 1000, 1000, 0)
    OP_C6(0x01, 0x01, 1000, 1000, 0)
    OP_C6(0x02, 0x01, 1000, 1000, 0)
    OP_C6(0x03, 0x01, 1000, 1000, 0)
    OP_C6(0x04, 0x01, 1000, 1000, 0)
    OP_C6(0x04, 0x04, 0, 0, 0)
    OP_C6(0x03, 0x04, 0, 0, 0)
    OP_C6(0x02, 0x04, 0, 0, 0)
    OP_C6(0x01, 0x04, 0, 0, 0)
    OP_C6(0x00, 0x04, 0, 0, 0)
    CreateThread(0x0019, 0x01, 0x02, 0x0018)
    Sleep(24)

    CreateThread(0x0019, 0x02, 0x02, 0x0019)
    Sleep(24)

    CreateThread(0x0019, 0x03, 0x02, 0x001A)
    Sleep(24)

    CreateThread(0x001A, 0x01, 0x02, 0x001B)
    Sleep(24)

    CreateThread(0x001A, 0x02, 0x02, 0x001C)
    WaitForThreadExit(0x001A, 0x0002)
    OP_C6(0x00, 0x03, 16777215, 400, 0)
    Sleep(24)

    OP_C6(0x01, 0x03, 16777215, 400, 0)
    Sleep(24)

    OP_C6(0x02, 0x03, 16777215, 400, 0)
    Sleep(24)

    OP_C6(0x03, 0x03, 16777215, 400, 0)
    Sleep(24)

    OP_C6(0x04, 0x03, 16777215, 400, 0)
    OP_C7(0x00, 0x00, 0x03)
    OP_C7(0x00, 0x01, 0x03)
    OP_C7(0x00, 0x02, 0x03)
    OP_C7(0x00, 0x03, 0x03)
    OP_C7(0x00, 0x04, 0x03)

    Return()

# id: 0x0018 offset: 0x78CC
@scena.Code('func_18_78CC')
def func_18_78CC():
    OP_C6(0x05, 0x01, 100, 1000, 100)
    OP_C7(0x00, 0x05, 0x01)
    PlaySE(256, 0x00, 0x64)
    OP_C6(0x00, 0x01, 100, 1000, 0)
    OP_C6(0x00, 0x03, -1, 0, 0)
    OP_C6(0x00, 0x01, 1000, 1000, 100)
    OP_C6(0x05, 0x03, 16777215, 0, 0)

    Return()

# id: 0x0019 offset: 0x7921
@scena.Code('func_19_7921')
def func_19_7921():
    OP_C6(0x06, 0x01, 100, 1000, 100)
    OP_C7(0x00, 0x06, 0x01)
    PlaySE(256, 0x00, 0x64)
    OP_C6(0x01, 0x01, 100, 1000, 0)
    OP_C6(0x01, 0x03, -1, 0, 0)
    OP_C6(0x01, 0x01, 1000, 1000, 100)
    OP_C6(0x06, 0x03, 16777215, 0, 0)

    Return()

# id: 0x001A offset: 0x7976
@scena.Code('func_1A_7976')
def func_1A_7976():
    OP_C6(0x07, 0x01, 100, 1000, 100)
    OP_C7(0x00, 0x07, 0x01)
    PlaySE(256, 0x00, 0x64)
    OP_C6(0x02, 0x01, 100, 1000, 0)
    OP_C6(0x02, 0x03, -1, 0, 0)
    OP_C6(0x02, 0x01, 1000, 1000, 100)
    OP_C6(0x07, 0x03, 16777215, 0, 0)

    Return()

# id: 0x001B offset: 0x79CB
@scena.Code('func_1B_79CB')
def func_1B_79CB():
    OP_C6(0x08, 0x01, 100, 1000, 100)
    OP_C7(0x00, 0x08, 0x01)
    PlaySE(256, 0x00, 0x64)
    OP_C6(0x03, 0x01, 100, 1000, 0)
    OP_C6(0x03, 0x03, -1, 0, 0)
    OP_C6(0x03, 0x01, 1000, 1000, 100)
    OP_C6(0x08, 0x03, 16777215, 0, 0)

    Return()

# id: 0x001C offset: 0x7A20
@scena.Code('func_1C_7A20')
def func_1C_7A20():
    OP_C6(0x09, 0x01, 100, 1000, 100)
    OP_C7(0x00, 0x09, 0x01)
    PlaySE(256, 0x00, 0x64)
    OP_C6(0x04, 0x01, 100, 1000, 0)
    OP_C6(0x04, 0x03, -1, 0, 0)
    OP_C6(0x04, 0x01, 1000, 1000, 100)
    OP_C6(0x09, 0x03, 16777215, 0, 0)

    Return()

# id: 0x001D offset: 0x7A75
@scena.Code('func_1D_7A75')
def func_1D_7A75():
    OP_C6(0x00, 0x01, 100, 1000, 100)
    OP_C7(0x00, 0x00, 0x01)
    PlaySE(256, 0x00, 0x64)
    OP_C6(0x05, 0x01, 100, 1000, 0)
    OP_C6(0x05, 0x03, -1, 0, 0)
    OP_C6(0x05, 0x01, 1000, 1000, 100)
    OP_C6(0x00, 0x03, 16777215, 0, 0)

    Return()

# id: 0x001E offset: 0x7ACA
@scena.Code('func_1E_7ACA')
def func_1E_7ACA():
    OP_C6(0x01, 0x01, 100, 1000, 100)
    OP_C7(0x00, 0x01, 0x01)
    PlaySE(256, 0x00, 0x64)
    OP_C6(0x06, 0x01, 100, 1000, 0)
    OP_C6(0x06, 0x03, -1, 0, 0)
    OP_C6(0x06, 0x01, 1000, 1000, 100)
    OP_C6(0x01, 0x03, 16777215, 0, 0)

    Return()

# id: 0x001F offset: 0x7B1F
@scena.Code('func_1F_7B1F')
def func_1F_7B1F():
    OP_C6(0x02, 0x01, 100, 1000, 100)
    OP_C7(0x00, 0x02, 0x01)
    PlaySE(256, 0x00, 0x64)
    OP_C6(0x07, 0x01, 100, 1000, 0)
    OP_C6(0x07, 0x03, -1, 0, 0)
    OP_C6(0x07, 0x01, 1000, 1000, 100)
    OP_C6(0x02, 0x03, 16777215, 0, 0)

    Return()

# id: 0x0020 offset: 0x7B74
@scena.Code('func_20_7B74')
def func_20_7B74():
    OP_C6(0x03, 0x01, 100, 1000, 100)
    OP_C7(0x00, 0x03, 0x01)
    PlaySE(256, 0x00, 0x64)
    OP_C6(0x08, 0x01, 100, 1000, 0)
    OP_C6(0x08, 0x03, -1, 0, 0)
    OP_C6(0x08, 0x01, 1000, 1000, 100)
    OP_C6(0x03, 0x03, 16777215, 0, 0)

    Return()

# id: 0x0021 offset: 0x7BC9
@scena.Code('func_21_7BC9')
def func_21_7BC9():
    OP_C6(0x04, 0x01, 100, 1000, 100)
    OP_C7(0x00, 0x04, 0x01)
    PlaySE(256, 0x00, 0x64)
    OP_C6(0x09, 0x01, 100, 1000, 0)
    OP_C6(0x09, 0x03, -1, 0, 0)
    OP_C6(0x09, 0x01, 1000, 1000, 100)
    OP_C6(0x04, 0x03, 16777215, 0, 0)

    Return()

# id: 0x0022 offset: 0x7C1E
@scena.Code('func_22_7C1E')
def func_22_7C1E():
    OP_26(543)

    ChrTalk(
        0x00FE,
        (
            'cut in测试哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    OP_D9(0x00, 'CTI00120')
    PlaySE(543, 0x00, 0x64)
    Sleep(2000)

    OP_D9(0x01)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            'cut in测试哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    OP_D9(0x00, 'CTI00130')
    PlaySE(543, 0x00, 0x64)
    Sleep(2000)

    OP_D9(0x01)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            'cut in测试哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    OP_D9(0x00, 'CTI00150')
    FadeOut(300, 0, 100)
    PlaySE(543, 0x00, 0x64)
    Sleep(2000)

    OP_D9(0x01)
    FadeIn(300, 0)

    Return()

# id: 0x0023 offset: 0x7CE6
@scena.Code('func_23_7CE6')
def func_23_7CE6():
    ChrTalk(
        0x00FE,
        (
            '头像测试哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(400, 0, -1)
    OP_C5(0x00, 0, 0, 640, 236, 0, 0, 128, 64, 0, 0, 62, 63, 0x00FFFFFF, 0x00, 'C_VIS225._CH')
    OP_C5(0x01, 0, 0, 640, 242, 0, 239, 128, 64, 0, 0, 62, 63, 0x00FFFFFF, 0x00, 'C_VIS225._CH')
    OP_C5(0x02, 0, 0, 640, 64, 64, 208, 640, 64, 0, 0, 640, 64, 0x00FFFFFF, 0x00, 'C_VIS223._CH')
    OP_C5(0x03, 0, 0, 640, 64, 640, 208, 64, 64, 65, 0, 65, 128, 0x00FFFFFF, 0x00, 'C_VIS225._CH')
    OP_0D()
    OP_C6(0x00, 0x03, -1, 0, 0)
    OP_C6(0x01, 0x03, -1, 0, 0)
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x01, 0x04, 0, 0, 0)
    Sleep(50)

    OP_C6(0x03, 0x03, -1, 0, 0)
    OP_C6(0x03, 0x00, 0, 208000, 800)
    OP_C7(0x00, 0x03, 0x00)
    OP_C6(0x02, 0x03, -1, 0, 0)
    OP_C6(0x00, 0x00, 0, -240000, 2000)
    OP_C6(0x01, 0x00, 0, 480000, 2000)
    OP_C6(0x03, 0x03, 16777215, 500, 0)
    OP_C6(0x02, 0x00, 0, 208000, 800)
    Sleep(600)

    OP_C6(0x02, 0x00, -64000, 208000, 2200)
    OP_C6(0x00, 0x00, 0, 2000, 1600)
    OP_C6(0x01, 0x00, 0, 236000, 1600)
    Sleep(3000)

    FadeIn(0, 0)
    OP_C7(0x01, 0xFF, 0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
