import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3119_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3119_1 ._SN')

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
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T3119_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
    OP_59()
    Fade(1000)
    ChrSetPos(0x0101, -560, 0, 5410, 0)
    ChrSetPos(0x00F7, 50, 0, 4460, 0)
    ChrSetPos(0x00F8, -1250, 0, 4210, 0)
    ChrSetPos(0x00F9, -520, 0, 3020, 0)
    CameraMove(-560, 0, 5410, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010450845V#1020F这、这回是什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450846V为什么『卡佩尔』\n',
            '写着这种事！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_283',
    )

    ChrTalk(
        0x0107,
        (
            '#0070450847V#065F可能是盗取了密码\n',
            '更改了数据。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070450848V如果用管理者权限登录\n',
            '任何人都能输入……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010450849V#1004F谁、谁都行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070450850V#561F一、一般是不行的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070450851V就算是我\n',
            '都难以置信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_391')

    def _loc_283(): pass

    label('loc_283')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_30E',
    )

    ChrTalk(
        0x0104,
        (
            '#0040450852V#032F虽然不清楚详情，\n',
            '但似乎是把里面的数据改写了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450853V#031F哈哈哈。\n',
            '要是敌人也只有称赞的份了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_391')

    def _loc_30E(): pass

    label('loc_30E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_391',
    )

    ChrTalk(
        0x0105,
        (
            '#0060450854V#042F虽然不清楚详情\n',
            '但似乎是把内部的数据改写了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060450855V看起来不像是\n',
            '外行人能处理的机器……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_391(): pass

    label('loc_391')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3FC',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450856V#551F真是个深不可测的家伙啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450857V#050F这个暂且不论……\n',
            '笔记记下了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_45D')

    def _loc_3FC(): pass

    label('loc_3FC')

    ChrTalk(
        0x0103,
        (
            '#0030450858V#025F真是个深不可测的家伙啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450859V#020F这个暂且不提……\n',
            '笔记记下了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_45D(): pass

    label('loc_45D')

    ChrTurnDirection(0x0101, 0x00F7, 400)

    ChrTalk(
        0x0101,
        (
            '#0010220821V#1006F嗯，当然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010450861V#1015F接下来好像又是城里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_522',
    )

    ChrTurnDirection(0x0105, 0x0101, 400)

    ChrTalk(
        0x0105,
        (
            '#0060450862V#040F要找的是\n',
            '尖帽子三兄弟吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060450863V这个也是\n',
            '什么比喻吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0105, 400)

    Jump('loc_596')

    def _loc_522(): pass

    label('loc_522')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_596',
    )

    ChrTurnDirection(0x0104, 0x0101, 400)

    ChrTalk(
        0x0104,
        (
            '#0040450864V#030F然后是尖帽子三兄弟吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040450865V这个也是\n',
            '应该是比喻没错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00F7, 0x0104, 400)

    def _loc_596(): pass

    label('loc_596')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_5E3',
    )

    ChrTalk(
        0x0106,
        (
            '#0050450866V#050F好，知道这个就够了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050450867V回城里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_628')

    def _loc_5E3(): pass

    label('loc_5E3')

    ChrTalk(
        0x0103,
        (
            '#0030450868V#020F知道这个就够了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030450869V好，返回城里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_628(): pass

    label('loc_628')

    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
