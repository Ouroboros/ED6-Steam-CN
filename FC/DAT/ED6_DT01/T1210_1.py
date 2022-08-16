import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1210_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1210_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T1210.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
    )

# id: 0x10000 offset: 0x64
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10001 offset: 0x64
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0x64
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x64
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x64
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x64
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.Eval, "OP_29(0x000E, 0x00, 0x04)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_65F',
    )

    EventBegin(0x00)
    OP_69(0x00FE, 1000)
    OP_28(0x000E, 0x04, 0x08)
    OP_28(0x000E, 0x04, 0x04)
    OP_28(0x000E, 0x01, 0x0001)
    OP_28(0x000E, 0x01, 0x0002)
    OP_28(0x000E, 0x01, 0x0004)
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x00FE,
        (
            '#1180151395V哦…………！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180151396V难道说，\n',
            '你们就是游击士协会派来的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180151397V一定是看了公告板\n',
            '而赶过来的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x000E, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_210',
    )

    ChrTalk(
        0x0101,
        (
            '#0010151398V#000F嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#1180151399V哦，那真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180151400V老朽名叫莱森，\n',
            '是本村的村长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180151401V正如你们所知的那样，\n',
            '最近村庄深处的山道上\n',
            '出现了一只凶暴的魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_354')

    def _loc_210(): pass

    label('loc_210')

    OP_28(0x000E, 0x04, 0x02)

    ChrTalk(
        0x0101,
        (
            '#0010151402V#000F公告板？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#1180151403V老朽名叫莱森。\n',
            '是本村的村长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180151404V其实最近在村庄深处的山道上\n',
            '出现了一只凶暴的魔兽……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180151405V希望游击士协会的各位\n',
            '能够帮忙消灭它。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x000E, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_354',
    )

    ChrTalk(
        0x0101,
        (
            '#0010151406V#004F咦……？！\n',
            '有这样的事情？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030151407V#022F能告诉我们详细的情况吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_354(): pass

    label('loc_354')

    ChrTalk(
        0x0102,
        (
            '#0020151408V#012F您知道出没的是什么样的魔兽吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 0)

    ChrTalk(
        0x00FE,
        (
            '#1180151409V我也不太清楚，\n',
            '因为还没有可靠的目击者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180151410V不过，\n',
            '恐怕是一种潜伏等待猎物到来，\n',
            '然后出来将其捕获的魔兽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180151411V在矿山还很兴旺的时候\n',
            '也曾经出现过这种魔兽，\n',
            '大家对此都感到十分苦恼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030151412V#022F……原来如此，是潜伏着的魔兽啊。\n',
            '这就有些麻烦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030151413V必须在山道上仔细搜索，\n',
            '把魔兽隐藏的地点找出来才行。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180151414V矿山荒废之后就没人再去那里了，\n',
            '我以为那些魔兽\n',
            '已经进入了休眠状态……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180151415V到底为什么\n',
            '又再次出现了呢…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#1180151416V过一阵就是今年\n',
            '开始种植树苗的时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180151417V村里的人为此都很担心。\n',
            '你们还可以去找守门人菲戈，\n',
            '也许他能告诉你们更多的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180151418V刻不容缓，\n',
            '请务必帮我们消灭掉魔兽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)

    Jump('loc_7D3')

    def _loc_65F(): pass

    label('loc_65F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_6E1',
    )

    ChrTalk(
        0x00FE,
        (
            '#1180151416V过一阵就是今年\n',
            '开始种植树苗的时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180151420V现在已经刻不容缓了，\n',
            '请务必帮我们消灭掉魔兽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D3')

    def _loc_6E1(): pass

    label('loc_6E1')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '#1180151421V哦，各位，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180151422V有没有什么成果呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151423V#003F抱歉，\n',
            '可能还要花些时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#1180151416V过一阵就是今年\n',
            '开始种植树苗的时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180151420V现在已经刻不容缓了，\n',
            '请务必帮我们消灭掉魔兽啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7D3(): pass

    label('loc_7D3')

    Return()

# id: 0x0001 offset: 0x7D4
@scena.Code('func_01_7D4')
def func_01_7D4():
    OP_28(0x000E, 0x01, 0x0800)
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    If(
        (
            (Expr.Eval, "OP_29(0x000E, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_885',
    )

    ChrTalk(
        0x00FE,
        (
            '#1180151421V哦，各位，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180151422V有没有什么成果呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010151512V#001F呵呵呵呵呵⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151513V已经解决掉啦☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_95B')

    def _loc_885(): pass

    label('loc_885')

    ChrTalk(
        0x00FE,
        (
            '#1180151514V哦，是你们。\n',
            '你们就是游击士协会派来的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180151397V一定是看了公告板\n',
            '而赶过来的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010151512V#001F呵呵呵呵呵⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010151517V通缉魔兽的话，\n',
            '已经解决掉啦☆',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_95B(): pass

    label('loc_95B')

    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '#1180151518V哦哦，那真是好消息！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180151519V太好了，\n',
            '这样我们今年就可以\n',
            '安安心心地种植树苗了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180151520V真的是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1180151521V我们这个偏僻的小村，\n',
            '随时都欢迎你们的到来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151522V#000F嗯，谢谢村长先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
