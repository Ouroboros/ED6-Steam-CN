import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1220_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1220   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1220.x'
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
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
    ]

# id: 0x10001 offset: 0xB2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '埃米尔',
            x                   = -1600,
            z                   = -1000,
            y                   = 7600,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
    )

# id: 0x10002 offset: 0xD2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xD2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xD2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -670,
            triggerZ            = -1000,
            triggerY            = 6680,
            triggerRange        = 400,
            actorX              = -1600,
            actorZ              = 500,
            actorY              = 7600,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0xF6
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0xF7
@scena.Code('func_01_F7')
def func_01_F7():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_10A',
    )

    OP_B1('T1220_n')

    Jump('loc_126')

    def _loc_10A(): pass

    label('loc_10A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_11D',
    )

    OP_B1('T1220_y')

    Jump('loc_126')

    def _loc_11D(): pass

    label('loc_11D')

    OP_B1('T1220_n')

    def _loc_126(): pass

    label('loc_126')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_137',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x1A),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_137(): pass

    label('loc_137')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_147',
    )

    OP_10(0x00, 0x00)
    OP_10(0x02, 0x01)

    Jump('loc_154')

    def _loc_147(): pass

    label('loc_147')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_154',
    )

    OP_10(0x00, 0x00)
    OP_10(0x01, 0x01)

    def _loc_154(): pass

    label('loc_154')

    Return()

# id: 0x0002 offset: 0x155
@scena.Code('func_02_155')
def func_02_155():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_16A',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_155')

    def _loc_16A(): pass

    label('loc_16A')

    Return()

# id: 0x0003 offset: 0x16B
@scena.Code('func_03_16B')
def func_03_16B():
    TalkBegin(0x0008)
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
        100,
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '买东西\n'),
            TXT(0x02, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C9',
    )

    OP_0D()
    OP_A9(0x46)
    OP_56(0x00)
    TalkEnd(0x0008)

    Return()

    def _loc_1C9(): pass

    label('loc_1C9')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DA',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_1DA(): pass

    label('loc_1DA')

    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x1DF
@scena.Code('func_04_1DF')
def func_04_1DF():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0412, 1, 0x2091)),
            Expr.Return,
        ),
        'loc_2E3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_28C',
    )

    ChrTalk(
        0x0008,
        (
            '定期船和货车都停开了，\n',
            '看来还没恢复原状呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这里的商品几乎\n',
            '都是从柏斯运来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '话虽如此，我们\n',
            '可是束手无策啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呼，只好叹气了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_2E0')

    def _loc_28C(): pass

    label('loc_28C')

    ChrTalk(
        0x0008,
        (
            '这里的商品几乎\n',
            '都是从柏斯运来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '搬运车不能动的话，\n',
            '要卖的东西也快光了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2E0(): pass

    label('loc_2E0')

    Jump('loc_67F')

    def _loc_2E3(): pass

    label('loc_2E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_405',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_399',
    )

    ChrTalk(
        0x0008,
        (
            '呀，欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '总之还在\n',
            '勉强继续营业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '导力器不能动了，\n',
            '柏斯好像也是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '搬运车不能动的话，\n',
            '我们的商品也很快要断货了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呼，怎么办呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_402')

    def _loc_399(): pass

    label('loc_399')

    ChrTalk(
        0x0008,
        (
            '总之还在\n',
            '勉强继续营业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '导力器不能动了，\n',
            '柏斯好像也是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '一定发生很大的\n',
            '骚乱了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_402(): pass

    label('loc_402')

    Jump('loc_67F')

    def _loc_405(): pass

    label('loc_405')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0380, 1, 0x1C01)),
            Expr.Return,
        ),
        'loc_469',
    )

    ChrTalk(
        0x0008,
        (
            '似乎有很多人\n',
            '为村子捐款呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '真是太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '终于感觉村子\n',
            '恢复往日的明朗了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_67F')

    def _loc_469(): pass

    label('loc_469')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_4E0',
    )

    ChrTalk(
        0x0008,
        (
            '果树园的重建\n',
            '似乎正在进行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '讨论那边\n',
            '不知道是否顺利呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果不齐心合力，\n',
            '复兴就只是梦想啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_67F')

    def _loc_4E0(): pass

    label('loc_4E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            Expr.Return,
        ),
        'loc_5C8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_543',
    )

    ChrTalk(
        0x0008,
        (
            '现在看到军服\n',
            '还是会感到不安呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……战争时期的事\n',
            '一直在脑子里挥之不去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5C5')

    def _loc_543(): pass

    label('loc_543')

    ChrTalk(
        0x0008,
        (
            '王国军的士兵们\n',
            '好像撤退了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然他们并没错，\n',
            '但是看到军服还是会不安啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……战争时期的事\n',
            '一直在脑子里挥之不去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_5C5(): pass

    label('loc_5C5')

    Jump('loc_67F')

    def _loc_5C8(): pass

    label('loc_5C8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_67F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_616',
    )

    ChrTalk(
        0x0008,
        (
            '果树园的损害很严重啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '今年的收获\n',
            '恐怕是不行了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_67F')

    def _loc_616(): pass

    label('loc_616')

    ChrTalk(
        0x0008,
        (
            '呀，欢迎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然火已经灭了，\n',
            '但果树园的损害很严重啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……我们拉文努村\n',
            '今后会怎样呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_67F(): pass

    label('loc_67F')

    TalkEnd(0x0008)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
