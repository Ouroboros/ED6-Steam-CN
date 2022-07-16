import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1101_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1101_1 ._SN')

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
    header.bgm            = 11
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x3AE
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10001 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('PreInit')
def PreInit():
    TalkBegin(0x0014)

    ChrTalk(
        0x00FE,
        (
            '#1370151183V准备好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_80(): pass

    label('loc_80')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B1',
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(300, 0, 100)

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【好了】\n'),
            TXT(0x01, '【对不起，还没有】\n'),
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
        (0x00000000, 'loc_EE'),
        (0x00000001, 'loc_228'),
        (-1, 'loc_2AE'),
    )

    def _loc_EE(): pass

    label('loc_EE')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_28(0x0010, 0x04, 0x08)
    OP_28(0x0010, 0x01, 0x0004)

    ChrTalk(
        0x0101,
        (
            '#0010151184V#006F好了，已经万事俱备了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1370151185V我也准备好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1370151186V那么，接下来就靠你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030151187V#020F古罗尼山顶，\n',
            '从这里一直向西就可以到达了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151188V路途比较远，\n',
            '要打起精神来哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0103, 400)

    ChrTalk(
        0x0102,
        (
            '#0020151189V#010F嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151190V#000F好了，出发吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0001)

    Jump('loc_2AE')

    def _loc_228(): pass

    label('loc_228')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010151191V#000F对不起，\n',
            '还要再准备一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#1370151192V请你们快点回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1370151193V我有很重要的一笔生意要谈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AE')

    def _loc_2AE(): pass

    label('loc_2AE')

    Jump('loc_80')

    def _loc_2B1(): pass

    label('loc_2B1')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    TalkEnd(0x0014)

    Return()

# id: 0x0001 offset: 0x2BF
@scena.Code('Init')
def Init():
    FadeOut(1000, 0, -1)
    OP_0D()
    FormationAddMember(0x34, 0x03)
    NewScene('ED6_DT01/R1200._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0002 offset: 0x2D7
@scena.Code('ReInit')
def ReInit():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    SetChrPos(0x0101, 24400, 0, 46300, 270)
    SetChrPos(0x0102, 25400, 0, 45300, 270)
    SetChrPos(0x0103, 24500, 0, 44300, 270)
    OP_69(0x0014, 0)
    TalkBegin(0x0014)
    FadeIn(1000, 0)
    OP_0D()
    ChrTurnDirection(0x0101, 0x0014, 400)

    ChrTalk(
        0x0101,
        (
            '#0010151194V#501F对不起啊，哈尔德先生。\n',
            '我们还要再补充一下装备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0014, 0x0101, 400)

    ChrTalk(
        0x0014,
        (
            '#1370151195V我会在这里等着的，\n',
            '请尽量快一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)
    TalkEnd(0x0014)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
