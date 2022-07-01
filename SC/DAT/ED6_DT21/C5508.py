import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5508_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5508   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5508.x'
    header.mapIndex       = 1
    header.bgm            = 34
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x9BE
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
        ScenaEventData(
            x           = -8100,
            y           = -200,
            z           = -42000,
            range       = 5600,
            dword_10    = 0x00001C20,
            dword_14    = 0xFFFF7874,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000002,
        ),
    )

# id: 0x10005 offset: 0xC8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xC8
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0204, 3, 0x1023)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D9',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x0003)

    def _loc_D9(): pass

    label('loc_D9')

    Return()

# id: 0x0001 offset: 0xDA
@scena.Code('Init')
def Init():
    OP_10(0x01, 0x00)
    OP_16(0x02, 0x00000FA0, 0xFFFE0818, 0xFFFDCD80, 0x00230070)

    Return()

# id: 0x0002 offset: 0xF0
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0204, 2, 0x1022)),
            Expr.Return,
        ),
        'loc_10E',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_11F')

    def _loc_10E(): pass

    label('loc_10E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0202, 2, 0x1012)),
            Expr.Return,
        ),
        'loc_11F',
    )

    ExecExpressionWithReg(
        0x0003,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_11F(): pass

    label('loc_11F')

    SetMapFlags(0x00000080)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_C5(0x00, 0x0000, 0x0000, 0x0280, 0x01E0, 0x0000, 0x0000, 0x0300, 0x0200, 0x0000, 0x0000, 0x0280, 0x01E0, 0x00FFFFFF, 0x00, 'C_VIS137._CH')
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x00, 0x03, -1, 500, 0)
    OP_C7(0x00, 0x00, 0x03)
    OP_77(0x00, 0x00, 0x00, 0x00, 0x00000000)

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_190(): pass

    label('loc_190')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xFF),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4AD',
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_1BB'),
        (0x00000001, 'loc_1E7'),
        (0x00000002, 'loc_224'),
        (-1, 'loc_276'),
    )

    def _loc_1BB(): pass

    label('loc_1BB')

    Menu(
        0,
        30,
        80,
        0,
        (
            TXT(0x00, '【训练场宿舍】\n'),
            TXT(0x01, '【巴斯塔尔水道】\n'),
        ),
    )

    Jump('loc_276')

    def _loc_1E7(): pass

    label('loc_1E7')

    Menu(
        0,
        30,
        80,
        0,
        (
            TXT(0x00, '【训练场宿舍】\n'),
            TXT(0x01, '【巴斯塔尔水道】\n'),
            TXT(0x02, '【圣科洛瓦森林】\n'),
        ),
    )

    Jump('loc_276')

    def _loc_224(): pass

    label('loc_224')

    Menu(
        0,
        30,
        80,
        0,
        (
            TXT(0x00, '【训练场宿舍】\n'),
            TXT(0x01, '【巴斯塔尔水道】\n'),
            TXT(0x02, '【圣科洛瓦森林】\n'),
            TXT(0x03, '【格林姆瑟尔小要塞】\n'),
        ),
    )

    Jump('loc_276')

    def _loc_276(): pass

    label('loc_276')

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
        (0x00000000, 'loc_2A0'),
        (0x00000001, 'loc_320'),
        (0x00000002, 'loc_3A2'),
        (0x00000003, 'loc_424'),
        (-1, 'loc_4AA'),
    )

    def _loc_2A0(): pass

    label('loc_2A0')

    SetChrName('')
    SetMessageWindowPos(-1, 120, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '要移动至【训练场宿舍】吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        1,
        10,
        -1,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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

    OP_5F(0x0001)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_30D'),
        (0x00000001, 'loc_31A'),
        (-1, 'loc_31D'),
    )

    def _loc_30D(): pass

    label('loc_30D')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_31D')

    def _loc_31A(): pass

    label('loc_31A')

    Jump('loc_31D')

    def _loc_31D(): pass

    label('loc_31D')

    Jump('loc_4AA')

    def _loc_320(): pass

    label('loc_320')

    SetChrName('')
    SetMessageWindowPos(-1, 120, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '要移动至【巴斯塔尔水道】吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        1,
        10,
        -1,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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

    OP_5F(0x0001)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_38F'),
        (0x00000001, 'loc_39C'),
        (-1, 'loc_39F'),
    )

    def _loc_38F(): pass

    label('loc_38F')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_39F')

    def _loc_39C(): pass

    label('loc_39C')

    Jump('loc_39F')

    def _loc_39F(): pass

    label('loc_39F')

    Jump('loc_4AA')

    def _loc_3A2(): pass

    label('loc_3A2')

    SetChrName('')
    SetMessageWindowPos(-1, 120, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '要移动至【圣科洛瓦森林】吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        1,
        10,
        -1,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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

    OP_5F(0x0001)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_411'),
        (0x00000001, 'loc_41E'),
        (-1, 'loc_421'),
    )

    def _loc_411(): pass

    label('loc_411')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_421')

    def _loc_41E(): pass

    label('loc_41E')

    Jump('loc_421')

    def _loc_421(): pass

    label('loc_421')

    Jump('loc_4AA')

    def _loc_424(): pass

    label('loc_424')

    SetChrName('')
    SetMessageWindowPos(-1, 120, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '要移动至【格林姆瑟尔小要塞】吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        1,
        10,
        -1,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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

    OP_5F(0x0001)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_497'),
        (0x00000001, 'loc_4A4'),
        (-1, 'loc_4A7'),
    )

    def _loc_497(): pass

    label('loc_497')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4A7')

    def _loc_4A4(): pass

    label('loc_4A4')

    Jump('loc_4A7')

    def _loc_4A7(): pass

    label('loc_4A7')

    Jump('loc_4AA')

    def _loc_4AA(): pass

    label('loc_4AA')

    Jump('loc_190')

    def _loc_4AD(): pass

    label('loc_4AD')

    Switch(
        (
            (Expr.PushReg, 0x2),
            Expr.Return,
        ),
        (0x00000000, 'loc_4C6'),
        (0x00000001, 'loc_4FA'),
        (0x00000002, 'loc_52E'),
        (0x00000003, 'loc_562'),
        (-1, 'loc_596'),
    )

    def _loc_4C6(): pass

    label('loc_4C6')

    OP_C6(0x00, 0x00, -640000, 0, 2000)
    OP_C6(0x00, 0x01, 2000, 2000, 2000)
    OP_C6(0x00, 0x03, 16777215, 2000, 0)
    OP_C7(0x00, 0x00, 0x03)

    Jump('loc_596')

    def _loc_4FA(): pass

    label('loc_4FA')

    OP_C6(0x00, 0x00, -358000, -37000, 2000)
    OP_C6(0x00, 0x01, 2000, 2000, 2000)
    OP_C6(0x00, 0x03, 16777215, 2000, 0)
    OP_C7(0x00, 0x00, 0x03)

    Jump('loc_596')

    def _loc_52E(): pass

    label('loc_52E')

    OP_C6(0x00, 0x00, -362000, -266000, 2000)
    OP_C6(0x00, 0x01, 2000, 2000, 2000)
    OP_C6(0x00, 0x03, 16777215, 2000, 0)
    OP_C7(0x00, 0x00, 0x03)

    Jump('loc_596')

    def _loc_562(): pass

    label('loc_562')

    OP_C6(0x00, 0x00, -64000, -340000, 2000)
    OP_C6(0x00, 0x01, 2000, 2000, 2000)
    OP_C6(0x00, 0x03, 16777215, 2000, 0)
    OP_C7(0x00, 0x00, 0x03)

    Jump('loc_596')

    def _loc_596(): pass

    label('loc_596')

    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_77(0xFF, 0xFF, 0xFF, 0x00, 0x00000000)

    Switch(
        (
            (Expr.PushReg, 0x2),
            Expr.Return,
        ),
        (0x00000000, 'loc_5C7'),
        (0x00000001, 'loc_5D3'),
        (0x00000002, 'loc_5DF'),
        (0x00000003, 'loc_5EB'),
        (-1, 'loc_5F7'),
    )

    def _loc_5C7(): pass

    label('loc_5C7')

    NewScene('ED6_DT21/T5100._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5F7')

    def _loc_5D3(): pass

    label('loc_5D3')

    NewScene('ED6_DT21/C5503._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_5F7')

    def _loc_5DF(): pass

    label('loc_5DF')

    NewScene('ED6_DT21/C5507._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_5F7')

    def _loc_5EB(): pass

    label('loc_5EB')

    NewScene('ED6_DT21/C5508._SN', 101, 0, 0)
    IdleLoop()

    Jump('loc_5F7')

    def _loc_5F7(): pass

    label('loc_5F7')

    Return()

# id: 0x0003 offset: 0x5F8
@scena.Code('func_03_5F8')
def func_03_5F8():
    EventBegin(0x00)
    OP_6D(-770, 500, -3680, 0)
    OP_67(0, 12230, -10000, 0)
    OP_6B(5220, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -2000, 0, -31300, 13)
    SetChrPos(0x010A, -200, 0, -31500, 360)
    OP_C8(0x0200, 0x0046, 'C_PLAC03._CH', 0x00, 0x07D0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_067D')
    def lambda_067D():
        OP_6D(-770, 0, -21740, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_067D)

    Sleep(1500)

    @scena.Lambda('lambda_069A')
    def lambda_069A():
        OP_8E(0x00FE, -2000, 0, -21130, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_069A)

    Sleep(400)

    @scena.Lambda('lambda_06BA')
    def lambda_06BA():
        OP_8E(0x00FE, -200, 0, -21130, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x010A, 0x0000, lambda_06BA)

    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    Fade(1000)
    OP_6D(-590, 0, -18490, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3080, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x010A, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010191422V#1004F#6P这就是『格林姆瑟尔小要塞』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191423V#5P#812F好厉害……\n',
            '是相当正统的训练设施哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191424V总之从外面看起来\n',
            '几乎感觉不到有人的气息……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8E(0x0101, -800, 0, -19470, 2000, 0x00)

    @scena.Lambda('lambda_07EB')
    def lambda_07EB():
        ChrTurnDirection(0x00FE, 0x0101, 500)

        ExitThread()

    DispatchAsync(0x010A, 0x0000, lambda_07EB)

    OP_8C(0x0101, 90, 500)
    Sleep(200)

    OP_8C(0x0101, 0, 500)
    OP_8C(0x0101, 270, 500)
    Sleep(400)

    OP_8C(0x0101, 0, 500)
    OP_8C(0x0101, 180, 500)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010191425V#1002F#5P嗯，没有错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191426V地面上还留有一些人\n',
            '最近走过的痕迹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191427V#811F呵呵，看来追踪训练\n',
            '的成果发挥作用了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191428V#810F照这个情况，敌人的数量\n',
            '应该不会太多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191429V约三四人的样子吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191430V#1006F#5P虽然说敌人似乎相当厉害……\n',
            '但我们毕竟也是正游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191431V还不至于无法对抗吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191432V#816F嗯，尽全力吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1023)
    OP_28(0x0080, 0x01, 0x0400)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
