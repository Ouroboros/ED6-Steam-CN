import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0100_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0100_1 ._SN')

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T0100_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x7A9
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
    Fade(1000)
    SetChrPos(0x0101, 62320, 250, 19870, 239)
    SetChrPos(0x00F7, 64480, 0, 19260, 270)
    SetChrPos(0x00F8, 65420, 0, 20030, 270)
    SetChrPos(0x00F9, 65940, 0, 18510, 269)
    OP_6D(62620, 250, 19470, 0)
    OP_67(0, 7170, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(300000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010471177V#1011F这里是……\n',
            '埃尔格先生的锻冶场吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471178V现在也没有生火，\n',
            '摸起来冰凉凉的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030471179V#027F卡片中的\n',
            '『八眼铁兽』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030471180V……你觉得是这里？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010471181V#1015F嗯……\n',
            '虽说不是很有信心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471182V#1000F那，保险起见还是调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0101, 0x0040)
    OP_8C(0x0101, 239, 400)
    OP_8E(0x0101, 61890, 250, 19380, 1000, 0x00)
    OP_8C(0x0101, 270, 400)
    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0101)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '调查炉中\n',
            '发现了卡片和钥匙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010471183V#1004F……有、有了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 90, 400)
    Fade(1000)
    SetChrChipByIndex(0x0101, 38)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010471184V#1011F嗯……我看看……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    FadeOut(300, 0, 100)
    OP_AD(0x00240093, 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 300, -1, 3)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0170471185V　　　　拿这个钥匙\n',
            '　   打开『打不开的门』。\n',
            '　　寻求的东西在地底深处。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x000001F4)
    Sleep(550)

    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['生锈的钥匙']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(ItemTable['生锈的钥匙'], 1)
    Sleep(400)

    Fade(1000)
    SetChrChipByIndex(0x0101, 65535)
    OP_0D()
    OP_8C(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010471186V#1015F──就这样\n',
            '钥匙是找到了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471187V#1019F不过，这是哪里的钥匙啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030471188V#022F说是『打不开的门』\n',
            '应该也是这市内的某处吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030471189V所有的门都试试看吧。',
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
        'loc_547',
    )

    ChrTalk(
        0x0107,
        (
            '#0070471190V#060F嗯……\n',
            '也只能这样了吧，姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_619')

    def _loc_547(): pass

    label('loc_547')

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5A4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050471191V#053F嗯，也只有这样了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050471192V#050F好，赶快去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_619')

    def _loc_5A4(): pass

    label('loc_5A4')

    If(
        (
            (Expr.Eval, "OP_42(0x07)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5E0',
    )

    ChrTalk(
        0x0108,
        (
            '#0080471193V#070F啊啊，也只有这样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_619')

    def _loc_5E0(): pass

    label('loc_5E0')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_619',
    )

    ChrTalk(
        0x0104,
        (
            '#0040471194V#035F呼，也只有这样了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_619(): pass

    label('loc_619')

    ChrTalk(
        0x0101,
        (
            '#0010471195V#1007F呼，一定就差一步了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471196V#1006F好，再加把劲吧。\n',
            '继续找找看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    OP_28(0x0077, 0x01, 0x0040)
    OP_64(0x03, 0x0001)
    ClearChrFlags(0x0101, 0x0040)
    EventEnd(0x04)

    Return()

# id: 0x0001 offset: 0x68B
@scena.Code('Init')
def Init():
    FadeOut(300, 0, 100)

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
        32,
        1,
        (
            TXT(0x00, '进入地下水路\n'),
            TXT(0x01, '离开\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_6E2'),
        (0x00000001, 'loc_6EE'),
        (-1, 'loc_6EE'),
    )

    def _loc_6E2(): pass

    label('loc_6E2')

    NewScene('ED6_DT21/C0500._SN', 100, 0, 0)
    IdleLoop()

    Jump('loc_6F4')

    def _loc_6EE(): pass

    label('loc_6EE')

    TalkEnd(0x00FF)

    Jump('loc_6F4')

    def _loc_6F4(): pass

    label('loc_6F4')

    Sleep(30)

    Return()

# id: 0x0002 offset: 0x6FA
@scena.Code('ReInit')
def ReInit():
    FadeOut(0, 0, -1)
    OP_0D()
    OP_6D(75350, 0, 18760, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0000, 75350, 0, 18760, 270)
    SetChrPos(0x0001, 75350, 0, 18760, 270)
    SetChrPos(0x0002, 75350, 0, 18760, 270)
    SetChrPos(0x0003, 75350, 0, 18760, 270)
    OP_30(0x00)
    SetMapFlags(0x00000001)
    OP_69(0x0000, 0x00000000)
    FadeIn(1000, 0)
    ClearMapFlags(0x00000080)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
