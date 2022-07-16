import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0200_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0200   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '乔丝特'),
    TXT(0x02, '洛连特市街道'),
    TXT(0x03, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0200.x'
    header.mapIndex       = 12
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x967
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0xFFFFE82C,
            dword_04        = 0x00000000,
            dword_08        = 0x00000032,
            word_0C         = 0x0004,
            word_0E         = 0x005A,
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
            word_3A         = 12,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0xFFFFE82C,
            dword_04        = 0x00000000,
            dword_08        = 0x00000032,
            word_0C         = 0x0004,
            word_0E         = 0x005A,
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
            word_3A         = 12,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xEC
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH02330._CH', 'ED6_DT07/CH02330P._CP'),
    ]

# id: 0x10002 offset: 0xF6
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -20690,
            z                   = 0,
            y                   = -180,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x136
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x136
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x136
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 13870,
            triggerZ            = 3700,
            triggerY            = -4460,
            triggerRange        = 500,
            actorX              = 13870,
            actorZ              = 4200,
            actorY              = -4460,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 8189,
            triggerZ            = 450,
            triggerY            = 0,
            triggerRange        = 800,
            actorX              = 8189,
            actorZ              = 1450,
            actorY              = 0,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x17E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 2, 0x25A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_191',
    )

    OP_64(0x00, 0x0001)

    Jump('loc_191')

    def _loc_191(): pass

    label('loc_191')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_1A1'),
        (0x00000067, 'loc_1A8'),
        (-1, 'loc_1B4'),
    )

    def _loc_1A1(): pass

    label('loc_1A1')

    Event(0, 0x0003)

    Jump('loc_1B4')

    def _loc_1A8(): pass

    label('loc_1A8')

    OP_6C(225000, 0)

    Jump('loc_1B4')

    def _loc_1B4(): pass

    label('loc_1B4')

    Return()

# id: 0x0001 offset: 0x1B5
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1CD',
    )

    OP_B1('t0200_y')

    Jump('loc_1D6')

    def _loc_1CD(): pass

    label('loc_1CD')

    OP_B1('t0200_n')

    def _loc_1D6(): pass

    label('loc_1D6')

    OP_16(0x02, 4000, -117000, -128000, 196610)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 2, 0x25A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1FC',
    )

    OP_72(0x0000, 0x0010)

    Jump('loc_200')

    def _loc_1FC(): pass

    label('loc_1FC')

    OP_64(0x01, 0x0001)

    def _loc_200(): pass

    label('loc_200')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 2, 0x25A)),
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 1, 0x261)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_215',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x57),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_215(): pass

    label('loc_215')

    Return()

# id: 0x0002 offset: 0x216
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    CameraMove(13870, 3700, -4460, 1000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 0, 0x260)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2CB',
    )

    ChrTalk(
        0x0101,
        (
            '#0010011072V#004F啊，这里的栏杆有划痕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011073V#012F真的啊……\n',
            '而且还是刚划上去的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020011074V#012F看起来是用金属之类的东西挂过的痕迹。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x004C, 0, 0x260))
    OP_28(0x001A, 0x01, 0x0080)

    Jump('loc_347')

    def _loc_2CB(): pass

    label('loc_2CB')

    ChrTalk(
        0x0101,
        (
            '#0010011075V#002F栏杆有划痕……\n',
            '看起来是用金属之类的东西弄成的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011076V#012F嗯，\n',
            '先把这些线索详细记录在手册上再说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_347(): pass

    label('loc_347')

    EventEnd(0x01)

    Return()

# id: 0x0003 offset: 0x34A
@scena.Code('func_03_34A')
def func_03_34A():
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0049, 7, 0x24F))
    OP_28(0x0003, 0x04, 0x10)
    OP_28(0x0003, 0x01, 0x0200)
    OP_28(0x0003, 0x01, 0x0400)
    OP_28(0x0004, 0x04, 0x40)
    OP_28(0x0006, 0x04, 0x40)
    SetMapFlags(0x00400000)
    ClearMapFlags(0x00000001)
    ClearChrFlags(0x0008, 0x0080)
    CameraMove(2040, 0, 650, 0)
    OP_6C(135000, 0)
    SetChrPos(0x0101, 1770, 0, 690, 270)
    SetChrPos(0x0102, 1640, 0, -790, 270)
    SetChrPos(0x0008, -450, 0, -60, 90)
    CameraMove(750, 0, -40, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010010360V#000F原来你明天\n',
            '就要坐定期船回去了啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090010361V#217F嗯，是的。\n',
            '因为学院快要开学了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010362V#010F#2P原来如此，\n',
            '是趁着学校放假的机会出来调查的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010363V#007F啊～～真遗憾。\n',
            '好不容易认识了一个朋友……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010364V#000F以后还有机会见面吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0090010365V#217F嗯……\n',
            '我也希望能再见到你们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090010366V#218F那么后会有期哦。\n',
            '艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0008, 270, 400)
    ChrWalkTo(0x0008, -9140, 0, 280, 3000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010010367V#001F啊～真是个好女孩呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010368V#001F虽然看起来像个大小姐，\n',
            '不过却完全没有架子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010369V#013F#2P………嗯…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010010370V#004F约修亚？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010371V#006F哎呀，难道说～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010372V#006F你喜欢的类型是那样的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010373V#014F#2P啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020010374V#012F#2P你、你在乱说些什么呀！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010375V#006F脸红了、脸红了⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010376V#001F呀～姐姐我真是吃了一惊呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010377V#001F原来约修亚喜欢的是\n',
            '大小姐类型的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010378V#001F下次见面之前，\n',
            '记得一定要准备好能打动人家芳心的告白哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020010379V#018F#2P哼，你不要再自编自演了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0102, 270, 400)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020010380V#013F#2P真是的，完全不了解别人的心情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010381V#004F咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020010382V#015F#2P……没什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020010383V#010F#2P好了，我们快点去协会报告吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020010384V父亲交待的工作还有一件就完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010010385V#004F啊，对呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010010386V#001F嗯，鼓足干劲去做吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0008, 0x0080)
    EventEnd(0x00)
    ClearMapFlags(0x00400000)

    Return()

# id: 0x0004 offset: 0x90B
@scena.Code('func_04_90B')
def func_04_90B():
    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    PlaySE(116, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
