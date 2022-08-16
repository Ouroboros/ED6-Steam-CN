import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0403_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0403_1 ._SN')

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/C0403_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, -6090, 250, 1060, 90)
    ChrSetPos(0x0103, -6070, 250, 2780, 180)
    ChrSetPos(0x00F8, -8390, 250, 160, 90)
    ChrSetPos(0x00F9, -7890, 250, 2110, 135)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_122',
    )

    ChrSetPos(0x00F9, -8390, 250, 160, 90)
    ChrSetPos(0x00F8, -7890, 250, 2110, 135)

    def _loc_122(): pass

    label('loc_122')

    CameraMove(-6780, 250, 1000, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    If(
        (
            (Expr.GetChrWork, 0x8, 0x2),
            (Expr.PushLong, 0xFA),
            Expr.Leq,
            Expr.Return,
        ),
        'loc_22C',
    )

    Sleep(1000)

    TerminateThread(0x0008, 0x01)
    ChrTurnDirection(0x0008, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0x8, 0x4),
            (Expr.PushLong, 0xB4),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1AE',
    )

    @scena.Lambda('lambda_0192')
    def lambda_0192():
        OP_97(0x0008, -4000, 1000, 360000, 7000, 0x0001)
        Yield()

        Jump('lambda_0192')

    DispatchAsync2(0x0008, 0x0001, lambda_0192)

    Jump('loc_1CD')

    def _loc_1AE(): pass

    label('loc_1AE')

    @scena.Lambda('lambda_01B4')
    def lambda_01B4():
        OP_97(0x0008, -4000, 1000, -360000, 7000, 0x0001)
        Yield()

        Jump('lambda_01B4')

    DispatchAsync2(0x0008, 0x0001, lambda_01B4)

    def _loc_1CD(): pass

    label('loc_1CD')

    ChrSetChipByIndex(0x0008, 11)
    ChrClearFlags(0x0008, 0x0400)
    ChrSetFlags(0x0008, 0x0004)
    PlaySE(347, 0x00, 0x64)
    PlaySE(140, 0x00, 0x64)
    def _loc_1E6(): pass

    label('loc_1E6')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_21E',
    )

    ExecExpressionWithValue(
        0x0008,
        0x02,
        (
            (Expr.PushLong, 0xC8),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.GetChrWork, 0x8, 0x2),
            (Expr.PushLong, 0x2328),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_216',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 2000)

    Jump('loc_21E')

    def _loc_216(): pass

    label('loc_216')

    Sleep(15)

    Jump('loc_1E6')

    def _loc_21E(): pass

    label('loc_21E')

    TerminateThread(0x0008, 0x01)
    ChrSetFlags(0x0008, 0x0080)
    ChrClearFlags(0x0008, 0x0004)

    def _loc_22C(): pass

    label('loc_22C')

    WaitForThreadExit(0x0008, 0x0001)
    StopEffect(0x00, 0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['白金戒指']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['白金戒指'], 1)

    ChrTalk(
        0x0101,
        (
            '#0010460813V#1004F戒、戒指……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460814V为什么这里\n',
            '会有这种东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_482',
    )

    ChrTalk(
        0x0103,
        (
            '#0030260945V#022F……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460816V刚才在这里的鸟……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460817V……是乌鸦吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010460818V#1002F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460819V好像是。\n',
            '但实在有点反常……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010460820V#1020F……啊……………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460821V难道说这个戒指……\n',
            '是阿鲁姆的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0103, 180, 400)

    ChrTalk(
        0x0103,
        (
            '#0030460822V#022F有这个可能。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460823V回城后去向本人\n',
            '确认一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460824V#1002F嗯，明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0072, 0x01, 0x0004)

    Jump('loc_6D8')

    def _loc_482(): pass

    label('loc_482')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4BA',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460825V#043F是谁掉的东西呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_566')

    def _loc_4BA(): pass

    label('loc_4BA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4F0',
    )

    ChrTalk(
        0x0107,
        (
            '#0070460826V#064F是谁掉的东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_566')

    def _loc_4F0(): pass

    label('loc_4F0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_537',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460827V#030F唔，大概是失物\n',
            '总觉得深具意义。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_566')

    def _loc_537(): pass

    label('loc_537')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_566',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460828V#073F是失物吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_566(): pass

    label('loc_566')

    ChrTalk(
        0x0103,
        (
            '#0030460829V#026F……如果是的话，这地方也太奇怪了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460830V没有人会到\n',
            '这种地方来郊游吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460831V#1007F确、确实如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460832V#1003F嗯～看起来\n',
            '好像也没有刻记号的样子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460833V……会是谁的戒指呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460834V#020F嗯，总之\n',
            '先暂时保管着吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460835V如果在意的话\n',
            '就去城镇里调查看看好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460836V#1000F是呀，先收着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6D8(): pass

    label('loc_6D8')

    OP_28(0x0072, 0x01, 0x4000)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
